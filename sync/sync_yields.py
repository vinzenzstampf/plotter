from collections import OrderedDict
from glob import glob
import ROOT as rt


years = ['2016', '2017', '2018']
chs = ['eee', 'eem_os', 'eem_ss', 'mem_ss', 'mem_os', 'mmm']
disps = ['lt_0p5', '0p5_to_1p5','1p5_to_4p0', 'mt_4p0']
bins = ['lo', 'hi']

sig8  = 'hnl_m_8_v2_2p3Em06_majorana'
sig10 = 'hnl_m_10_v2_1p0Em06_majorana'
sigs = [sig8, sig10]

folders = glob('/Users/cesareborgia/cernbox/plots/plotter/*/*/*/datacards/') # year/channel/date_of_prod

files = OrderedDict()

for f in folders:
    f_yr = f.split('/')[-5]
    f_ch = f.split('/')[-4]
    try: files[f_yr][f_ch] = f
    except: 
        files[f_yr] = OrderedDict()
        files[f_yr][f_ch] = f

yields = OrderedDict()

for yr in years:
    yields[yr] = OrderedDict()
    for ch in chs:    
        yields[yr][ch] = OrderedDict()
        for disp in disps: 
            yields[yr][ch][disp] = OrderedDict()
            for sig in sigs:  
                yields[yr][ch][disp][sig] = OrderedDict()


for yr in files.keys():
    for ch in files[yr].keys():
        f_in = OrderedDict()
        for disp in disps:
            f_in[disp]  = rt.TFile(files[yr][ch] + 'datacard_hnl_m_12_lxy_{disp}.root'.format(disp = disp))
            for sig in sigs:
                if ch[0] == 'm' and '2p3' in sig: continue #muon channels don't have the m=8,v2=2.3e-6 signal
                h = f_in[disp].Get(sig)
                yields[yr][ch][disp][sig] = OrderedDict()
                yields[yr][ch][disp][sig]['lo'] = h.GetBinContent(1)
                yields[yr][ch][disp][sig]['hi'] = h.GetBinContent(2)


out_folder = glob('/Users/cesareborgia/cernbox/plots/plotter/sync/') 

with open(out_folder + 'sync_yields.txt', 'w') as f:
    for yr in years:
        for ch in chs:
            print >> f, 'year={yr}'
            print >> f, 'channel={ch}'
            print >> f, '\t\t\t\t{disp0}\t\t\t\t{disp1}\t\t\t\t{disp2}\t\t\t\t{disp3}'
            print >> f, '\t\t{d0_mlo}\t\t{d0_mhi}\t\t{d1_mlo}\t\t{d1_mhi}\t\t{d2_mlo}\t\t{d2_mhi}\t\t{d3_mlo}\t\t{d3_mhi}'

