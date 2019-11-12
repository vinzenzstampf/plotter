import re
import time
import ROOT as rt
# import uproot
# import rootpy
# import root_pandas
# from rootpy.plotting import Hist
import numpy as np
import pandas as pd
# from rootpy.plotting import Hist
# from root_numpy import root2array
from collections import OrderedDict
import sklearn
from selections import selections, selections_df
from evaluate_nn import Evaluator
from sample import Sample
from variables import variables
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from pdb import set_trace

# basedir        = '/Users/manzoni/Documents/efficiencyNN/HNL/mmm/ntuples/'
basedir        = '/Users/cesareborgia/cernbox/2018_new/mmm/'
postfix        = 'HNLTreeProducer/tree.root'
lumi           = 59700. # fb-1
selection_data = selections['baseline']
# selection_mc   = selections['baseline'] 
selection_mc   = '&'.join([selections['baseline'], selections['ispromptlepton']])

# NN evaluator
model          = 'net_model_weighted.h5'
transformation = 'input_tranformation_weighted.pck'
features       = 'input_features.pck'
evaluator      = Evaluator(model, transformation, features)

@rt.DeclareCppCallable(["float"] * len(evaluator.features), "float") # does this init work?!
def evaluate_RDF(*arg):
    return evaluator.eval_rdf(arg) 

print '============> starting reading the trees'
now = time.time()
                   
data = [
    Sample('Single_mu_2018A', '2018A', selection_data, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
    # Sample('Single_mu_2018B', '2018B', selection_data, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
    # Sample('Single_mu_2018C', '2018C', selection_data, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
    # Sample('Single_mu_2018D', '2018D', selection_data, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
]

mc = [
    Sample('DYJetsToLL_M50_ext', r'DY$\to\ell\ell$', selection_mc, 'DY', 'gold'     ,10, basedir, postfix, False, True, False, 1.,  6077.22),
    # Sample('TTJets_ext'        , r'$t\bar{t}$'     , selection_mc, 'TT', 'slateblue', 0, basedir, postfix, False, True, False, 1.,   831.76),
    # Sample('WW'                , 'WW'              , selection_mc, 'WW', 'blue'     , 5, basedir, postfix, False, True, False, 1.,    75.88),
    # Sample('WZ'                , 'WZ'              , selection_mc, 'WZ', 'blue'     , 5, basedir, postfix, False, True, False, 1.,    27.6 ),
    # Sample('ZZ'                , 'ZZ'              , selection_mc, 'ZZ', 'blue'     , 5, basedir, postfix, False, True, False, 1.,    12.14),
]            

signal = [
]

print '============> it took %.2f seconds' %(time.time() - now)

# evaluate FR

# prepare inputs for cpp-callable in RDataFrame
in_list = ', '.join(evaluator.features)
# print 'in_list: ', in_list

for isample in (data+mc+signal): # WHY SIGNAL HERE?!

    isample.df = isample.df.Define('log_abs_l0_dz' , 'log(abs(l0_dz ))')
    isample.df = isample.df.Define('log_abs_l1_dxy', 'log(abs(l1_dxy))')
    isample.df = isample.df.Define('log_abs_l1_dz' , 'log(abs(l1_dz ))')
    isample.df = isample.df.Define('log_abs_l2_dxy', 'log(abs(l2_dxy))')
    isample.df = isample.df.Define('log_abs_l2_dz' , 'log(abs(l2_dz ))')

    isample.df = isample.df.Define('abs_l0_eta', 'abs(l0_eta)')
    isample.df = isample.df.Define('abs_l1_eta', 'abs(l1_eta)')
    isample.df = isample.df.Define('abs_l2_eta', 'abs(l2_eta)')

    isample.df = isample.df.Define('fr', 'CppCallable::evaluate_RDF( ' + in_list + ' )')
    isample.df = isample.df.Define('fr_corr', 'fr / (1. - fr)')

# split the dataframe in tight and loose-not-tight (called simply loose for short)
for isample in (mc+data):
    isample.df_tight = isample.df.Filter(selections_df['tight'])
    isample.df_lnt   = isample.df.Filter('! ( ' + selections_df['tight'] + ' )')
    if isample in mc:
        isample.df_tight = isample.df_tight.Define('evt_wht_tight', str(lumi) + ' * ' + str(isample.lumi_scaling) + ' * weight *  lhe_weight')
        isample.df_lnt   = isample.df_lnt  .Define('evt_wht_lnt',   str(lumi) + ' * ' + str(isample.lumi_scaling) + ' * weight *  lhe_weight * -1 * fr_corr')

# sort depending on their position in the stack
mc.sort(key = lambda x : x.position_in_stack)

can = rt.TCanvas()

for variable, bins, xlabel, ylabel in variables:
    
    print 'plotting', variable

    # plot MC stack in tight
    hists_tight = OrderedDict()
    hists_lnt = OrderedDict()

    for imc in mc: 
        hist_t = None;   hist_lnt = None
        hist_t   = imc.df_tight.Histo1D( ('h_tight_'+variable+'_'+imc.name, 'h_tight_'+variable+'_'+imc.name, len(bins)-1, bins), variable, 'evt_wht_tight')
        hist_lnt = imc.df_lnt  .Histo1D( ('h_lnt_'+variable+'_'+imc.name,   'h_lnt_'+variable+'_'+imc.name,   len(bins)-1, bins), variable, 'evt_wht_lnt')
        hist_t = hist_t.GetPtr();   hist_lnt = hist_lnt.GetPtr()
        hists_tight[imc.name] = hist_t
        hists_lnt  [imc.name] = hist_lnt
        print imc.name + ' drawn'

    for idt in data: 
        hist_t = None;   hist_lnt = None
        hist_t   = idt.df_tight.Histo1D( ('h_tight_'+variable+'_'+idt.name, 'h_tight_'+variable+'_'+idt.name, len(bins)-1, bins), variable)
        hist_lnt = idt.df_lnt  .Histo1D( ('h_lnt_'+variable+'_'+idt.name,   'h_lnt_'+variable+'_'+idt.name,   len(bins)-1, bins), variable, 'fr_corr')
        hist_t = hist_t.GetPtr();   hist_lnt = hist_lnt.GetPtr()
        hists_tight[idt.name] = hist_t
        hists_lnt  [idt.name] = hist_lnt
        print idt.name + ' drawn'

    stack = rt.THStack('stack', 'stack')
    for k in hists_tight.keys(): 
        if '2018' in k: continue
        stack.Add(hists_tight[k])
        print k + ' tight added to stack'
    for k in hists_lnt.keys():
        stack.Add(hists_lnt[k])
        print k + ' lnt added to stack'

    h_data = rt.TH1D()
    for k in hists_tight.keys():
        if not '2018' in k: continue
        h_data.Add(hists_tight[k])
    
    # set_trace()
    
    can.cd()
    stack.Draw('histE')
    h_data.Draw('same')
    can.Modified(); can.Update()
    can.SaveAs(variable + '.pdf')
    can.SaveAs(variable + '.root')
    can.SaveAs(variable + '.png')

    # outfile = rt.TFile.Open('datacard_%s.root' %variable, 'recreate')
    # outfile.cd()
    # h_data = Hist(bins, name='data_obs')
    # h_data.fill_array(df_data[variable])
    # h_data.Write()
    # for imc in mc:
        # h_mc = Hist(bins, name=imc.datacard_name)
        # h_mc.fill_array(imc.df[variable], imc.df.weight * imc.df.lumi_scaling * imc.df.lhe_weight)
        # h_mc.Write()
    # outfile.Close()
