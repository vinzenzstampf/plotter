from collections import OrderedDict
from glob import glob
import ROOT as rt
from pdb import set_trace
from rootpy.plotting import Hist, HistStack, Canvas, Pad, Legend
from rootpy.plotting.utils import draw
import numpy as np
from plotter.cmsstyle import CMS_lumi

# f_in  ='/Users/cesareborgia/cernbox/hnl/2018/sig/HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO/HNLTreeProducer_mmm/tree.root'
# tf = rt.TFile(f_in)
# t = tf.Get('tree')

out_dir = '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/'

rt.gStyle.SetOptStat(0)

years = ['2016', '2017', '2018']
chs = ['mmm', 'mem_os', 'mem_ss', 'eee', 'eem_os', 'eem_ss']
disps = ['lt_0p5', '0p5_to_1p5','1p5_to_4p0', 'mt_4p0']
bins = ['lo', 'hi']

data  = 'data_obs' 
prmp  = 'prompt' 
nonp  = 'nonprompt'
sig8  = 'hnl_m_8_v2_2p3Em06_majorana'
sig10 = 'hnl_m_10_v2_5p7Em07_majorana'
sigs  = [sig8, sig10]

folders = []

# '''# 26Mar20 #'''
# R = 'MRtrain_train_w_dispSig_WO_sbtr_plot_WO_sbtr_w_dispSig'
# folders = glob('/Users/cesareborgia/Dropbox/documents/physics/phd/plots/*/*/200326_*_MRtrain_train_w_dispSig_WO_sbtr_plot_WO_sbtr_w_dispSig/datacards/')

# '''# 26Mar20 #'''
# R = 'MR_train_WO_sbtr_w_dispSig_plot_WO_sbtr_w_dispSig'
# folders = glob('/Users/cesareborgia/Dropbox/documents/physics/phd/plots/*/*/200326_*_MR_train_WO_sbtr_w_dispSig_plot_WO_sbtr_w_dispSig/datacards/')

# '''# 25Mar20 #'''
# R = 'MR_train_w_sbtr_WO_dispSig_plot_WO_sbtr_w_dispSig' # is really with disp sig for plotting, this is checked 
# folders = glob('/Users/cesareborgia/Dropbox/documents/physics/phd/plots/*/*/200325_*_MR_train_w_sbtr_plot_WO_sbtr/datacards/')

'''# 25Mar20 #'''
R = 'MRtrain_train_w_sbtr_WO_dispSig_plot_w_sbtr_WO_dispSig'
folders = glob('/Users/cesareborgia/Dropbox/documents/physics/phd/plots/*/*/200325_*_training_MR/datacards/')

# '''# 24Mar20 #'''
# R = 'MR_with_disp_sig_24Mar20'
# folders = [
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/mmm/200324_13h_9m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/mem_os/200324_13h_15m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/mem_ss/200324_13h_25m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/eee/200324_13h_47m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/eem_os/200324_13h_34m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/eem_ss/200324_13h_40m/datacards/',

# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/mmm/200324_13h_11m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/mem_os/200324_13h_18m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/mem_ss/200324_13h_28m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/eee/200324_13h_49m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/eem_os/200324_13h_36m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/eem_ss/200324_13h_42m/datacards/',

# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/mmm/200324_13h_13m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/mem_os/200324_13h_22m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/mem_ss/200324_13h_31m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/eee/200324_13h_52m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/eem_os/200324_13h_38m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/eem_ss/200324_13h_45m/datacards/',]

# '''# 24Mar20 #'''
# R = 'MR_WO_disp_sig_24Mar20'
# folders = [
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/mmm/200324_12h_4m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/mem_os/200324_12h_11m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/mem_ss/200324_12h_20m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/eee/200324_12h_50m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/eem_os/200324_12h_31m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2016/eem_ss/200324_12h_41m/datacards/',

# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/mmm/200324_12h_6m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/mem_os/200324_12h_14m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/mem_ss/200324_12h_23m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/eee/200324_12h_52m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/eem_os/200324_12h_35m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2017/eem_ss/200324_12h_44m/datacards/',

# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/mmm/200324_12h_9m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/mem_os/200324_12h_17m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/mem_ss/200324_12h_28m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/eee/200324_12h_55m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/eem_os/200324_12h_38m/datacards/',
# '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/2018/eem_ss/200324_12h_47m/datacards/',]

# R = 'CR_MRloose_no_svProb'
# folders = ['/Users/cesareborgia/cernbox/plots/plotter/2016/mmm/200310_13h_57m_CR_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/mem_os/200310_14h_6m_CR_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/mem_ss/200310_14h_20m_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/eem_os/200310_14h_35m_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/eem_ss/200310_14h_47m_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/eee/200310_14h_58m_MRloose_no_svProb/datacards/',

           # '/Users/cesareborgia/cernbox/plots/plotter/2017/mmm/200310_13h_59m_CR_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/mem_os/200310_14h_10m_CR_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/mem_ss/200310_14h_25m_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/eem_os/200310_14h_39m_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/eem_ss/200310_14h_51m_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/eee/200310_15h_2m_MRloose_no_svProb/datacards/',

           # '/Users/cesareborgia/cernbox/plots/plotter/2018/mmm/200310_14h_2m_CR_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/mem_os/200310_14h_15m_CR_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/mem_ss/200310_14h_31m_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/eem_os/200310_14h_42m_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/eem_ss/200310_14h_55m_MRloose_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/eee/200310_15h_6m_MRloose_no_svProb/datacards/',
           # ]

# R = 'CR_bj_no_svProb'
# folders = ['/Users/cesareborgia/cernbox/plots/plotter/2016/mem_ss/200310_14h_4m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/mem_os/200310_13h_50m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/mmm/200310_13h_44m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/eem_os/200310_14h_19m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/eem_ss/200310_14h_30m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2016/eee/200310_14h_41m_CR_bj_no_svProb/datacards/',

           # '/Users/cesareborgia/cernbox/plots/plotter/2017/mmm/200310_13h_46m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/mem_os/200310_13h_54m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/mem_ss/200310_14h_9m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/eem_os/200310_14h_22m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/eem_ss/200310_14h_34m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2017/eee/200310_14h_47m_CR_bj_no_svProb/datacards/',

           # '/Users/cesareborgia/cernbox/plots/plotter/2018/mmm/200310_13h_48m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/mem_os/200310_13h_58m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/mem_ss/200310_14h_14m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/eem_os/200310_14h_26m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/eem_ss/200310_14h_38m_CR_bj_no_svProb/datacards/',
           # '/Users/cesareborgia/cernbox/plots/plotter/2018/eee/200310_14h_52m_CR_bj_no_svProb/datacards/',
           # ]

# '''# 25Feb20 #'''
# R = 'MR_with_disp_sig' # 
# folders = glob('/Users/cesareborgia/cernbox/plots/plotter/2018/*/200225_16h_*/datacards/')   # 2018 WITH disp_sig
# folders += glob('/Users/cesareborgia/cernbox/plots/plotter/2017/*/200225_15h_*/datacards/')  # 2017 WITH disp_sig (training: /all_channels_200213_15h_24m/)
# folders += glob('/Users/cesareborgia/cernbox/plots/plotter/2016/*/200225_16h_7m/datacards/') # 2016 WITH disp_sig
# folders += glob('/Users/cesareborgia/cernbox/plots/plotter/2016/*/200225_16h_8m/datacards/')  # 2016 WITH disp_sig
# folders += glob('/Users/cesareborgia/cernbox/plots/plotter/2016/*/200225_16h_1*/datacards/')  # 2016 WITH disp_sig

# '''# 25Feb20 #'''
# R = 'MR_WO_disp_sig'  
# folders  = glob('/Users/cesareborgia/cernbox/plots/plotter/2018/*/200225_15h_*/datacards/')  # 2018 W/O disp_sig
# folders += glob('/Users/cesareborgia/cernbox/plots/plotter/2017/*/200225_14h_*/datacards/')  # 2017 W/O disp_sig
# folders += glob('/Users/cesareborgia/cernbox/plots/plotter/2016/*/200225_16h_2*/datacards/') # 2016 W/O disp_sig
# folders += glob('/Users/cesareborgia/cernbox/plots/plotter/2016/*/200225_16h_3*/datacards/') # 2016 W/O disp_sig

signal = None
if 'CR' in R or 'MR' in R:
    signal = False
if 'SR' in R:
    signal = True
assert signal != None, 'signal not defined'

files = OrderedDict()

for f in folders:
    f_yr = f.split('/')[-5]
    f_ch = f.split('/')[-4]
    if 'txt' in f: f = f.replace(f.split('/')[-1],'')
    try: files[f_yr][f_ch] = f
    except: 
        files[f_yr] = OrderedDict()
        files[f_yr][f_ch] = f

yields = OrderedDict()
yields_err = OrderedDict()

for yr in years:
    yields[yr] = OrderedDict()
    yields_err[yr] = OrderedDict()
    for ch in chs:    
        yields[yr][ch] = OrderedDict()
        yields_err[yr][ch] = OrderedDict()
        for disp in disps: 
            yields[yr][ch][disp] = OrderedDict()
            yields_err[yr][ch][disp] = OrderedDict()
            for sig in sigs:  
                yields[yr][ch][disp][sig] = OrderedDict()
                yields_err[yr][ch][disp][sig] = OrderedDict()


for yr in files.keys():
    for ch in files[yr].keys():
        f_in = OrderedDict()
        for disp in disps:
            f_in[disp]  = rt.TFile(files[yr][ch] + 'datacard_hnl_m_12_lxy_{disp}.root'.format(disp = disp))
            for sig in sigs:
                # if ch[0] == 'm' and '2p3' in sig: continue #muon channels don't have the m=8,v2=2.3e-6 signal
                h_sig  = f_in[disp].Get(sig)
                h_nonp = f_in[disp].Get(nonp)
                h_prmp = f_in[disp].Get(prmp)
                h_data = f_in[disp].Get(data)

                if signal:
                    try: h_sig.GetBinContent(1)
                    except: 
                        continue
                        set_trace()

                yields[yr][ch][disp][sig] = OrderedDict()
                yields_err[yr][ch][disp][sig] = OrderedDict()
                yields[yr][ch][disp][data] = OrderedDict()
                yields_err[yr][ch][disp][data] = OrderedDict()
                yields[yr][ch][disp][nonp] = OrderedDict()
                yields_err[yr][ch][disp][nonp] = OrderedDict()
                yields[yr][ch][disp][prmp] = OrderedDict()
                yields_err[yr][ch][disp][prmp] = OrderedDict()
                
                if signal:
                    yields[yr][ch][disp][sig]['lo']  = h_sig.GetBinContent(1)
                    yields[yr][ch][disp][sig]['hi']  = h_sig.GetBinContent(2)
                    yields_err[yr][ch][disp][sig]['lo']  = h_sig.GetBinError(1)
                    yields_err[yr][ch][disp][sig]['hi']  = h_sig.GetBinError(2)

                if not signal:
                    yields[yr][ch][disp][data]['lo']  = h_data.GetBinContent(1)
                    yields[yr][ch][disp][data]['hi']  = h_data.GetBinContent(2)
                    yields_err[yr][ch][disp][data]['lo']  = h_data.GetBinError(1)
                    yields_err[yr][ch][disp][data]['hi']  = h_data.GetBinError(2)
                
                yields[yr][ch][disp][nonp]['lo'] = h_nonp.GetBinContent(1)
                yields[yr][ch][disp][nonp]['hi'] = h_nonp.GetBinContent(2)
                yields_err[yr][ch][disp][nonp]['lo']  = h_nonp.GetBinError(1)
                yields_err[yr][ch][disp][nonp]['hi']  = h_nonp.GetBinError(2)
                
                yields[yr][ch][disp][prmp]['lo'] = h_prmp.GetBinContent(1)
                yields[yr][ch][disp][prmp]['hi'] = h_prmp.GetBinContent(2)
                yields_err[yr][ch][disp][prmp]['lo']  = h_prmp.GetBinError(1)
                yields_err[yr][ch][disp][prmp]['hi']  = h_prmp.GetBinError(2)

bins = np.arange(0.,25,1)

# fill data: xxx:lo,hi; xxy_os:lo,hi; xxy_ss:lo,hi
# SetBinX start with 1! (0 is underflow)
for yr in years:

    h_data = Hist(bins, title='data', markersize=1, legendstyle='LEP', name='data')
    h_nonp = Hist(bins, title='non-prompt', markersize=0, legendstyle='F',   name='non-prompt')
    h_prmp = Hist(bins, title='prompt', markersize=0, legendstyle='F',   name='prompt')

    h_prmp.fillstyle = 'solid'
    h_prmp.fillcolor = 'steelblue'
    h_prmp.linecolor = 'steelblue'
    h_prmp.linewidth = 0

    h_nonp.fillstyle = 'solid'
    h_nonp.fillcolor = 'skyblue'
    h_nonp.linecolor = 'skyblue'
    h_nonp.linewidth = 0
   
    for l0 in ['e','mu']:
        if l0 == 'e':  chs = ['eee', 'eem_os', 'eem_ss']
        if l0 == 'mu': chs = ['mmm', 'mem_os', 'mem_ss']
        i = 0
        for ch in chs:
            for m_bin in ['lo','hi']:
                for disp in disps:
                    h_data.SetBinContent(i+1, yields[yr][ch][disp][data][m_bin])
                    h_prmp.SetBinContent(i+1, yields[yr][ch][disp][prmp][m_bin])
                    h_nonp.SetBinContent(i+1, yields[yr][ch][disp][nonp][m_bin])

                    h_data.SetBinError(i+1, yields_err[yr][ch][disp][data][m_bin])
                    h_prmp.SetBinError(i+1, yields_err[yr][ch][disp][prmp][m_bin])
                    h_nonp.SetBinError(i+1, yields_err[yr][ch][disp][nonp][m_bin])
                    
                    i+=1

        stack = HistStack([h_nonp, h_prmp], drawstyle='HIST', title='')

        labels =  ['0-0.5','0.5-1.5','1.5-4','>4','0-0.5','0.5-1.5','1.5-4','>4',
                   '0-0.5','0.5-1.5','1.5-4','>4','0-0.5','0.5-1.5','1.5-4','>4',
                   '0-0.5','0.5-1.5','1.5-4','>4','0-0.5','0.5-1.5','1.5-4','>4']

        hist_error = stack.sum #sum([all_exp_prompt, all_exp_nonprompt])    
        hist_error.drawstyle = 'E2'
        hist_error.fillstyle = '/'
        hist_error.color     = 'gray'
        hist_error.title     = 'stat. unc.'
        hist_error.legendstyle = 'F'

        ratio_exp_error = Hist(bins)
        ratio_data = Hist(bins)
        for ibin in hist_error.bins_range():
            ratio_exp_error.set_bin_content(ibin, 1.)
            ratio_exp_error.set_bin_error  (ibin, hist_error.get_bin_error(ibin) / hist_error.get_bin_content(ibin) if hist_error.get_bin_content(ibin)!=0. else 0.)
            ratio_data.set_bin_content     (ibin, h_data.get_bin_content(ibin) / hist_error.get_bin_content(ibin) if hist_error.get_bin_content(ibin)!=0. else 0.)
            ratio_data.set_bin_error       (ibin, h_data.get_bin_error(ibin) / hist_error.get_bin_content(ibin) if hist_error.get_bin_content(ibin)!=0. else 0.)

        ratio_data.drawstyle = 'EP'
        ratio_data.title     = ''

        ratio_exp_error.drawstyle  = 'E2'
        ratio_exp_error.markersize = 0
        ratio_exp_error.title      = ''
        ratio_exp_error.fillstyle  = '/'
        ratio_exp_error.color      = 'gray'

        can = Canvas(width=700,height=700)

        can.cd(); pad_plt = Pad(0.,0.25,1.,1.); pad_plt.Draw()
        can.cd(); pad_tio = Pad(0.,0.,1.,0.25); pad_tio.Draw()

        pad_plt.SetTicks(True)
        pad_plt.SetBottomMargin(0.)
        pad_plt.SetLeftMargin(0.15)
        pad_plt.SetRightMargin(0.15)

        pad_tio.SetLeftMargin(0.15)
        pad_tio.SetRightMargin(0.15)
        pad_tio.SetTopMargin(0.)   
        pad_tio.SetGridy()
        pad_tio.SetBottomMargin(0.3)

        h_data.GetXaxis().LabelsOption('h')
        h_data.GetXaxis().SetTitle ('#Delta (PV-SV)_2D (cm)')
        h_data.GetXaxis().SetTitleSize(0.06)
        h_data.GetXaxis().SetTitleOffset(1.1)
        h_data.GetXaxis().SetTitleFont(132)

# bin labels
        for i, lbl in enumerate(labels):
            h_data.GetXaxis().SetBinLabel(i+1, lbl)

        things_to_plot = [stack, h_data, hist_error]

        yaxis_max =  1.45 * max([ithing.max() for ithing in things_to_plot])

        for ithing in things_to_plot:
            ithing.SetMaximum(yaxis_max)   

        draw(things_to_plot, xtitle='', ytitle='Counts', pad=pad_plt, logy=False)

        high_flav = yaxis_max / 1.125
        high_mll = high_flav * 0.85
        left_mll = 0.97
          
        pad_plt.cd()

        line0 = rt.TLine(8, 0, 8, high_flav)
        line0.SetLineWidth(2)
        line0.Draw('same')

        line1 = rt.TLine(16, 0, 16, high_flav)
        line1.SetLineWidth(2)
        line1.Draw('same')

        line2 = rt.TLine(4, high_mll*1.025, 4, 0.1)
        line2.SetLineStyle(2)
        line2.SetLineWidth(1)
        line2.Draw('same')

        line3 = rt.TLine(12, high_mll*1.025, 12, 0.1)
        line3.SetLineStyle(2)
        line3.SetLineWidth(1)
        line3.Draw('same')

        line4 = rt.TLine(20, high_mll*1.025, 20, 0.1)
        line4.SetLineStyle(2)
        line4.SetLineWidth(1)
        line4.Draw('same')

        tex0 = rt.TLatex(0.8748578,17546.74,'')
        tex0 = rt.TLatex(left_mll, high_mll, 'M_{ll} < 4 GeV')
        tex0.SetTextSize(0.02)
        tex0.SetTextFont(42)
        tex0.SetLineWidth(2)
        tex0.Draw('same')

        tex1 = rt.TLatex(left_mll+4, high_mll, 'M_{ll} > 4 GeV')
        tex1.SetTextSize(0.02)
        tex1.SetTextFont(42)
        tex1.SetLineWidth(2)
        tex1.Draw('same')

        tex2 = rt.TLatex(left_mll+8, high_mll, 'M_{ll} < 4 GeV')
        tex2.SetTextSize(0.02)
        tex2.SetTextFont(42)
        tex2.SetLineWidth(2)
        tex2.Draw('same')

        tex2 = rt.TLatex(left_mll+12, high_mll, 'M_{ll} > 4 GeV')
        tex2.SetTextSize(0.02)
        tex2.SetTextFont(42)
        tex2.SetLineWidth(2)
        tex2.Draw('same')

        tex3 = rt.TLatex(left_mll+16, high_mll, 'M_{ll} < 4 GeV')
        tex3.SetTextSize(0.02)
        tex3.SetTextFont(42)
        tex3.SetLineWidth(2)
        tex3.Draw('same')

        tex4 = rt.TLatex(left_mll+20, high_mll, 'M_{ll} > 4 GeV')
        tex4.SetTextSize(0.02)
        tex4.SetTextFont(42)
        tex4.SetLineWidth(2)
        tex4.Draw('same')

        mmm    = '\mu\mu\mu'
        eee    = 'eee'
        mem_os = '\mu^{\pm}\mu^{\mp}e'
        mem_ss = '\mu^{\pm}\mu^{\pm}e'
        eem_os = 'e^{\pm}e^{\mp}\mu'
        eem_ss = 'e^{\pm}e^{\pm}\mu'

        if l0 == 'e':
            state0 = eee; state1 = eem_os; state2 = eem_ss
        if l0 == 'mu':
            state0 = mmm; state1 = mem_os; state2 = mem_ss

        state_0 = rt.TLatex(left_mll+2.05,  high_flav*.925, state0)
        state_0.SetTextFont(43)
        state_0.SetTextSize(25)
        state_0.Draw('same')

        state_1 = rt.TLatex(left_mll+9.5,  high_flav*.925, state1)
        state_1.SetTextFont(43)
        state_1.SetTextSize(25)
        state_1.Draw('same')

        state_2 = rt.TLatex(left_mll+17.5, high_flav*.925, state2)
        state_2.SetTextFont(43)
        state_2.SetTextSize(25)
        state_2.Draw('same')

        year = int(yr)
        if year == 2016:
            lumi_text = "2016, L = 35.87 fb^{-1}"
        elif year == 2017:
            lumi_text = "2017, L = 41.53 fb^{-1}"
        elif year == 2018:
            lumi_text = "2018, L = 59.74 fb^{-1}"
        CMS_lumi(pad_plt, 4, 0, lumi_13TeV = lumi_text)

        legend = Legend([h_data, stack, hist_error], pad=pad_plt, leftmargin=0., rightmargin=0., topmargin=0., textfont=42, textsize=0.03, entrysep=0.01, entryheight=0.04)
        legend.SetBorderSize(0)
        legend.x1 = 0.25
        legend.y1 = 0.8
        legend.x2 = 0.85
        legend.y2 = 0.85
        legend.SetFillColor(0)
        legend.SetNColumns(4)
        legend.Draw('same')

        for ithing in [ratio_data, ratio_exp_error]:
            ithing.xaxis.set_label_size(ithing.xaxis.get_label_size() * 3.) # the scale should match that of the main/ratio pad size ratio
            ithing.yaxis.set_label_size(ithing.yaxis.get_label_size() * 3.) # the scale should match that of the main/ratio pad size ratio
            ithing.xaxis.set_title_size(ithing.xaxis.get_title_size() * 3.) # the scale should match that of the main/ratio pad size ratio
            ithing.yaxis.set_title_size(ithing.yaxis.get_title_size() * 3.) # the scale should match that of the main/ratio pad size ratio
            ithing.yaxis.set_ndivisions(405)
            ithing.yaxis.set_title_offset(0.4)
            # ithing.GetXaxis().LabelsOption('vu')
            ithing.GetXaxis().LabelsOption('h')

            for i, lbl in enumerate(labels):
                ithing.GetXaxis().SetBinLabel(i+1, lbl)

        draw([ratio_data, ratio_exp_error], xtitle='#Delta_{2D}(PV, SV) (cm)', ytitle='obs/exp', pad=pad_tio, logy=False, ylimits=(0.5, 1.5))

        line = rt.TLine(min(bins), 1., max(bins), 1.)
        line.SetLineColor(rt.kBlack)
        line.SetLineWidth(1)
        pad_tio.cd()
        line.Draw('same')

        can.Modified(); can.Update()
        can.SaveAs(out_dir + 'all_%s_ch_%s_%s.pdf'  %(l0, yr, R))
        can.SaveAs(out_dir + 'all_%s_ch_%s_%s.root' %(l0, yr, R))


'''
## 2016 ##
mmm
- mmm/200306_15h_8m_CR_bj_with_svProb0p001
- mmm/200310_13h_44m_CR_bj_no_svProb
- mmm/200310_13h_57m_CR_MRloose_no_svProb
mem_os
- mem_os/200306_15h_13m_CR_bj_with_svProb0p001
- mem_os/200310_13h_50m_CR_bj_no_svProb
- mem_os/200310_14h_6m_CR_MRloose_no_svProb
mem_ss
- mem_ss/200306_15h_23m_CR_bj_with_svProb0p001
- mem_ss/200310_14h_4m_CR_bj_no_svProb
- mem_ss/200310_14h_20m_MRloose_no_svProb
eem_os
- eem_os/200306_15h_33m_CR_bj_with_svProb0p001
- eem_os/200310_14h_19m_CR_bj_no_svProb
- eem_os/200310_14h_35m_MRloose_no_svProb
eem_ss
- eem_ss/200306_15h_40m_CR_bj_with_svProb0p001
- eem_ss/200310_14h_30m_CR_bj_no_svProb
- eem_ss/200310_14h_47m_MRloose_no_svProb
eee
- eee/200306_15h_47m_CR_bj_with_svProb0p001
- eee/200310_14h_41m_CR_bj_no_svProb
- eee/200310_14h_58m_MRloose_no_svProb
##########

## 2017 ##
mmm
- mmm/200306_15h_10m_CR_bj_with_svProb0p001
- mmm/200310_13h_46m_CR_bj_no_svProb
- mmm/200310_13h_59m_CR_MRloose_no_svProb
mem_os
- mem_os/200306_15h_16m_CR_bj_with_svProb0p001
- mem_os/200310_13h_54m_CR_bj_no_svProb
- mem_os/200310_14h_10m_CR_MRloose_no_svProb
mem_ss
- mem_ss/200306_15h_26m_CR_bj_with_svProb0p001
- mem_ss/200310_14h_9m_CR_bj_no_svProb
- mem_ss/200310_14h_25m _MRloose_no_svProb
eem_os
- eem_os/200306_15h_35m_CR_bj_with_svProb0p001
- eem_os/200310_14h_22m_CR_bj_no_svProb
- eem_os/200310_14h_39m_MRloose_no_svProb
eem_ss
- eem_ss/200306_15h_42m_CR_bj_with_svProb0p001
- eem_ss/200310_14h_34m_CR_bj_no_svProb
- eem_ss/200310_14h_51m_MRloose_no_svProb
eee
- eee/200306_15h_50m_CR_bj_with_svProb0p001
- eee/200310_14h_47m_CR_bj_no_svProb
- eee/200310_15h_2m_MRloose_no_svProb
##########

## 2018 ##
mmm
- mmm/200306_15h_12m_CR_bj_with_svProb0p001
- mmm/200310_13h_48m_CR_bj_no_svProb
- mmm/200310_14h_2m_CR_MRloose_no_svProb
mem_os
- mem_os/200306_15h_20m _CR_bj_with_svProb0p001
- mem_os/200310_13h_58m _CR_bj_no_svProb
- mem_os/200310_14h_15m_CR_MRloose_no_svProb
mem_ss
- mem_ss/200306_15h_29m_CR_bj_with_svProb0p001
- mem_ss/200310_14h_14m_CR_bj_no_svProb
- mem_ss/200310_14h_31m_MRloose_no_svProb
eem_os
- eem_os/200306_15h_37m_CR_bj_with_svProb0p001
- eem_os/200310_14h_26m_CR_bj_no_svProb
- eem_os/200310_14h_42m_MRloose_no_svProb
eem_ss
- eem_ss/200306_15h_45m_CR_bj_with_svProb0p001
- eem_ss/200310_14h_38m_CR_bj_no_svProb
- eem_ss/200310_14h_55m_MRloose_no_svProb
eee
- eee/200306_15h_53m_CR_bj_with_svProb0p001
- eee/200310_14h_52m_CR_bj_no_svProb
- eee/200310_15h_6m_MRloose_no_svProb
'''
