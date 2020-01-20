from collections import OrderedDict
from glob import glob

yields = OrderedDict()

# channels['eee'   ] = 'hnl_m_8_v2_2p3Em06_majorana'
# channels['mmm'   ] = 'hnl_m_10_v2_1p0Em06_majorana'

folders = glob('/Users/cesareborgia/cernbox/plots/plotter/*/*/*/datacards/') # year/channel/date_of_prod

years = [2016, 2017, 2018]
chs = ['eee', 'eem_os', 'eem_ss', 'mme_ss', 'mme_os', 'mmm']
disps = ['lt_0p5', '0p5_to_1p5','10p5_to_4p0', 'mt_4p0']

sig8  = 'hnl_m_8_v2_2p3Em06_majorana'
sig10 = 'hnl_m_10_v2_1p0Em06_majorana'
sigs = [sig8, sig10]

for yr in years: yields[yr] = OrderedDict()
    for ch in chs: yields[yr][ch] = OrderedDict()

for disp in disps:

   'datacard_hnl_m_12_lxy_{disp}.root'.format(yr = year, ch = ch, disp = disp)

    f_in  = rt.TFile(f)

    for sig in sigs:
        h8 = f_in.Get(sig8)
        y8_lo = h8.getbincontent(1)
        y8_hi = h8.getbincontent(2)


