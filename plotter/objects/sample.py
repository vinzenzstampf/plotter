from re import findall
import numpy as np
import pandas as pd
from root_pandas import read_root
from collections import OrderedDict
from os.path import exists
import ROOT as rt
from os import environ as env

global channel_dict
channel_dict = OrderedDict()
channel_dict['mmm'] = 1
channel_dict['mem'] = 2
channel_dict['eee'] = 3
channel_dict['eem'] = 4

global signal_weights_dict
signal_weights_dict = OrderedDict()
signal_weights_dict['1.0em01'] = 1.0e-01
signal_weights_dict['2.0em01'] = 2.0e-01
signal_weights_dict['3.0em01'] = 3.0e-01
signal_weights_dict['4.0em01'] = 4.0e-01
signal_weights_dict['5.0em01'] = 5.0e-01
signal_weights_dict['6.0em01'] = 6.0e-01
signal_weights_dict['7.0em01'] = 7.0e-01
signal_weights_dict['8.0em01'] = 8.0e-01
signal_weights_dict['9.0em01'] = 9.0e-01
signal_weights_dict['1.0em02'] = 1.0e-02
signal_weights_dict['2.0em02'] = 2.0e-02
signal_weights_dict['3.0em02'] = 3.0e-02
signal_weights_dict['4.0em02'] = 4.0e-02
signal_weights_dict['5.0em02'] = 5.0e-02
signal_weights_dict['6.0em02'] = 6.0e-02
signal_weights_dict['7.0em02'] = 7.0e-02
signal_weights_dict['8.0em02'] = 8.0e-02
signal_weights_dict['9.0em02'] = 9.0e-02
signal_weights_dict['1.0em03'] = 1.0e-03
signal_weights_dict['2.0em03'] = 2.0e-03
signal_weights_dict['3.0em03'] = 3.0e-03
signal_weights_dict['4.0em03'] = 4.0e-03
signal_weights_dict['5.0em03'] = 5.0e-03
signal_weights_dict['6.0em03'] = 6.0e-03
signal_weights_dict['7.0em03'] = 7.0e-03
signal_weights_dict['8.0em03'] = 8.0e-03
signal_weights_dict['9.0em03'] = 9.0e-03
signal_weights_dict['1.0em04'] = 1.0e-04
signal_weights_dict['2.0em04'] = 2.0e-04
signal_weights_dict['3.0em04'] = 3.0e-04
signal_weights_dict['4.0em04'] = 4.0e-04
signal_weights_dict['5.0em04'] = 5.0e-04
signal_weights_dict['6.0em04'] = 6.0e-04
signal_weights_dict['7.0em04'] = 7.0e-04
signal_weights_dict['8.0em04'] = 8.0e-04
signal_weights_dict['9.0em04'] = 9.0e-04
signal_weights_dict['1.0em05'] = 1.0e-05
signal_weights_dict['2.0em05'] = 2.0e-05
signal_weights_dict['3.0em05'] = 3.0e-05
signal_weights_dict['4.0em05'] = 4.0e-05
signal_weights_dict['5.0em05'] = 5.0e-05
signal_weights_dict['6.0em05'] = 6.0e-05
signal_weights_dict['7.0em05'] = 7.0e-05
signal_weights_dict['8.0em05'] = 8.0e-05
signal_weights_dict['9.0em05'] = 9.0e-05
signal_weights_dict['1.0em06'] = 1.0e-06
signal_weights_dict['2.0em06'] = 2.0e-06
signal_weights_dict['3.0em06'] = 3.0e-06
signal_weights_dict['4.0em06'] = 4.0e-06
signal_weights_dict['5.0em06'] = 5.0e-06
signal_weights_dict['6.0em06'] = 6.0e-06
signal_weights_dict['7.0em06'] = 7.0e-06
signal_weights_dict['8.0em06'] = 8.0e-06
signal_weights_dict['9.0em06'] = 9.0e-06
signal_weights_dict['1.0em07'] = 1.0e-07
signal_weights_dict['2.0em07'] = 2.0e-07
signal_weights_dict['3.0em07'] = 3.0e-07
signal_weights_dict['4.0em07'] = 4.0e-07
signal_weights_dict['5.0em07'] = 5.0e-07
signal_weights_dict['6.0em07'] = 6.0e-07
signal_weights_dict['7.0em07'] = 7.0e-07
signal_weights_dict['8.0em07'] = 8.0e-07
signal_weights_dict['9.0em07'] = 9.0e-07
signal_weights_dict['1.0em08'] = 1.0e-08
signal_weights_dict['2.0em08'] = 2.0e-08
signal_weights_dict['3.0em08'] = 3.0e-08
signal_weights_dict['4.0em08'] = 4.0e-08
signal_weights_dict['5.0em08'] = 5.0e-08
signal_weights_dict['6.0em08'] = 6.0e-08
signal_weights_dict['7.0em08'] = 7.0e-08
signal_weights_dict['8.0em08'] = 8.0e-08
signal_weights_dict['9.0em08'] = 9.0e-08
signal_weights_dict['1.0em09'] = 1.0e-09
signal_weights_dict['2.0em09'] = 2.0e-09
signal_weights_dict['3.0em09'] = 3.0e-09
signal_weights_dict['4.0em09'] = 4.0e-09
signal_weights_dict['5.0em09'] = 5.0e-09
signal_weights_dict['6.0em09'] = 6.0e-09
signal_weights_dict['7.0em09'] = 7.0e-09
signal_weights_dict['8.0em09'] = 8.0e-09
signal_weights_dict['9.0em09'] = 9.0e-09
signal_weights_dict['1.0em10'] = 1.0e-10
signal_weights_dict['2.0em10'] = 2.0e-10
signal_weights_dict['3.0em10'] = 3.0e-10
signal_weights_dict['4.0em10'] = 4.0e-10
signal_weights_dict['5.0em10'] = 5.0e-10
signal_weights_dict['6.0em10'] = 6.0e-10
signal_weights_dict['7.0em10'] = 7.0e-10
signal_weights_dict['8.0em10'] = 8.0e-10
signal_weights_dict['9.0em10'] = 9.0e-10

global signal_weights
signal_weights = list(signal_weights_dict.keys())

global ranges
ranges = OrderedDict()
ranges[1 ] = (5e-5, 1e-2)
ranges[2 ] = (1e-5, 1e-2)
ranges[3 ] = (1e-6, 1e-2)
ranges[4 ] = (1e-6, 1e-2)
ranges[5 ] = (5e-7, 1e-2)
ranges[6 ] = (1e-7, 1e-2)
ranges[7 ] = (1e-7, 2e-3)
ranges[8 ] = (1e-7, 1e-3)
ranges[9 ] = (1e-7, 1e-3)
ranges[10] = (1e-7, 1e-3)
ranges[11] = (5e-7, 1e-3)
ranges[12] = (5e-7, 1e-3)
ranges[15] = (1e-6, 1e-4)
ranges[20] = (1e-6, 1e-4)


groups = OrderedDict()
groups['DY'      ] = ['DY_nlo_ext', 'DY_nlo', 'DY_lo', 'DY_lo_ext', 'DY_lo_low', 'DY_lo_low_ext']
groups['single-t'] = ['TtW', 'Ttch', 'TbtW', 'Tbtch']
groups['di-boson'] = ['WW', 'WZ', 'ZZ']
groups['TT'      ] = ['TT', 'TT_ext']
groups['W'       ] = ['W', 'W_ext']

togroup = []
for ii in groups.values(): togroup += ii


@np.vectorize
def ptcone(pt, iso, iso_cut):
    if iso < iso_cut:
        return pt
    else:
        return (1.+iso-iso_cut)*pt

#######################
####  Scalefactors ####
#######################

############
# ID #######
############

#########
## L0 ###
#########

l0_ele_ID_SFs_16_tf = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/2016LegacyReReco_ElectronMVA90noiso_Fall17V2.root')
l0_ele_ID_SFs_17_tf = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/2017_ElectronMVA90noiso.root')
l0_ele_ID_SFs_18_tf = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/2018_ElectronMVA90noiso.root')

#FIXME for 2016 runs BCDEF and GH were measured separately: https://twiki.cern.ch/twiki/bin/view/CMS/MuonReferenceEffs2016LegacyRereco#Efficiencies
l0_mu_ID_SFs_16_tf = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/RunBCDEF_SF_ID_2016.root') #TODO add SFs Runs G & H
l0_mu_ID_SFs_17_tf = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/RunBCDEF_SF_ID_2017.root') 
l0_mu_ID_SFs_18_tf = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/RunABCD_SF_ID_18.root')

l0_ID_SFs = OrderedDict()
for i in ['e','m']:
    l0_ID_SFs[i] = OrderedDict()

l0_ID_SFs['e'][2016] = l0_ele_ID_SFs_16_tf.Get('EGamma_SF2D')
l0_ID_SFs['e'][2017] = l0_ele_ID_SFs_17_tf.Get('EGamma_SF2D')
l0_ID_SFs['e'][2018] = l0_ele_ID_SFs_18_tf.Get('EGamma_SF2D')

l0_ID_SFs['m'][2016] = l0_mu_ID_SFs_16_tf.Get('NUM_MediumID_DEN_genTracks_eta_pt')
l0_ID_SFs['m'][2017] = l0_mu_ID_SFs_17_tf.Get('NUM_MediumID_DEN_genTracks_pt_abseta')
l0_ID_SFs['m'][2018] = l0_mu_ID_SFs_18_tf.Get('NUM_MediumID_DEN_TrackerMuons_pt_abseta')

##########
## LDISP #
##########

#FIXME for 2016 runs BCDEF and GH were measured separately: https://twiki.cern.ch/twiki/bin/view/CMS/MuonReferenceEffs2016LegacyRereco#Efficiencies
ldisp_mu_ID_SFs_16_tf = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/RunBCDEF_SF_ID_2016.root') #TODO add SFs Runs G & H
ldisp_mu_ID_SFs_17_tf = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/RunBCDEF_SF_ID_2017.root')
ldisp_mu_ID_SFs_18_tf = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/RunABCD_SF_ID_18.root')

ldisp_ID_SFs = OrderedDict()
for i in ['e','m']:
    ldisp_ID_SFs[i] = OrderedDict()

# FIXME which ID SFs to use for ldisp in case of electrons? below is just a *DUMMY* to check if code works
ldisp_ID_SFs['e'][2016] = l0_ele_ID_SFs_16_tf.Get('EGamma_SF2D')
ldisp_ID_SFs['e'][2017] = l0_ele_ID_SFs_17_tf.Get('EGamma_SF2D')
ldisp_ID_SFs['e'][2018] = l0_ele_ID_SFs_18_tf.Get('EGamma_SF2D')

# FIXME for now this is POG, not custom (but martina's medium is (unnoticeably?) different from POG Loose)
ldisp_ID_SFs['m'][2016] = l0_mu_ID_SFs_16_tf.Get('NUM_LooseID_DEN_genTracks_eta_pt')
ldisp_ID_SFs['m'][2017] = l0_mu_ID_SFs_17_tf.Get('NUM_LooseID_DEN_genTracks_pt_abseta')
ldisp_ID_SFs['m'][2018] = l0_mu_ID_SFs_18_tf.Get('NUM_LooseID_DEN_TrackerMuons_pt_abseta')

###########
# TRIGGER #
###########

#########
## L0 ###
#########

####################
## LDISP #from POG #
####################
ldisp_mu_Trigger_SFs_16 = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/EfficienciesStudies_2016_trigger_EfficienciesAndSF_RunBtoF.root') 
ldisp_mu_Trigger_SFs_17 = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/EfficienciesStudies_2017_trigger_EfficienciesAndSF_RunBtoF_Nov17Nov2017.root')
ldisp_mu_Trigger_SFs_18 = rt.TFile(env['BASE_DIR'] + '/plotter/objects/SF/EfficienciesStudies_2018_trigger_EfficienciesAndSF_2018Data_AfterMuonHLTUpdate.root')

ldisp_Trigger_SFs = OrderedDict()
for i in ['e','m']:
    ldisp_Trigger_SFs[i] = OrderedDict()

# ldisp_Trigger_SFs['mu'][2016] = ldisp_mu_Trigger_SFs_16
# ldisp_Trigger_SFs['mu'][2017] = ldisp_mu_Trigger_SFs_17
# ldisp_Trigger_SFs['mu'][2018] = ldisp_mu_Trigger_SFs_18

# h = tf.Get('IsoMu24_OR_IsoTkMu24_EtaBins/eta_ratio')




'''Tom's ele trigger SF
disp ele (will change)
2016-17-18
but they are going to change
'''

biNs = OrderedDict()
for i in [2016,2017,2018]:
    biNs[i] = OrderedDict()

# indices according to number of missing hits!!

biNs[2016][0] = 1.012
biNs[2016][1] = 1.024
biNs[2016][2] = 0.850
biNs[2016][3] = 0.818
biNs[2016][4] = 0.785
biNs[2016][5] = 0.658
biNs[2016][6] = 0.506

biNs[2017][0] = 1.028
biNs[2017][1] = 1.095
biNs[2017][2] = 1.070
biNs[2017][3] = 1.173
biNs[2017][4] = 1.101
biNs[2017][5] = 1.124
biNs[2017][6] = 1.304

biNs[2018][0] = 1.109
biNs[2018][1] = 1.155
biNs[2018][2] = 1.094
biNs[2018][3] = 1.072
biNs[2018][4] = 1.116
biNs[2018][5] = 1.134
biNs[2018][6] = 1.225

def get_pt_eta_SF(h, pt, eta, ch, year):
    x = h.GetXaxis()
    y = h.GetXaxis()
    if ch == 'm' and (year == 2018 or year == 2017): # pt and eta axis are different for 2017 and 2018 muon ID
        eta = np.abs(eta)
        sf = h.GetBinContent( x.FindBin(pt), y.FindBin(eta) )
    else: sf = h.GetBinContent( x.FindBin(eta), y.FindBin(pt) )
    return sf

class Sample(object):
    def __init__(self, 
                 name, 
                 samples,
                 channel,
                 label,
                 selection,
                 datacard_name,
                 colour,
                 position_in_stack, 
                 basedir, 
                 postfix, 
                 isdata, 
                 ismc, 
                 issignal, 
                 weight,
                 xs,
                 toplot=True,
                 extra_signal_weights=[],
                 is_generator=False,
                 mayfail=True,
                 year=2018):
        self.name                 = name
        self.samples              = samples
        self.channel              = channel
        self.label                = label   
        self.selection            = selection         
        self.datacard_name        = datacard_name ; print('loading', self.name, '\t', self.datacard_name, end = '')        
        self.colour               = colour           
        self.position_in_stack    = position_in_stack
        self.basedir              = basedir          
        self.postfix              = postfix          
        self.isdata               = isdata           
        self.ismc                 = ismc             
        self.issignal             = issignal         
        self.weight               = weight           
        self.xs                   = xs        
        self.nevents              = 0.
        self.file                 = '/'.join([basedir, self.name, postfix])       
        self.toplot               = toplot 
        self.extra_signal_weights = extra_signal_weights
        self.is_generator         = is_generator  
        self.mayfail              = mayfail  
        self.year                 = year  
        
        self.tree_files = []
        
        for isample in self.samples:        
            if not self.isdata:
                nevents_file = '/'.join([basedir, isample, 'SkimAnalyzerCount/SkimReport.txt'])
                with open(nevents_file) as ff:
                    lines = ff.readlines()
                    for line in lines:
                        if 'Sum Norm Weights' in line:
                            self.nevents += float(findall(r'\d+', lines[2])[0])
                            break
            fname = '/'.join([self.basedir, isample, self.postfix])
            if exists(fname):
                self.tree_files.append(fname)
                print('\tloaded: ', fname)
            elif self.mayfail and not self.is_generator:
                print('WARNING!: non existing file', fname)
            else:
                print('ERROR!: non existing file', fname)
                exit()
        
#         print('\n\n=========> tree file\n', tree_file)
#         print('\n\n=========> selection\n', self.selection, '\n\n')
                
        self.df = read_root( self.tree_files, 'tree', where=self.selection, warn_missing_tree=True ); print('\tselected events', len(self.df))
        
        # self awareness...
        self.df['channel'] = channel_dict[self.channel]
        # FIXME! extra features should be computed here once for all not in trainer or plotter
        self.df['abs_l0_eta'    ] = np.abs(self.df.l0_eta)
        self.df['abs_l1_eta'    ] = np.abs(self.df.l1_eta)
        self.df['abs_l2_eta'    ] = np.abs(self.df.l2_eta)
        self.df['abs_l0_pdgid'  ] = np.abs(self.df.l0_pdgid)
        self.df['abs_l1_pdgid'  ] = np.abs(self.df.l1_pdgid)
        self.df['abs_l2_pdgid'  ] = np.abs(self.df.l2_pdgid)
        self.df['log_abs_l0_dxy'] = np.log10(np.abs(self.df.l0_dxy))
        self.df['log_abs_l0_dz' ] = np.log10(np.abs(self.df.l0_dz ))
        self.df['log_abs_l1_dxy'] = np.log10(np.abs(self.df.l1_dxy))
        self.df['log_abs_l1_dz' ] = np.log10(np.abs(self.df.l1_dz ))
        self.df['log_abs_l2_dxy'] = np.log10(np.abs(self.df.l2_dxy))
        self.df['log_abs_l2_dz' ] = np.log10(np.abs(self.df.l2_dz ))
        self.df['abs_q_02'      ] = np.abs(self.df.hnl_q_02)
        self.df['abs_q_01'      ] = np.abs(self.df.hnl_q_01)
        self.df['abs_q_12'      ] = np.abs(self.df.hnl_q_12)
        
        self.df['log_l0_dxy_sig'] = np.log10(self.df.l0_dxy_error / np.abs(self.df.l0_dxy ))
        self.df['log_l1_dxy_sig'] = np.log10(self.df.l1_dxy_error / np.abs(self.df.l1_dxy ))
        self.df['log_l2_dxy_sig'] = np.log10(self.df.l2_dxy_error / np.abs(self.df.l2_dxy ))
        self.df['log_l0_dz_sig' ] = np.log10(self.df.l0_dz_error / np.abs(self.df.l0_dz ))
        self.df['log_l1_dz_sig' ] = np.log10(self.df.l1_dz_error / np.abs(self.df.l1_dz ))
        self.df['log_l2_dz_sig' ] = np.log10(self.df.l2_dz_error / np.abs(self.df.l2_dz ))

        self.df['log_hnl_2d_disp'    ] = np.log10(self.df.hnl_2d_disp)
        self.df['log_hnl_2d_disp_sig'] = np.log10(self.df.hnl_2d_disp_sig)
        
        self.df['l0_ptcone'] = ptcone(self.df.l0_pt, self.df.l0_reliso_rho_03, 0.1) if len(self.df) else np.nan
        self.df['l1_ptcone'] = ptcone(self.df.l1_pt, self.df.l1_reliso_rho_03, 0.2) if len(self.df) else np.nan
        self.df['l2_ptcone'] = ptcone(self.df.l2_pt, self.df.l2_reliso_rho_03, 0.2) if len(self.df) else np.nan
        
        # defined à la Martina
        self.df['hnl_2d_disp_sig_alt'] = self.df.hnl_2d_disp**2 / np.sqrt(self.df.sv_covxx * self.df.sv_x**2 + self.df.sv_covyy * self.df.sv_y**2)
        
        self.df['_norm_'] = 0.

        ## SFs
        # if self.ismc:
        print('### Computing Scalefactors...')
        ## Trigger ## TODO
        ## ID ##
        # l0
        self.df['l0_id_sf'] = get_pf_eta_SF( l0_ID_SFs[self.channel[0]][self.year],     self.df['l0_pt'], self.df['l0_eta'], self.channel[0], self.year)
        # l1
        self.df['l1_id_sf'] = get_pf_eta_SF( ldisp_ID_SFs[self.channel[0]][self.year],  self.df['l1_pt'], self.df['l1_eta'], self.channel[1], self.year)
        # l2
        self.df['l2_id_sf'] = get_pf_eta_SF( ldisp_ID_SFs[self.channel[0]][self.year],  self.df['l2_pt'], self.df['l2_eta'], self.channel[2], self.year)
        ## ISO ## TODO
        print('### Scalefactors finished.')
        
        self.df['year'] = self.year

        self.df['isdata'] = self.isdata
                
        # scale to 1/pb 
        self.lumi_scaling = 1. if self.isdata else (self.xs / self.nevents)
