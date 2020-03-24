import os
import re
import ROOT
import root_pandas
import numpy as np
import pandas as pd
from os import makedirs
from os import environ as env
from time import time
from collections import OrderedDict
from plotter.evaluate_nn import Evaluator
from plotter.sample import get_data_samples, get_mc_samples, get_signal_samples
from plotter.variables import variables
from plotter.utils import plot_dir
from plotter.cmsstyle import CMS_lumi

from rootpy.plotting import Hist, HistStack, Legend, Canvas, Graph, Pad
from rootpy.plotting.style import get_style, set_style
from rootpy.plotting.utils import draw
from pdb import set_trace

import logging
logging.disable(logging.DEBUG)


ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(False)

class Plotter(object):

    def __init__(self            , 
                 channel         , 
                 year            ,
                 base_dir        ,
                 post_fix        ,
                 selection_data  ,
                 selection_mc    ,
                 selection_tight ,
                 pandas_selection,
                 lumi            ,
                 model           , 
                 transformation  ,
                 features        ,
                 process_signals , 
                 plot_signals    ,
                 blinded         ,
                 datacards=[]    ,
                 mini_signals=False,
                 do_ratio=True):

        self.channel          = channel.split('_')[0]
        self.year             = year
        self.full_channel     = channel
        self.base_dir         = base_dir 
        self.post_fix         = post_fix 
        self.selection_data   = ' & '.join(selection_data)
        self.selection_mc     = ' & '.join(selection_mc)
        self.selection_tight  = selection_tight
        self.pandas_selection = pandas_selection
        self.lumi             = lumi
        self.model            = model          
        self.transformation   = transformation 
        self.features         = features 
        self.process_signals  = process_signals    
        self.plot_signals     = plot_signals if self.process_signals else []
        self.blinded          = blinded      
        self.selection_lnt    = 'not (%s)' %self.selection_tight
        self.do_ratio         = do_ratio
        self.mini_signals     = mini_signals
        self.datacards        = datacards
    
    def total_weight_calculator(self, df, weight_list, scalar_weights=[]):
        total_weight = df[weight_list[0]].to_numpy().astype(np.float)
        for iw in weight_list[1:]:
            total_weight *= df[iw].to_numpy().astype(np.float)
        for iw in scalar_weights:
            total_weight *= iw
        return total_weight

    def create_canvas(self, ratio=True):
        if ratio:
            self.canvas = Canvas(width=700, height=700) ; self.canvas.Draw()
            self.canvas.cd() ; self.main_pad   = Pad(0.  , 0.25, 1. , 1.  ) ; self.main_pad .Draw()
            self.canvas.cd() ; self.ratio_pad  = Pad(0.  , 0.  , 1. , 0.25) ; self.ratio_pad.Draw()

            self.main_pad.SetTicks(True)
            self.main_pad.SetBottomMargin(0.)
            self.main_pad.SetLeftMargin(0.15)
            self.main_pad.SetRightMargin(0.15)
            self.ratio_pad.SetLeftMargin(0.15)
            self.ratio_pad.SetRightMargin(0.15)
            self.ratio_pad.SetTopMargin(0.)   
            self.ratio_pad.SetGridy()
            self.ratio_pad.SetBottomMargin(0.3)
        
        else:
            self.canvas = Canvas(width=700, height=700) ; self.canvas.Draw()
            self.canvas.cd() ; self.main_pad   = Pad(0. , 0. , 1., 1.  )    ; self.main_pad .Draw()
            self.canvas.cd() ; self.ratio_pad  = Pad(-1., -1., -.9, -.9)    ; self.ratio_pad.Draw() # put it outside the canvas
            self.main_pad.SetTicks(True)
            self.main_pad.SetTopMargin(0.15)
            self.main_pad.SetBottomMargin(0.15)
            self.main_pad.SetLeftMargin(0.15)
            self.main_pad.SetRightMargin(0.15)

    def create_kanvas(self):
        self.kanvas = Canvas(width=700, height=700) ; self.kanvas.Draw()
        self.kanvas.cd() ; self.kpad   = Pad(0. , 0. , 1., 1.  )    ; self.kpad .Draw()
        self.kpad.SetTicks(True)
        self.kpad.SetTopMargin(0.15)
        self.kpad.SetBottomMargin(0.15)
        self.kpad.SetLeftMargin(0.15)
        self.kpad.SetRightMargin(0.15)

    def create_datacards(self, data, bkgs, signals, label, protect_empty_bins=['nonprompt']):  
        '''
        FIXME! For now this is specific to the data-driven case
        '''  
        # save a ROOT file with histograms, aka datacard
        datacard_dir = '/'.join([self.plt_dir, 'datacards'])
        makedirs(datacard_dir, exist_ok=True)
        outfile = ROOT.TFile.Open('/'.join([datacard_dir, 'datacard_%s.root' %label]), 'recreate')
        outfile.cd()
        
        # data in tight
        data.name = 'data_obs'
        data.Write()
        
        # reads off a dictionary
        for bkg_name, bkg in bkgs.items():
            bkg.name = bkg_name.split('#')[0]
            bkg.drawstyle = 'HIST E'
            bkg.color = 'black'
            bkg.linewidth = 2
            
            # manual protection against empty bins, that would make combine crash
            if bkg_name in protect_empty_bins:
                for ibin in bkg.bins_range():
                    if bkg.GetBinContent(ibin)<=0.:
                        bkg.SetBinContent(ibin, 1e-2)
                        bkg.SetBinError(ibin, np.sqrt(1e-2))
            
            bkg.Write()

        # signals
        for isig in signals:
            isig.name = isig.name.split('#')[0]
            isig.drawstyle = 'HIST E'
            isig.color = 'black'
            isig.Write()

            # print out the txt datacard
            with open('/'.join([datacard_dir, 'datacard_%s_%s.txt' %(label, isig.name)]), 'w') as card:
                card.write(
'''
imax 1 number of bins
jmax * number of processes minus 1
kmax * number of nuisance parameters
--------------------------------------------------------------------------------------------------------------------------------------------
shapes *    {cat} datacard_{cat}.root $PROCESS $PROCESS_$SYSTEMATIC
--------------------------------------------------------------------------------------------------------------------------------------------
bin               {cat}
observation       {obs:d}
--------------------------------------------------------------------------------------------------------------------------------------------
bin                                                     {cat}                          {cat}                            {cat}
process                                                 {signal_name}                  nonprompt                        prompt
process                                                 0                              1                                2
rate                                                    {signal:.4f}                   {nonprompt:.4f}                  {prompt:.4f}
--------------------------------------------------------------------------------------------------------------------------------------------
lumi                                    lnN             1.025                          -                                -   
norm_prompt_{ch}_{cat}                  lnN             -                              -                                1.15   
norm_nonprompt_{ch}_{cat}               lnN             -                              1.20                             -   
norm_sig_{ch}_{cat}                     lnN             1.2                            -                                -   
--------------------------------------------------------------------------------------------------------------------------------------------
{cat} autoMCStats 0 0 1
'''.format(cat         = label,
           obs         = int(data.integral()) if self.blinded==False else -1,
           signal_name = isig.name,
           signal      = isig.integral(),
           ch          = self.full_channel,
           prompt      = bkgs['prompt'].integral(),
           nonprompt   = bkgs['nonprompt'].integral(),
           )
        )

        outfile.Close()

    def plot(self):

        evaluator = Evaluator(self.model, self.transformation, self.features)
        self.plt_dir = plot_dir()
        # NN evaluator

        print('============> starting reading the trees')
        print ('Plots will be stored in: ', self.plt_dir)
        now = time()
        signal = []
        if self.process_signals:
            signal = get_signal_samples(self.channel, env['NTUPLE_BASE_DIR'] + '{year}/sig'.format(year=self.year), 'HNLTreeProducer_%s/tree.root'%self.channel, self.selection_data, mini=self.mini_signals, year=self.year)
        else:
            signal = []        

        if self.year != 2018:
            data  = get_data_samples(self.channel, env['NTUPLE_BASE_DIR'] + '{year}/data'.format(year=self.year), 'HNLTreeProducer_%s/tree.root'%self.channel, self.selection_data, self.year)
        if self.year == 2018:
            data  = get_data_samples(self.channel, env['NTUPLE_BASE_DIR'] + '{year}/{ch}18'.format(year=self.year, ch=self.channel), self.post_fix, self.selection_data, self.year)

        mc     = get_mc_samples    (self.channel, env['NTUPLE_BASE_DIR'] + '{year}/mc'.format(year=self.year), 'HNLTreeProducer_%s/tree.root'%self.channel, self.selection_mc, self.year)
        print('============> it took %.2f seconds' %(time() - now))
                 
        dbg = False

        # apply an extra selection to the pandas dataframes
        if len(self.pandas_selection):
            for isample in (mc+data+signal):
                isample.df = isample.df.query(self.pandas_selection)

        # evaluate FR
        for isample in (mc+data): #+signal):
            isample.df['year'] = self.year
            isample.df['fr'] = evaluator.evaluate(isample.df)
            # already corrected, ready to be applied in lnt-not-tight
            isample.df['fr_corr'] = isample.df['fr'] / (1. - isample.df['fr']) 

        # split the dataframe in tight and lnt-not-tight (called simply lnt for short)
        for isample in (mc+data+signal):
            # extra variables
            isample.df['abs_l1_dxy'] = np.abs(isample.df['l1_dxy'])
            isample.df['abs_l2_dxy'] = np.abs(isample.df['l2_dxy'])
            #defining tight/lnt
            isample.df_tight = isample.df.query(self.selection_tight)
            isample.df_lnt   = isample.df.query(self.selection_lnt)

        if self.process_signals and dbg:
            # jmc = signal[1] # =  4 GeV Mass
            # jmc = signal[3] # = 10 GeV Mass
            weights_TEST = self.total_weight_calculator(jmc.df_tight, ['weight', 'lhe_weight']+jmc.extra_signal_weights, [self.lumi, jmc.lumi_scaling])
            weights_onlyLHE_TEST = self.total_weight_calculator(jmc.df_tight, ['lhe_weight']+jmc.extra_signal_weights, [self.lumi, jmc.lumi_scaling])
            check_yields = 0
            check_yields_onlyLHE = 0
            for i in weights_TEST:
                check_yields += i
            for lhi in weights_onlyLHE_TEST:
                check_yields_onlyLHE += lhi
            print (self.year, self.channel, 'events:', jmc.df_tight.shape[0], ' ##  yield =', check_yields, '(all weights)') 
            print (self.lumi, jmc.lumi_scaling, check_yields_onlyLHE, '(only lhe)')
            if dbg == True:
                return 0

        # sort depending on their position in the stack
        mc.sort(key = lambda x : x.position_in_stack)

        # now we plot 
        self.create_canvas(self.do_ratio)
        # create checkpad
        self.create_kanvas()

        for ivar in variables:
            
            variable, bins, label, xlabel, ylabel, extra_sel = ivar.var, ivar.bins, ivar.label, ivar.xlabel, ivar.ylabel, ivar.extra_selection
            
            print('plotting', label)
            
            ######################################################################################
            # plot MC stacks, in tight and lnt
            ######################################################################################
            
            stack_prompt    = []
            stack_nonprompt = []
            stack_nonprompt_check = []
            
            for imc in mc:
                
                if extra_sel:
                    mc_df_tight = imc.df_tight.query(extra_sel) 
                    mc_df_lnt = imc.df_lnt.query(extra_sel) 
                else:
                    mc_df_tight = imc.df_tight
                    mc_df_lnt = imc.df_lnt
                
                histo_tight = Hist(bins, title=imc.label, markersize=0, legendstyle='F', name=imc.datacard_name+'#'+label)

                weights = self.total_weight_calculator(mc_df_tight, ['weight', 'lhe_weight']+imc.extra_signal_weights, [self.lumi, imc.lumi_scaling])
                # print ('WARNING, ONLY LHE WEIGHTS'); weights = self.total_weight_calculator(mc_df_tight, ['lhe_weight']+imc.extra_signal_weights, [self.lumi, imc.lumi_scaling])
                histo_tight.fill_array(mc_df_tight[variable], weights=weights)

                # print ('WARNING, ONLY EVENT NUMBERS, UNSCALED'); histo_tight.fill_array(mc_df_tight[variable])

                histo_tight.fillstyle = 'solid'
                histo_tight.fillcolor = 'steelblue'
                histo_tight.linecolor = 'steelblue'
                histo_tight.linewidth = 0

                stack_prompt.append(histo_tight)

                histo_lnt = Hist(bins, title=imc.label, markersize=0, legendstyle='F')
                histo_lnt_check = Hist(bins, title=imc.label+'check', markersize=0, legendstyle='F')

                weights = self.total_weight_calculator(mc_df_lnt, ['weight', 'lhe_weight', 'fr_corr']+imc.extra_signal_weights, [-1., self.lumi, imc.lumi_scaling])
                # print ('WARNING, ONLY LHE WEIGHTS'); weights = self.total_weight_calculator(mc_df_lnt, ['lhe_weight', 'fr_corr']+imc.extra_signal_weights, [-1., self.lumi, imc.lumi_scaling])
                histo_lnt.fill_array(mc_df_lnt[variable], weights=weights)

                # Sanity check
                weights_noFR = self.total_weight_calculator(mc_df_lnt, ['weight', 'lhe_weight']+imc.extra_signal_weights, [self.lumi, imc.lumi_scaling])
                histo_lnt_check.fill_array(mc_df_lnt[variable], weights=weights_noFR)

                # print ('WARNING, ONLY EVENT NUMBERS, UNSCALED'); histo_lnt.fill_array(mc_df_lnt[variable])

                histo_lnt.fillstyle = 'solid'
                histo_lnt.linecolor = 'skyblue'
                histo_lnt.fillcolor = 'skyblue'
                histo_lnt.linewidth = 0

                histo_lnt_check.fillstyle = 'solid'
                histo_lnt_check.linecolor = 'skyblue'
                histo_lnt_check.fillcolor = 'skyblue'
                histo_lnt_check.linewidth = 0

                stack_nonprompt.append(histo_lnt)
                stack_nonprompt_check.append(histo_lnt_check)

            ######################################################################################
            # plot the signals
            ######################################################################################
            
            all_signals     = []
            signals_to_plot = []
            
            for isig in signal:

                if extra_sel:
                    isig_df_tight = isig.df_tight.query(extra_sel) 
                else:
                    isig_df_tight = isig.df_tight

                histo_tight = Hist(bins, title=isig.label, markersize=0, legendstyle='L', name=isig.datacard_name+'#'+label) # the "#" thing is a trick to give hists unique name, else ROOT complains

                weights = self.total_weight_calculator(isig_df_tight, ['weight', 'lhe_weight']+isig.extra_signal_weights, [self.lumi, isig.lumi_scaling])
                # print ('WARNING, ONLY LHE WEIGHTS'); weights = self.total_weight_calculator(isig_df_tight, ['lhe_weight']+isig.extra_signal_weights, [self.lumi, isig.lumi_scaling])
                histo_tight.fill_array(isig_df_tight[variable], weights=weights)

                # print ('WARNING, ONLY EVENT NUMBERS, UNSCALED'); histo_tight.fill_array(isig_df_tight[variable])

                histo_tight.color     = isig.colour
                histo_tight.fillstyle = 'hollow'
                histo_tight.linewidth = 2
                histo_tight.linestyle = 'dashed'
                histo_tight.drawstyle = 'HIST'

                all_signals.append(histo_tight)
                if isig.toplot: signals_to_plot.append(histo_tight)
            
            ######################################################################################
            # plot the data
            ######################################################################################

            data_prompt    = []
            data_nonprompt = []
            data_nonprompt_check = []
            
            for idata in data:

                if extra_sel:
                    idata_df_tight = idata.df_tight.query(extra_sel) 
                    idata_df_lnt = idata.df_lnt.query(extra_sel) 
                else:
                    idata_df_tight = idata.df_tight
                    idata_df_lnt = idata.df_lnt

                histo_tight = Hist(bins, title=idata.label, markersize=1, legendstyle='LEP')
                histo_tight.fill_array(idata_df_tight[variable])
                
                data_prompt.append(histo_tight)

                histo_lnt = Hist(bins, title=idata.label, markersize=0, legendstyle='F')
                histo_lnt.fill_array(idata_df_lnt[variable], weights=idata_df_lnt.fr_corr)
                
                data_nonprompt.append(histo_lnt)

                # check LNT
                histo_lnt_check = Hist(bins, title=idata.label+'check', markersize=0, legendstyle='F')
                histo_lnt_check.fill_array(idata_df_lnt[variable])
                data_nonprompt_check.append(histo_lnt_check)

                histo_lnt_check.fillstyle = 'solid'
                histo_lnt_check.fillcolor = 'firebrick'
                histo_lnt_check.linecolor = 'firebrick'
                histo_lnt_check.linewidth = 0

            # put the prompt backgrounds together
            all_exp_prompt = sum(stack_prompt)
            all_exp_prompt.title = 'prompt'

            # put the nonprompt backgrounds together
            all_exp_nonprompt = sum(stack_nonprompt+data_nonprompt)
            all_exp_nonprompt.title = 'nonprompt'

            all_exp_nonprompt_mc_check = sum(stack_nonprompt_check)
            all_exp_nonprompt_mc_check.title = 'nonprompt_mc_check'

            # check_stack
            all_exp_nonprompt_data_check = sum(data_nonprompt_check)
            all_exp_nonprompt_data_check.title = 'data_nonprompt_check'

            # all_exp_nonprompt_check = sum(stack_nonprompt_check + data_nonprompt_check)
            # all_exp_nonprompt_check.title = 'all_LNT_check'


            # create the stacks
            stack = HistStack([all_exp_prompt, all_exp_nonprompt], drawstyle='HIST', title='')
            stack_check = HistStack([all_exp_nonprompt_data_check, all_exp_nonprompt_mc_check], drawstyle='HISTE', title='')

            # stat uncertainty
            hist_error = stack.sum #sum([all_exp_prompt, all_exp_nonprompt])    
            hist_error.drawstyle = 'E2'
            hist_error.fillstyle = '/'
            hist_error.color     = 'gray'
            hist_error.title     = 'stat. unc.'
            hist_error.legendstyle = 'F'

            # put the data together
            all_obs_prompt = sum(data_prompt)
            all_obs_prompt.title = 'observed'

            # prepare the legend
            print(signals_to_plot)
            for jj in signals_to_plot: print(jj.name, jj.integral())
            if len(signals_to_plot):
                legend         = Legend([all_obs_prompt, stack, hist_error], pad=self.main_pad, leftmargin=0., rightmargin=0., topmargin=0., textfont=42, textsize=0.025, entrysep=0.01, entryheight=0.04)
                legend_signals = Legend(signals_to_plot                    , pad=self.main_pad, leftmargin=0., rightmargin=0., topmargin=0., textfont=42, textsize=0.025, entrysep=0.01, entryheight=0.04)
                legend_signals.SetBorderSize(0)
                legend_signals.x1 = 0.42
                legend_signals.y1 = 0.74
                legend_signals.x2 = 0.88
                legend_signals.y2 = 0.90
                legend_signals.SetFillColor(0)
                legend.SetBorderSize(0)
                legend.x1 = 0.2
                legend.y1 = 0.74
                legend.x2 = 0.45
                legend.y2 = 0.90
                legend.SetFillColor(0)
            else:
                legend = Legend([all_obs_prompt, stack, hist_error], pad=self.main_pad, leftmargin=0., rightmargin=0., topmargin=0., textfont=42, textsize=0.03, entrysep=0.01, entryheight=0.04)
                legend.SetBorderSize(0)
                legend.x1 = 0.55
                legend.y1 = 0.74
                legend.x2 = 0.88
                legend.y2 = 0.90
                legend.SetFillColor(0)
            

            # plot with ROOT, linear and log scale
            for islogy in [False, True]:

                things_to_plot = [stack, hist_error]
                if not self.blinded: 
                    things_to_plot.append(all_obs_prompt)
                
                # plot signals, as an option
                if self.plot_signals: 
                    things_to_plot += signals_to_plot
                
                # set the y axis range 
                # FIXME! setting it by hand to each object as it doesn't work if passed to draw
                if islogy : yaxis_max = 40.   * max([ithing.max() for ithing in things_to_plot])
                else      : yaxis_max =  1.65 * max([ithing.max() for ithing in things_to_plot])
                if islogy : yaxis_min = 0.01
                else      : yaxis_min = 0.

#                 print('---------------------------> 1', things_to_plot)
#                 for ii in things_to_plot: print(islogy, ii.GetMinimum(), ii.GetMaximum())
                for ithing in things_to_plot:
                    ithing.SetMaximum(yaxis_max)   
                    # ithing.SetMinimum(yaxis_min) # FIXME! this doesn't work                              
                    # stack.yaxis.set_range_user(yaxis_min, yaxis_max)

#                 print('---------------------------> 2', things_to_plot)
#                 for ii in things_to_plot: print(islogy, ii.GetMinimum(), ii.GetMaximum())

                draw(things_to_plot, xtitle=xlabel, ytitle=ylabel, pad=self.main_pad, logy=islogy)

                check_LNT = True
                all_exp_nonprompt_data_check .linewidth = 2
                all_exp_nonprompt_mc_check   .linewidth = 2
                if check_LNT and islogy == False:
                    self.kpad.cd()
                    all_obs_prompt.SetMarkerSize(0)
                    all_obs_prompt.SetTitle('%s; %s; %s' %(label, xlabel, ylabel))
                    stack_check.SetTitle('%s; %s; %s' %(label, xlabel, ylabel))
                    stack_check.Draw('histe')
                    all_obs_prompt.Draw('histesame')
                    legend_check = Legend([all_obs_prompt, stack_check], pad=self.kpad, leftmargin=0., rightmargin=0., topmargin=0., textfont=42, textsize=0.02, entrysep=0.01, entryheight=0.03)
                    legend_check.SetBorderSize(0)
                    legend_check.x1 = 0.35
                    legend_check.y1 = 0.69
                    legend_check.x2 = 0.68
                    legend_check.y2 = 0.82
                    legend_check.SetFillColor(0)
                    self.kanvas.cd()
                    legend_check.Draw('same')
                    self.kpad.cd()
                    stack_check.Draw('histesame')
                    all_obs_prompt.Draw('histesame')

                self.main_pad.cd()
                # TODO instead do hist.DrawNormalized('ep'), 'epsame'  ... 
                # draw(all_exp_nonprompt, xtitle=xlabel, ytitle=ylabel, pad=self.kpad, logy=islogy)
                
                # update the stack yaxis range *after* is drawn. 
                # It will be picked up by canvas.Update()
#                 stack.yaxis.set_range_user(yaxis_min, yaxis_max)
                
#                 print('---------------------------> 3', things_to_plot)
#                 for ii in things_to_plot: print(islogy, ii.GetMinimum(), ii.GetMaximum())
#                 import pdb ; pdb.set_trace()
                
                # expectation uncertainty in the ratio pad
                ratio_exp_error = Hist(bins)
                ratio_data = Hist(bins)
                for ibin in hist_error.bins_range():
                    ratio_exp_error.set_bin_content(ibin, 1.)
                    ratio_exp_error.set_bin_error  (ibin, hist_error.get_bin_error(ibin)      / hist_error.get_bin_content(ibin) if hist_error.get_bin_content(ibin)!=0. else 0.)
                    ratio_data.set_bin_content     (ibin, all_obs_prompt.get_bin_content(ibin)/ hist_error.get_bin_content(ibin) if hist_error.get_bin_content(ibin)!=0. else 0.)
                    ratio_data.set_bin_error       (ibin, all_obs_prompt.get_bin_error(ibin)  / hist_error.get_bin_content(ibin) if hist_error.get_bin_content(ibin)!=0. else 0.)

                ratio_data.drawstyle = 'EP'
                ratio_data.title     = ''

                ratio_exp_error.drawstyle  = 'E2'
                ratio_exp_error.markersize = 0
                ratio_exp_error.title      = ''
                ratio_exp_error.fillstyle  = '/'
                ratio_exp_error.color      = 'gray'

                for ithing in [ratio_data, ratio_exp_error]:
                    if ivar.set_log_x:
                        ithing.xaxis.set_no_exponent()
                        ithing.xaxis.set_more_log_labels()
                    ithing.xaxis.set_label_size(ithing.xaxis.get_label_size() * 3.) # the scale should match that of the main/ratio pad size ratio
                    ithing.yaxis.set_label_size(ithing.yaxis.get_label_size() * 3.) # the scale should match that of the main/ratio pad size ratio
                    ithing.xaxis.set_title_size(ithing.xaxis.get_title_size() * 3.) # the scale should match that of the main/ratio pad size ratio
                    ithing.yaxis.set_title_size(ithing.yaxis.get_title_size() * 3.) # the scale should match that of the main/ratio pad size ratio
                    ithing.yaxis.set_ndivisions(405)
                    ithing.yaxis.set_title_offset(0.4)
                    
                things_to_plot = [ratio_exp_error]
                if not self.blinded: 
                    things_to_plot.append(ratio_data)

                draw(things_to_plot, xtitle=xlabel, ytitle='obs/exp', pad=self.ratio_pad, logy=False, ylimits=(0.5, 1.5))

                line = ROOT.TLine(min(bins), 1., max(bins), 1.)
                line.SetLineColor(ROOT.kBlack)
                line.SetLineWidth(1)
                self.ratio_pad.cd()
                line.Draw('same')

                for can in [self.canvas, self.kanvas]:
                    can.cd()
                    if   self.full_channel == 'mmm': channel = '\mu\mu\mu'
                    elif self.full_channel == 'eee': channel = 'eee'
                    elif self.full_channel == 'mem_os': channel = '\mu^{\pm}\mu^{\mp}e'
                    elif self.full_channel == 'mem_ss': channel = '\mu^{\pm}\mu^{\pm}e'
                    elif self.full_channel == 'eem_os': channel = 'e^{\pm}e^{\mp}\mu'
                    elif self.full_channel == 'eem_ss': channel = 'e^{\pm}e^{\pm}\mu'
                    else: assert False, 'ERROR: Channel not valid.'
                    finalstate = ROOT.TLatex(0.68, 0.68, channel)
                    finalstate.SetTextFont(43)
                    finalstate.SetTextSize(25)
                    finalstate.SetNDC()
                    finalstate.Draw('same')
                
                self.canvas.cd()
                legend.Draw('same')
                if self.plot_signals: 
                    legend_signals.Draw('same')
                if self.year == 2016:
                    lumi_text = "2016, L = 35.87 fb^{-1}"
                elif self.year == 2017:
                    lumi_text = "2017, L = 41.53 fb^{-1}"
                elif self.year == 2018:
                    lumi_text = "2018, L = 59.74 fb^{-1}"
                CMS_lumi(self.main_pad, 4, 0, lumi_13TeV = lumi_text)
                # CMS_lumi(self.kpad, 4, 0, lumi_13TeV = lumi_text)
                if ivar.set_log_x: 
                    self.main_pad .SetLogx() 
                    self.kpad .SetLogx() 
                    self.ratio_pad.SetLogx() 
                self.canvas.Modified();  self.canvas.Update()
                self.canvas.SaveAs(self.plt_dir + '%s%s.pdf' %(label, '_log' if islogy else '_lin'))
                if check_LNT and islogy == False:
                    self.kanvas.Modified();  self.kanvas.Update()
                    self.kanvas.SaveAs(self.plt_dir + '%s%s_check_LNT-T.pdf' %(label, '_log' if islogy else '_lin'))

            # save only the datacards you want, don't flood everything
            if len(self.datacards) and label not in self.datacards:
                continue
                
            self.create_datacards(data=all_obs_prompt, 
                                  bkgs={'prompt':all_exp_prompt, 'nonprompt':all_exp_nonprompt}, 
                                  signals=all_signals, 
                                  label=label)  
