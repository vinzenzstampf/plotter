from collections import OrderedDict
from glob import glob
import ROOT as rt


years = ['2016', '2017', '2018']
chs = ['eee', 'eem_os', 'eem_ss', 'mem_ss', 'mem_os', 'mmm']
disps = ['lt_0p5', '0p5_to_1p5','1p5_to_4p0', 'mt_4p0']
bins = ['lo', 'hi']

prmp  = 'prompt' 
nonp  = 'nonprompt'
sig8  = 'hnl_m_8_v2_2p3Em06_majorana'
sig10 = 'hnl_m_10_v2_1p0Em06_majorana'
sigs  = [sig8, sig10]

# folders = glob('/Users/cesareborgia/cernbox/plots/plotter/*/*/*/datacards/') # year/channel/date_of_prod
# folders = glob('/Users/cesareborgia/cernbox/plots/plotter/*/*/200122_*/datacards/') # year/channel/date_of_prod
folders = glob('/Users/cesareborgia/cernbox/plots/plotter/*/*/20021*/datacards/') # year/channel/date_of_prod


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
                h_sig = f_in[disp].Get(sig)
                h_nonp = f_in[disp].Get(nonp)
                h_prmp = f_in[disp].Get(prmp)

                yields[yr][ch][disp][sig] = OrderedDict()
                yields[yr][ch][disp][nonp] = OrderedDict()
                yields[yr][ch][disp][prmp] = OrderedDict()
                
                yields[yr][ch][disp][sig]['lo']  = h_sig.GetBinContent(1)
                yields[yr][ch][disp][sig]['hi']  = h_sig.GetBinContent(2)
                
                yields[yr][ch][disp][nonp]['lo'] = h_nonp.GetBinContent(1)
                yields[yr][ch][disp][nonp]['hi'] = h_nonp.GetBinContent(2)
                
                yields[yr][ch][disp][prmp]['lo'] = h_prmp.GetBinContent(1)
                yields[yr][ch][disp][prmp]['hi'] = h_prmp.GetBinContent(2)


out_folder = '/Users/cesareborgia/HNL/plotter/sync/'

with open(out_folder + 'sync_yields.txt', 'w') as f:
    for yr in files.keys():
        for ch in files[yr].keys():
            f.write('\n\t\tyear={yr}\n'.format(yr=yr))
            
            f.write('\t\tchannel={ch}\n'.format(ch=ch))
            
            f.write('\t\t\tdisp\t\t{disp0}\t\t\t\t{disp1}\t\t\t{disp2}\t\t\t{disp3}\n'.format(disp0=disps[0],disp1=disps[1],disp2=disps[2],disp3=disps[3]))

            f.write('\t\t\tbin\t\t0 < m < 4\t4 < m < 12')
            f.write('\t0 < m < 4\t4 < m < 12')
            f.write('\t0 < m < 4\t4 < m < 12')
            f.write('\t0 < m < 4\t4 < m < 12')
            f.write('\n')

            f.write('\t\t\tnon-prompt\t{d0_mlo:.3f}\t\t{d0_mhi:.3f}\t\t{d1_mlo:.3f}\t\t{d1_mhi:.3f}'.format(d0_mlo=yields[yr][ch][disps[0]][nonp]['lo'], d0_mhi=yields[yr][ch][disps[0]][nonp]['hi'], 
                                                                                                            d1_mlo=yields[yr][ch][disps[1]][nonp]['lo'], d1_mhi=yields[yr][ch][disps[1]][nonp]['hi']))
                             
            f.write('\t\t{d2_mlo:.3f}\t\t{d2_mhi:.3f}\t\t{d3_mlo:.3f}\t\t{d3_mhi:.3f}'.format(d2_mlo=yields[yr][ch][disps[2]][nonp]['lo'], d2_mhi=yields[yr][ch][disps[2]][nonp]['hi'], 
                                                                                              d3_mlo=yields[yr][ch][disps[3]][nonp]['lo'], d3_mhi=yields[yr][ch][disps[3]][nonp]['hi']))

            f.write('\n')

            f.write('\t\t\tprompt\t\t{d0_mlo:.3f}\t\t{d0_mhi:.3f}\t\t{d1_mlo:.3f}\t\t{d1_mhi:.3f}'.format(d0_mlo=yields[yr][ch][disps[0]][prmp]['lo'], d0_mhi=yields[yr][ch][disps[0]][prmp]['hi'], 
                                                                                                          d1_mlo=yields[yr][ch][disps[1]][prmp]['lo'], d1_mhi=yields[yr][ch][disps[1]][prmp]['hi']))
                             
            f.write('\t\t{d2_mlo:.3f}\t\t{d2_mhi:.3f}\t\t{d3_mlo:.3f}\t\t{d3_mhi:.3f}'.format(d2_mlo=yields[yr][ch][disps[2]][prmp]['lo'], d2_mhi=yields[yr][ch][disps[2]][prmp]['hi'], 
                                                                                              d3_mlo=yields[yr][ch][disps[3]][prmp]['lo'], d3_mhi=yields[yr][ch][disps[3]][prmp]['hi']))

            f.write('\n')
         
            for sig in sigs:
                if ch[0] == 'm' and '2p3' in sig: continue #muon channels don't have the m=8,v2=2.3e-6 signal
                f.write('\t{s}\t{d0_mlo:.3f}\t\t{d0_mhi:.3f}\t\t{d1_mlo:.3f}\t\t{d1_mhi:.3f}'.format(s=sig, d0_mlo=yields[yr][ch][disps[0]][sig]['lo'], d0_mhi=yields[yr][ch][disps[0]][sig]['hi'], 
                                                                                                     d1_mlo=yields[yr][ch][disps[1]][sig]['lo'], d1_mhi=yields[yr][ch][disps[1]][sig]['hi']))
                                 
                f.write('\t\t{d2_mlo:.3f}\t\t{d2_mhi:.3f}\t\t{d3_mlo:.3f}\t\t{d3_mhi:.3f}'.format(d2_mlo=yields[yr][ch][disps[2]][sig]['lo'], d2_mhi=yields[yr][ch][disps[2]][sig]['hi'], 
                                                                                                  d3_mlo=yields[yr][ch][disps[3]][sig]['lo'], d3_mhi=yields[yr][ch][disps[3]][sig]['hi']))
                f.write('\n')

            f.write('\n\n')
f.close()
