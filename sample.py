import re
import numpy as np
import pandas as pd
from root_pandas import read_root

class Sample(object):
    def __init__(self, 
                 name, 
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
                 extra_signal_weights=[]):
        self.name                 = name ; print('loading', self.name)
        self.label                = label   
        self.selection            = selection         
        self.datacard_name        = datacard_name            
        self.colour               = colour           
        self.position_in_stack    = position_in_stack
        self.basedir              = basedir          
        self.postfix              = postfix          
        self.isdata               = isdata           
        self.ismc                 = ismc             
        self.issignal             = issignal         
        self.weight               = weight           
        self.xs                   = xs        
        self.nevents              = 1.
        self.file                 = '/'.join([basedir, self.name, postfix])       
        self.toplot               = toplot 
        self.extra_signal_weights = extra_signal_weights  
        
        if not self.isdata:
            nevents_file = '/'.join([basedir, self.name, 'SkimAnalyzerCount/SkimReport.txt'])
            with open(nevents_file) as ff:
                lines = ff.readlines()
                for line in lines:
                    if 'Sum Norm Weights' in line:
                        self.nevents = float(re.findall(r'\d+', lines[2])[0])
                        break
        tree_file = '/'.join([self.basedir, self.name, self.postfix])
        
        # selection = self.selection.replace('&', 'and').replace('|', 'or').replace('!', 'not') 
        # self.df = uproot.open(tree_file)['tree'].pandas.df().query(selection) # can't apply any selection with uproot...
        # self.df = pd.DataFrame( root2array(tree_file, 'tree', selection=self.selection) )
        self.df = read_root( tree_file, 'tree', where=self.selection )
        # scale to 1/pb 
        self.lumi_scaling = 1. if self.isdata else (self.xs / self.nevents)
 


def get_data_samples(basedir, postfix, selection):
    data = [
        Sample('Single_mu_2018A', '2018A', selection, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
        Sample('Single_mu_2018B', '2018B', selection, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
        Sample('Single_mu_2018C', '2018C', selection, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
        Sample('Single_mu_2018D', '2018D', selection, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
    ]
    return data

def get_mc_samples(basedir, postfix, selection):
    mc = [
        Sample('DYJetsToLL_M50_ext', r'DY$\to\ell\ell$', selection, 'DY', 'gold'     ,10, basedir, postfix, False, True, False, 1.,  6077.22),
        Sample('TTJets_ext'        , r'$t\bar{t}$'     , selection, 'TT', 'slateblue', 0, basedir, postfix, False, True, False, 1.,   831.76),
        Sample('WW'                , 'WW'              , selection, 'WW', 'blue'     , 5, basedir, postfix, False, True, False, 1.,    75.88),
        Sample('WZ'                , 'WZ'              , selection, 'WZ', 'blue'     , 5, basedir, postfix, False, True, False, 1.,    27.6 ),
        Sample('ZZ'                , 'ZZ'              , selection, 'ZZ', 'blue'     , 5, basedir, postfix, False, True, False, 1.,    12.14),
    ]   
    return mc         

def get_signal_samples(basedir, postfix, selection):
    signal = [ 
        ########## M = 1
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=9.0 10^{-3}, Majorana' , selection, 'hnl_m_1_v2_9p0Em03_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False),
        # weighted samples
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=1.0 10^{-9}, Majorana' , selection, 'hnl_m_1_v2_1p0Em09_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_1em09'  , 'xs_w_v2_1em09'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=5.0 10^{-9}, Majorana' , selection, 'hnl_m_1_v2_5p0Em09_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_5em09'  , 'xs_w_v2_5em09'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=1.0 10^{-8}, Majorana' , selection, 'hnl_m_1_v2_1p0Em08_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_1em08'  , 'xs_w_v2_1em08'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=5.0 10^{-8}, Majorana' , selection, 'hnl_m_1_v2_5p0Em08_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_5em08'  , 'xs_w_v2_5em08'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=1.0 10^{-7}, Majorana' , selection, 'hnl_m_1_v2_1p0Em07_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_1em07'  , 'xs_w_v2_1em07'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=5.0 10^{-7}, Majorana' , selection, 'hnl_m_1_v2_5p0Em07_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_5em07'  , 'xs_w_v2_5em07'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=5.0 10^{-6}, Majorana' , selection, 'hnl_m_1_v2_5p0Em06_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_5em06'  , 'xs_w_v2_5em06'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=6.0 10^{-6}, Majorana' , selection, 'hnl_m_1_v2_6p0Em06_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_6em06'  , 'xs_w_v2_6em06'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=8.0 10^{-6}, Majorana' , selection, 'hnl_m_1_v2_8p0Em06_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_8em06'  , 'xs_w_v2_8em06'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=1.0 10^{-5}, Majorana' , selection, 'hnl_m_1_v2_1p0Em05_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_1em05'  , 'xs_w_v2_1em05'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=2.0 10^{-5}, Majorana' , selection, 'hnl_m_1_v2_2p0Em05_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_2em05'  , 'xs_w_v2_2em05'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=3.0 10^{-5}, Majorana' , selection, 'hnl_m_1_v2_3p0Em05_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_3em05'  , 'xs_w_v2_3em05'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=4.0 10^{-5}, Majorana' , selection, 'hnl_m_1_v2_4p0Em05_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_4em05'  , 'xs_w_v2_4em05'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=5.0 10^{-5}, Majorana' , selection, 'hnl_m_1_v2_5p0Em05_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_5em05'  , 'xs_w_v2_5em05'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=7.0 10^{-5}, Majorana' , selection, 'hnl_m_1_v2_7p0Em05_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_7em05'  , 'xs_w_v2_7em05'  ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=1.0 10^{-4}, Majorana' , selection, 'hnl_m_1_v2_1p0Em04_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_0.0001' , 'xs_w_v2_0.0001' ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=2.0 10^{-4}, Majorana' , selection, 'hnl_m_1_v2_2p0Em04_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_0.0002' , 'xs_w_v2_0.0002' ]),
        Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'   , 'm=1 GeV, |V|^{2}=2.5 10^{-4}, Majorana' , selection, 'hnl_m_1_v2_2p5Em04_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False, extra_signal_weights=['ctau_w_v2_0.00025', 'xs_w_v2_0.00025']),

        ########## M = 2
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=1.2 10^{-4}, Majorana' , selection, 'hnl_m_2_v2_1p2Em04_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=True ),
        Sample('HN3L_M_2_V_0p0248394846967_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=6.2 10^{-4}, Majorana' , selection, 'hnl_m_2_v2_6p2Em04_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  2.647    , toplot=False),
        # weighted samples
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=1.0 10^{-9}, Majorana' , selection, 'hnl_m_2_v2_1p0Em09_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_1em09'  , 'xs_w_v2_1em09'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=5.0 10^{-9}, Majorana' , selection, 'hnl_m_2_v2_5p0Em09_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_5em09'  , 'xs_w_v2_5em09'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=1.0 10^{-8}, Majorana' , selection, 'hnl_m_2_v2_1p0Em08_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_1em08'  , 'xs_w_v2_1em08'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=5.0 10^{-8}, Majorana' , selection, 'hnl_m_2_v2_5p0Em08_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_5em08'  , 'xs_w_v2_5em08'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=1.0 10^{-7}, Majorana' , selection, 'hnl_m_2_v2_1p0Em07_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_1em07'  , 'xs_w_v2_1em07'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=5.0 10^{-7}, Majorana' , selection, 'hnl_m_2_v2_5p0Em07_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_5em07'  , 'xs_w_v2_5em07'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=5.0 10^{-6}, Majorana' , selection, 'hnl_m_2_v2_5p0Em06_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_5em06'  , 'xs_w_v2_5em06'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=6.0 10^{-6}, Majorana' , selection, 'hnl_m_2_v2_6p0Em06_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_6em06'  , 'xs_w_v2_6em06'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=8.0 10^{-6}, Majorana' , selection, 'hnl_m_2_v2_8p0Em06_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_8em06'  , 'xs_w_v2_8em06'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=1.0 10^{-5}, Majorana' , selection, 'hnl_m_2_v2_1p0Em05_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_1em05'  , 'xs_w_v2_1em05'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=2.0 10^{-5}, Majorana' , selection, 'hnl_m_2_v2_2p0Em05_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_2em05'  , 'xs_w_v2_2em05'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=3.0 10^{-5}, Majorana' , selection, 'hnl_m_2_v2_3p0Em05_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_3em05'  , 'xs_w_v2_3em05'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=4.0 10^{-5}, Majorana' , selection, 'hnl_m_2_v2_4p0Em05_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_4em05'  , 'xs_w_v2_4em05'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=5.0 10^{-5}, Majorana' , selection, 'hnl_m_2_v2_5p0Em05_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_5em05'  , 'xs_w_v2_5em05'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=7.0 10^{-5}, Majorana' , selection, 'hnl_m_2_v2_7p0Em05_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_7em05'  , 'xs_w_v2_7em05'  ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=1.0 10^{-4}, Majorana' , selection, 'hnl_m_2_v2_1p0Em04_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_0.0001' , 'xs_w_v2_0.0001' ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=2.0 10^{-4}, Majorana' , selection, 'hnl_m_2_v2_2p0Em04_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_0.0002' , 'xs_w_v2_0.0002' ]),
        Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'   , 'm=2 GeV, |V|^{2}=2.5 10^{-4}, Majorana' , selection, 'hnl_m_2_v2_2p5Em04_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=False, extra_signal_weights=['ctau_w_v2_0.00025', 'xs_w_v2_0.00025']),

        ########## M = 3
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=5.0 10^{-5}, Majorana' , selection, 'hnl_m_3_v2_5p0Em05_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False),
        # weighted samples
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=1.0 10^{-9}, Majorana' , selection, 'hnl_m_3_v2_1p0Em09_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_1em09'  , 'xs_w_v2_1em09'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=5.0 10^{-9}, Majorana' , selection, 'hnl_m_3_v2_5p0Em09_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_5em09'  , 'xs_w_v2_5em09'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=1.0 10^{-8}, Majorana' , selection, 'hnl_m_3_v2_1p0Em08_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_1em08'  , 'xs_w_v2_1em08'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=5.0 10^{-8}, Majorana' , selection, 'hnl_m_3_v2_5p0Em08_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_5em08'  , 'xs_w_v2_5em08'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=1.0 10^{-7}, Majorana' , selection, 'hnl_m_3_v2_1p0Em07_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_1em07'  , 'xs_w_v2_1em07'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=5.0 10^{-7}, Majorana' , selection, 'hnl_m_3_v2_5p0Em07_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_5em07'  , 'xs_w_v2_5em07'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=5.0 10^{-6}, Majorana' , selection, 'hnl_m_3_v2_5p0Em06_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_5em06'  , 'xs_w_v2_5em06'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=6.0 10^{-6}, Majorana' , selection, 'hnl_m_3_v2_6p0Em06_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_6em06'  , 'xs_w_v2_6em06'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=8.0 10^{-6}, Majorana' , selection, 'hnl_m_3_v2_8p0Em06_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_8em06'  , 'xs_w_v2_8em06'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=1.0 10^{-5}, Majorana' , selection, 'hnl_m_3_v2_1p0Em05_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_1em05'  , 'xs_w_v2_1em05'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=2.0 10^{-5}, Majorana' , selection, 'hnl_m_3_v2_2p0Em05_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_2em05'  , 'xs_w_v2_2em05'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=3.0 10^{-5}, Majorana' , selection, 'hnl_m_3_v2_3p0Em05_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_3em05'  , 'xs_w_v2_3em05'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=4.0 10^{-5}, Majorana' , selection, 'hnl_m_3_v2_4p0Em05_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_4em05'  , 'xs_w_v2_4em05'  ]),
#         Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=5.0 10^{-5}, Majorana' , selection, 'hnl_m_3_v2_5p0Em05_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_5em05'  , 'xs_w_v2_5em05'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=7.0 10^{-5}, Majorana' , selection, 'hnl_m_3_v2_7p0Em05_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_7em05'  , 'xs_w_v2_7em05'  ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=1.0 10^{-4}, Majorana' , selection, 'hnl_m_3_v2_1p0Em04_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_0.0001' , 'xs_w_v2_0.0001' ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=2.0 10^{-4}, Majorana' , selection, 'hnl_m_3_v2_2p0Em04_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_0.0002' , 'xs_w_v2_0.0002' ]),
        Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'  , 'm=3 GeV, |V|^{2}=2.5 10^{-4}, Majorana' , selection, 'hnl_m_3_v2_2p5Em04_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False, extra_signal_weights=['ctau_w_v2_0.00025', 'xs_w_v2_0.00025']),

        ########## M = 4
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=8.4 10^{-6}, Majorana' , selection, 'hnl_m_4_v2_8p4Em06_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False),
        # weighted samples
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=1.0 10^{-9}, Majorana' , selection, 'hnl_m_4_v2_1p0Em09_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_1em09'  , 'xs_w_v2_1em09'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=5.0 10^{-9}, Majorana' , selection, 'hnl_m_4_v2_5p0Em09_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_5em09'  , 'xs_w_v2_5em09'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=1.0 10^{-8}, Majorana' , selection, 'hnl_m_4_v2_1p0Em08_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_1em08'  , 'xs_w_v2_1em08'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=5.0 10^{-8}, Majorana' , selection, 'hnl_m_4_v2_5p0Em08_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_5em08'  , 'xs_w_v2_5em08'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=1.0 10^{-7}, Majorana' , selection, 'hnl_m_4_v2_1p0Em07_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_1em07'  , 'xs_w_v2_1em07'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=5.0 10^{-7}, Majorana' , selection, 'hnl_m_4_v2_5p0Em07_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_5em07'  , 'xs_w_v2_5em07'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=5.0 10^{-6}, Majorana' , selection, 'hnl_m_4_v2_5p0Em06_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_5em06'  , 'xs_w_v2_5em06'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=6.0 10^{-6}, Majorana' , selection, 'hnl_m_4_v2_6p0Em06_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_6em06'  , 'xs_w_v2_6em06'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=8.0 10^{-6}, Majorana' , selection, 'hnl_m_4_v2_8p0Em06_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_8em06'  , 'xs_w_v2_8em06'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=1.0 10^{-5}, Majorana' , selection, 'hnl_m_4_v2_1p0Em05_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_1em05'  , 'xs_w_v2_1em05'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=2.0 10^{-5}, Majorana' , selection, 'hnl_m_4_v2_2p0Em05_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_2em05'  , 'xs_w_v2_2em05'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=3.0 10^{-5}, Majorana' , selection, 'hnl_m_4_v2_3p0Em05_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_3em05'  , 'xs_w_v2_3em05'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=4.0 10^{-5}, Majorana' , selection, 'hnl_m_4_v2_4p0Em05_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_4em05'  , 'xs_w_v2_4em05'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=5.0 10^{-5}, Majorana' , selection, 'hnl_m_4_v2_5p0Em05_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_5em05'  , 'xs_w_v2_5em05'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=7.0 10^{-5}, Majorana' , selection, 'hnl_m_4_v2_7p0Em05_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_7em05'  , 'xs_w_v2_7em05'  ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=1.0 10^{-4}, Majorana' , selection, 'hnl_m_4_v2_1p0Em04_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_0.0001' , 'xs_w_v2_0.0001' ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=2.0 10^{-4}, Majorana' , selection, 'hnl_m_4_v2_2p0Em04_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_0.0002' , 'xs_w_v2_0.0002' ]),
        Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'  , 'm=4 GeV, |V|^{2}=2.5 10^{-4}, Majorana' , selection, 'hnl_m_4_v2_2p5Em04_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False, extra_signal_weights=['ctau_w_v2_0.00025', 'xs_w_v2_0.00025']),

        ########## M = 5
        Sample('HN3L_M_5_V_0p000316227766017_mu_massiveAndCKM_LO' , 'm=5 GeV, |V|^{2}=1.0 10^{-7}, Majorana' , selection, 'hnl_m_5_v2_1p0Em07_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.0003981, toplot=False),
        Sample('HN3L_M_5_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=5 GeV, |V|^{2}=3.0 10^{-7}, Majorana' , selection, 'hnl_m_5_v2_3p0Em07_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.001194 , toplot=False),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=2.1 10^{-6}, Majorana' , selection, 'hnl_m_5_v2_2p1Em06_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=True ),
        # weighted samples
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=1.0 10^{-9}, Majorana' , selection, 'hnl_m_5_v2_1p0Em09_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_1em09'  , 'xs_w_v2_1em09'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=5.0 10^{-9}, Majorana' , selection, 'hnl_m_5_v2_5p0Em09_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_5em09'  , 'xs_w_v2_5em09'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=1.0 10^{-8}, Majorana' , selection, 'hnl_m_5_v2_1p0Em08_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_1em08'  , 'xs_w_v2_1em08'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=5.0 10^{-8}, Majorana' , selection, 'hnl_m_5_v2_5p0Em08_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_5em08'  , 'xs_w_v2_5em08'  ]),
#         Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=1.0 10^{-7}, Majorana' , selection, 'hnl_m_5_v2_1p0Em07_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_1em07'  , 'xs_w_v2_1em07'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=5.0 10^{-7}, Majorana' , selection, 'hnl_m_5_v2_5p0Em07_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_5em07'  , 'xs_w_v2_5em07'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=5.0 10^{-6}, Majorana' , selection, 'hnl_m_5_v2_5p0Em06_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_5em06'  , 'xs_w_v2_5em06'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=6.0 10^{-6}, Majorana' , selection, 'hnl_m_5_v2_6p0Em06_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_6em06'  , 'xs_w_v2_6em06'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=8.0 10^{-6}, Majorana' , selection, 'hnl_m_5_v2_8p0Em06_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_8em06'  , 'xs_w_v2_8em06'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=1.0 10^{-5}, Majorana' , selection, 'hnl_m_5_v2_1p0Em05_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_1em05'  , 'xs_w_v2_1em05'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=2.0 10^{-5}, Majorana' , selection, 'hnl_m_5_v2_2p0Em05_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_2em05'  , 'xs_w_v2_2em05'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=3.0 10^{-5}, Majorana' , selection, 'hnl_m_5_v2_3p0Em05_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_3em05'  , 'xs_w_v2_3em05'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=4.0 10^{-5}, Majorana' , selection, 'hnl_m_5_v2_4p0Em05_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_4em05'  , 'xs_w_v2_4em05'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=5.0 10^{-5}, Majorana' , selection, 'hnl_m_5_v2_5p0Em05_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_5em05'  , 'xs_w_v2_5em05'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=7.0 10^{-5}, Majorana' , selection, 'hnl_m_5_v2_7p0Em05_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_7em05'  , 'xs_w_v2_7em05'  ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=1.0 10^{-4}, Majorana' , selection, 'hnl_m_5_v2_1p0Em04_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_0.0001' , 'xs_w_v2_0.0001' ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=2.0 10^{-4}, Majorana' , selection, 'hnl_m_5_v2_2p0Em04_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_0.0002' , 'xs_w_v2_0.0002' ]),
        Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=2.5 10^{-4}, Majorana' , selection, 'hnl_m_5_v2_2p5Em04_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=False, extra_signal_weights=['ctau_w_v2_0.00025', 'xs_w_v2_0.00025']),

        ########## M = 6
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=4.1 10^{-6}, Majorana' , selection, 'hnl_m_6_v2_4p1Em06_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False),
        # weighted samples
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=1.0 10^{-9}, Majorana' , selection, 'hnl_m_6_v2_1p0Em09_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_1em09'  , 'xs_w_v2_1em09'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=5.0 10^{-9}, Majorana' , selection, 'hnl_m_6_v2_5p0Em09_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_5em09'  , 'xs_w_v2_5em09'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=1.0 10^{-8}, Majorana' , selection, 'hnl_m_6_v2_1p0Em08_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_1em08'  , 'xs_w_v2_1em08'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=5.0 10^{-8}, Majorana' , selection, 'hnl_m_6_v2_5p0Em08_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_5em08'  , 'xs_w_v2_5em08'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=1.0 10^{-7}, Majorana' , selection, 'hnl_m_6_v2_1p0Em07_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_1em07'  , 'xs_w_v2_1em07'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=5.0 10^{-7}, Majorana' , selection, 'hnl_m_6_v2_5p0Em07_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_5em07'  , 'xs_w_v2_5em07'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=5.0 10^{-6}, Majorana' , selection, 'hnl_m_6_v2_5p0Em06_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_5em06'  , 'xs_w_v2_5em06'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=6.0 10^{-6}, Majorana' , selection, 'hnl_m_6_v2_6p0Em06_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_6em06'  , 'xs_w_v2_6em06'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=8.0 10^{-6}, Majorana' , selection, 'hnl_m_6_v2_8p0Em06_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_8em06'  , 'xs_w_v2_8em06'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=1.0 10^{-5}, Majorana' , selection, 'hnl_m_6_v2_1p0Em05_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_1em05'  , 'xs_w_v2_1em05'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=2.0 10^{-5}, Majorana' , selection, 'hnl_m_6_v2_2p0Em05_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_2em05'  , 'xs_w_v2_2em05'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=3.0 10^{-5}, Majorana' , selection, 'hnl_m_6_v2_3p0Em05_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_3em05'  , 'xs_w_v2_3em05'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=4.0 10^{-5}, Majorana' , selection, 'hnl_m_6_v2_4p0Em05_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_4em05'  , 'xs_w_v2_4em05'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=5.0 10^{-5}, Majorana' , selection, 'hnl_m_6_v2_5p0Em05_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_5em05'  , 'xs_w_v2_5em05'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=7.0 10^{-5}, Majorana' , selection, 'hnl_m_6_v2_7p0Em05_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_7em05'  , 'xs_w_v2_7em05'  ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=1.0 10^{-4}, Majorana' , selection, 'hnl_m_6_v2_1p0Em04_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_0.0001' , 'xs_w_v2_0.0001' ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=2.0 10^{-4}, Majorana' , selection, 'hnl_m_6_v2_2p0Em04_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_0.0002' , 'xs_w_v2_0.0002' ]),
        Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=2.5 10^{-4}, Majorana' , selection, 'hnl_m_6_v2_2p5Em04_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False, extra_signal_weights=['ctau_w_v2_0.00025', 'xs_w_v2_0.00025']),

        ########## M = 8
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=3.0 10^{-7}, Majorana' , selection, 'hnl_m_8_v2_3p0Em07_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False),
        # weighted samples
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=1.0 10^{-9}, Majorana' , selection, 'hnl_m_8_v2_1p0Em09_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_1em09'  , 'xs_w_v2_1em09'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=5.0 10^{-9}, Majorana' , selection, 'hnl_m_8_v2_5p0Em09_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_5em09'  , 'xs_w_v2_5em09'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=1.0 10^{-8}, Majorana' , selection, 'hnl_m_8_v2_1p0Em08_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_1em08'  , 'xs_w_v2_1em08'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=5.0 10^{-8}, Majorana' , selection, 'hnl_m_8_v2_5p0Em08_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_5em08'  , 'xs_w_v2_5em08'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=1.0 10^{-7}, Majorana' , selection, 'hnl_m_8_v2_1p0Em07_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_1em07'  , 'xs_w_v2_1em07'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=5.0 10^{-7}, Majorana' , selection, 'hnl_m_8_v2_5p0Em07_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_5em07'  , 'xs_w_v2_5em07'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=5.0 10^{-6}, Majorana' , selection, 'hnl_m_8_v2_5p0Em06_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_5em06'  , 'xs_w_v2_5em06'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=6.0 10^{-6}, Majorana' , selection, 'hnl_m_8_v2_6p0Em06_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_6em06'  , 'xs_w_v2_6em06'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=8.0 10^{-6}, Majorana' , selection, 'hnl_m_8_v2_8p0Em06_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_8em06'  , 'xs_w_v2_8em06'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=1.0 10^{-5}, Majorana' , selection, 'hnl_m_8_v2_1p0Em05_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_1em05'  , 'xs_w_v2_1em05'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=2.0 10^{-5}, Majorana' , selection, 'hnl_m_8_v2_2p0Em05_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_2em05'  , 'xs_w_v2_2em05'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=3.0 10^{-5}, Majorana' , selection, 'hnl_m_8_v2_3p0Em05_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_3em05'  , 'xs_w_v2_3em05'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=4.0 10^{-5}, Majorana' , selection, 'hnl_m_8_v2_4p0Em05_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_4em05'  , 'xs_w_v2_4em05'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=5.0 10^{-5}, Majorana' , selection, 'hnl_m_8_v2_5p0Em05_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_5em05'  , 'xs_w_v2_5em05'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=7.0 10^{-5}, Majorana' , selection, 'hnl_m_8_v2_7p0Em05_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_7em05'  , 'xs_w_v2_7em05'  ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=1.0 10^{-4}, Majorana' , selection, 'hnl_m_8_v2_1p0Em04_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_0.0001' , 'xs_w_v2_0.0001' ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=2.0 10^{-4}, Majorana' , selection, 'hnl_m_8_v2_2p0Em04_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_0.0002' , 'xs_w_v2_0.0002' ]),
        Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO' , 'm=8 GeV, |V|^{2}=2.5 10^{-4}, Majorana' , selection, 'hnl_m_8_v2_2p5Em04_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False, extra_signal_weights=['ctau_w_v2_0.00025', 'xs_w_v2_0.00025']),

        ########## M = 10
        Sample('HN3L_M_10_V_0p000547722557505_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=3.0 10^{-7}, Majorana', selection, 'hnl_m_10_v2_3p0Em07_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.001237 , toplot=False),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=5.7 10^{-7}, Majorana', selection, 'hnl_m_10_v2_5p7Em07_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False),
        Sample('HN3L_M_10_V_0p001_mu_massiveAndCKM_LO'            , 'm=10 GeV, |V|^{2}=1.0 10^{-6}, Majorana', selection, 'hnl_m_10_v2_1p0Em06_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.004121 , toplot=True ),
        # weighted samples
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=1.0 10^{-9}, Majorana', selection, 'hnl_m_10_v2_1p0Em09_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_1em09'  , 'xs_w_v2_1em09'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=5.0 10^{-9}, Majorana', selection, 'hnl_m_10_v2_5p0Em09_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_5em09'  , 'xs_w_v2_5em09'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=1.0 10^{-8}, Majorana', selection, 'hnl_m_10_v2_1p0Em08_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_1em08'  , 'xs_w_v2_1em08'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=5.0 10^{-8}, Majorana', selection, 'hnl_m_10_v2_5p0Em08_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_5em08'  , 'xs_w_v2_5em08'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=1.0 10^{-7}, Majorana', selection, 'hnl_m_10_v2_1p0Em07_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_1em07'  , 'xs_w_v2_1em07'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=5.0 10^{-7}, Majorana', selection, 'hnl_m_10_v2_5p0Em07_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_5em07'  , 'xs_w_v2_5em07'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=5.0 10^{-6}, Majorana', selection, 'hnl_m_10_v2_5p0Em06_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_5em06'  , 'xs_w_v2_5em06'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=6.0 10^{-6}, Majorana', selection, 'hnl_m_10_v2_6p0Em06_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_6em06'  , 'xs_w_v2_6em06'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=8.0 10^{-6}, Majorana', selection, 'hnl_m_10_v2_8p0Em06_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_8em06'  , 'xs_w_v2_8em06'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=1.0 10^{-5}, Majorana', selection, 'hnl_m_10_v2_1p0Em05_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_1em05'  , 'xs_w_v2_1em05'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=2.0 10^{-5}, Majorana', selection, 'hnl_m_10_v2_2p0Em05_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_2em05'  , 'xs_w_v2_2em05'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=3.0 10^{-5}, Majorana', selection, 'hnl_m_10_v2_3p0Em05_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_3em05'  , 'xs_w_v2_3em05'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=4.0 10^{-5}, Majorana', selection, 'hnl_m_10_v2_4p0Em05_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_4em05'  , 'xs_w_v2_4em05'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=5.0 10^{-5}, Majorana', selection, 'hnl_m_10_v2_5p0Em05_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_5em05'  , 'xs_w_v2_5em05'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=7.0 10^{-5}, Majorana', selection, 'hnl_m_10_v2_7p0Em05_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_7em05'  , 'xs_w_v2_7em05'  ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=1.0 10^{-4}, Majorana', selection, 'hnl_m_10_v2_1p0Em04_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_0.0001' , 'xs_w_v2_0.0001' ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=2.0 10^{-4}, Majorana', selection, 'hnl_m_10_v2_2p0Em04_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_0.0002' , 'xs_w_v2_0.0002' ]),
        Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO', 'm=10 GeV, |V|^{2}=2.5 10^{-4}, Majorana', selection, 'hnl_m_10_v2_2p5Em04_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False, extra_signal_weights=['ctau_w_v2_0.00025', 'xs_w_v2_0.00025']),
    ]
    
    return signal



##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
# FULL LIST
# 
# def get_signal_samples(basedir, postfix, selection):
#     signal = [ 
#         Sample('HN3L_M_1_V_0p0949736805647_mu_massiveAndCKM_LO'             , 'm=1 GeV, |V|^{2}=9.0 10^{-3}, Majorana' , selection, 'hnl_m_1_v2_9p0Em03_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  38.67    , toplot=False),
#         Sample('HN3L_M_1_V_0p13416407865_mu_Dirac_massiveAndCKM_LO'         , 'm=1 GeV, |V|^{2}=1.8 10^{-2}, Dirac'    , selection, 'hnl_m_1_v2_1p8Em02_dirac'    , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  44.46    , toplot=False),
#         Sample('HN3L_M_1_V_0p13416407865_mu_Dirac_cc_massiveAndCKM_LO'      , 'm=1 GeV, |V|^{2}=1.8 10^{-2}, Dirac cc' , selection, 'hnl_m_1_v2_1p8Em02_dirac_cc' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  33.21    , toplot=False),
# #         Sample('HN3L_M_1_V_0p212367605816_mu_massiveAndCKM_LO'              , 'm=1 GeV, |V|^{2}=4.5 10^{-2}, Majorana' , selection, 'hnl_m_1_v2_4p5Em02_majorana' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  193.3    , toplot=False),
#         Sample('HN3L_M_1_V_0p300333148354_mu_Dirac_massiveAndCKM_LO'        , 'm=1 GeV, |V|^{2}=9.0 10^{-2}, Dirac'    , selection, 'hnl_m_1_v2_9p0Em02_dirac'    , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  222.7    , toplot=False),
#         Sample('HN3L_M_1_V_0p300333148354_mu_Dirac_cc_massiveAndCKM_LO'     , 'm=1 GeV, |V|^{2}=9.0 10^{-2}, Dirac cc' , selection, 'hnl_m_1_v2_9p0Em02_dirac_cc' , 'darkorange' ,10, basedir, postfix, False, True, False, 1.,  166.9    , toplot=False),
#         Sample('HN3L_M_2_V_0p0110905365064_mu_massiveAndCKM_LO'             , 'm=2 GeV, |V|^{2}=1.2 10^{-4}, Majorana' , selection, 'hnl_m_2_v2_1p2Em04_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.5278   , toplot=True ),
#         Sample('HN3L_M_2_V_0p0137840487521_mu_Dirac_cc_massiveAndCKM_LO'    , 'm=2 GeV, |V|^{2}=1.9 10^{-4}, Dirac cc' , selection, 'hnl_m_2_v2_1p9Em04_dirac_cc' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.352    , toplot=False),
#         Sample('HN3L_M_2_V_0p0157162336455_mu_Dirac_massiveAndCKM_LO'       , 'm=2 GeV, |V|^{2}=2.5 10^{-4}, Dirac'    , selection, 'hnl_m_2_v2_2p5Em04_dirac'    , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.6117   , toplot=False),
#         Sample('HN3L_M_2_V_0p0157162336455_mu_Dirac_cc_massiveAndCKM_LO'    , 'm=2 GeV, |V|^{2}=2.5 10^{-4}, Dirac cc' , selection, 'hnl_m_2_v2_2p5Em04_dirac_cc' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  0.458    , toplot=False),
#         Sample('HN3L_M_2_V_0p0248394846967_mu_massiveAndCKM_LO'             , 'm=2 GeV, |V|^{2}=6.2 10^{-4}, Majorana' , selection, 'hnl_m_2_v2_6p2Em04_majorana' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  2.647    , toplot=False),
#         Sample('HN3L_M_2_V_0p0307896086367_mu_Dirac_cc_massiveAndCKM_LO'    , 'm=2 GeV, |V|^{2}=9.5 10^{-4}, Dirac cc' , selection, 'hnl_m_2_v2_9p5Em04_dirac_cc' , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  1.75     , toplot=False),
#         Sample('HN3L_M_2_V_0p0350713558335_mu_Dirac_massiveAndCKM_LO'       , 'm=2 GeV, |V|^{2}=1.2 10^{-3}, Dirac'    , selection, 'hnl_m_2_v2_1p2Em03_dirac'    , 'forestgreen',10, basedir, postfix, False, True, False, 1.,  3.047    , toplot=False),
#         Sample('HN3L_M_3_V_0p00443846820423_mu_Dirac_cc_massiveAndCKM_LO'   , 'm=3 GeV, |V|^{2}=2.0 10^{-5}, Dirac cc' , selection, 'hnl_m_3_v2_2p0Em05_dirac_cc' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.03459  , toplot=True ),
#         Sample('HN3L_M_3_V_0p00707813534767_mu_massiveAndCKM_LO'            , 'm=3 GeV, |V|^{2}=5.0 10^{-5}, Majorana' , selection, 'hnl_m_3_v2_5p0Em05_majorana' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.2014   , toplot=False),
#         Sample('HN3L_M_3_V_0p01_mu_Dirac_massiveAndCKM_LO'                  , 'm=3 GeV, |V|^{2}=1.0 10^{-4}, Dirac'    , selection, 'hnl_m_3_v2_1p0Em04_dirac'    , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.233    , toplot=False),
#         Sample('HN3L_M_3_V_0p0140356688476_mu_Dirac_cc_massiveAndCKM_LO'    , 'm=3 GeV, |V|^{2}=2.0 10^{-4}, Dirac cc' , selection, 'hnl_m_3_v2_2p0Em04_dirac_cc' , 'firebrick'  ,10, basedir, postfix, False, True, False, 1.,  0.3434   , toplot=False),
#         Sample('HN3L_M_4_V_0p00183575597507_mu_Dirac_cc_massiveAndCKM_LO'   , 'm=4 GeV, |V|^{2}=3.4 10^{-6}, Dirac cc' , selection, 'hnl_m_4_v2_3p4Em06_dirac_cc' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.005818 , toplot=False),
#         Sample('HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO'            , 'm=4 GeV, |V|^{2}=8.4 10^{-6}, Majorana' , selection, 'hnl_m_4_v2_8p4Em06_majorana' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.0335   , toplot=False),
#         Sample('HN3L_M_4_V_0p00354964786986_mu_Dirac_cc_massiveAndCKM_LO'   , 'm=4 GeV, |V|^{2}=1.3 10^{-5}, Dirac cc' , selection, 'hnl_m_4_v2_1p3Em05_dirac_cc' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.02173  , toplot=False),
#         Sample('HN3L_M_4_V_0p00411096095822_mu_Dirac_massiveAndCKM_LO'      , 'm=4 GeV, |V|^{2}=1.7 10^{-5}, Dirac'    , selection, 'hnl_m_4_v2_1p7Em05_dirac'    , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.03904  , toplot=False),
#         Sample('HN3L_M_4_V_0p0101980390272_mu_Dirac_cc_massiveAndCKM_LO'    , 'm=4 GeV, |V|^{2}=1.0 10^{-4}, Dirac cc' , selection, 'hnl_m_4_v2_1p0Em04_dirac_cc' , 'indigo'     ,10, basedir, postfix, False, True, False, 1.,  0.18     , toplot=False),
#         Sample('HN3L_M_5_V_0p000316227766017_mu_Dirac_massiveAndCKM_LO'     , 'm=5 GeV, |V|^{2}=1.0 10^{-7}, Dirac'    , selection, 'hnl_m_5_v2_1p0Em07_dirac'    , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.0002326, toplot=False),
#         Sample('HN3L_M_5_V_0p000316227766017_mu_massiveAndCKM_LO'           , 'm=5 GeV, |V|^{2}=1.0 10^{-7}, Majorana' , selection, 'hnl_m_5_v2_1p0Em07_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.0003981, toplot=False),
#         Sample('HN3L_M_5_V_0p000547722557505_mu_Dirac_massiveAndCKM_LO'     , 'm=5 GeV, |V|^{2}=3.0 10^{-7}, Dirac'    , selection, 'hnl_m_5_v2_3p0Em07_dirac'    , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.0006979, toplot=False),
#         Sample('HN3L_M_5_V_0p000547722557505_mu_massiveAndCKM_LO'           , 'm=5 GeV, |V|^{2}=3.0 10^{-7}, Majorana' , selection, 'hnl_m_5_v2_3p0Em07_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.001194 , toplot=False),
#         Sample('HN3L_M_5_V_0p000920326029187_mu_Dirac_cc_massiveAndCKM_LO'  , 'm=5 GeV, |V|^{2}=8.5 10^{-7}, Dirac cc' , selection, 'hnl_m_5_v2_8p5Em07_dirac_cc' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.001473 , toplot=False),
# #         Sample('HN3L_M_5_V_0p001_mu_Dirac_massiveAndCKM_LO'                 , 'm=5 GeV, |V|^{2}=1.0 10^{-6}, Dirac'    , selection, 'hnl_m_5_v2_1p0Em06_dirac'    , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.002324 , toplot=False),
# #         Sample('HN3L_M_5_V_0p001_mu_massiveAndCKM_LO'                       , 'm=5 GeV, |V|^{2}=1.0 10^{-6}, Majorana' , selection, 'hnl_m_5_v2_1p0Em06_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.003977 , toplot=False),
#         Sample('HN3L_M_5_V_0p00145602197786_mu_massiveAndCKM_LO'            , 'm=5 GeV, |V|^{2}=2.1 10^{-6}, Majorana' , selection, 'hnl_m_5_v2_2p1Em06_majorana' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.008434 , toplot=True ),
#         Sample('HN3L_M_5_V_0p00178044938148_mu_Dirac_cc_massiveAndCKM_LO'   , 'm=5 GeV, |V|^{2}=3.2 10^{-6}, Dirac cc' , selection, 'hnl_m_5_v2_3p2Em06_dirac_cc' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.005518 , toplot=False),
#         Sample('HN3L_M_5_V_0p00205669638012_mu_Dirac_massiveAndCKM_LO'      , 'm=5 GeV, |V|^{2}=4.2 10^{-6}, Dirac'    , selection, 'hnl_m_5_v2_4p2Em06_dirac'    , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.009836 , toplot=False),
# #         Sample('HN3L_M_5_V_0p0065574385243_mu_Dirac_cc_massiveAndCKM_LO'    , 'm=5 GeV, |V|^{2}=4.3 10^{-5}, Dirac cc' , selection, 'hnl_m_5_v2_4p3Em05_dirac_cc' , 'chocolate'  ,10, basedir, postfix, False, True, False, 1.,  0.07522  , toplot=False),
#         Sample('HN3L_M_6_V_0p000522494019105_mu_Dirac_cc_massiveAndCKM_LO'  , 'm=6 GeV, |V|^{2}=2.7 10^{-7}, Dirac cc' , selection, 'hnl_m_6_v2_2p7Em07_dirac_cc' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.0004745, toplot=False),
#         Sample('HN3L_M_6_V_0p00101488915651_mu_Dirac_cc_massiveAndCKM_LO'   , 'm=6 GeV, |V|^{2}=1.0 10^{-6}, Dirac cc' , selection, 'hnl_m_6_v2_1p0Em06_dirac_cc' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.001795 , toplot=False),
#         Sample('HN3L_M_6_V_0p00202484567313_mu_massiveAndCKM_LO'            , 'm=6 GeV, |V|^{2}=4.1 10^{-6}, Majorana' , selection, 'hnl_m_6_v2_4p1Em06_majorana' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01655  , toplot=False),
#         Sample('HN3L_M_6_V_0p00286356421266_mu_Dirac_massiveAndCKM_LO'      , 'm=6 GeV, |V|^{2}=8.2 10^{-6}, Dirac'    , selection, 'hnl_m_6_v2_8p2Em06_dirac'    , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01926  , toplot=False),
#         Sample('HN3L_M_6_V_0p00299666481275_mu_Dirac_cc_massiveAndCKM_LO'   , 'm=6 GeV, |V|^{2}=9.0 10^{-6}, Dirac cc' , selection, 'hnl_m_6_v2_9p0Em06_dirac_cc' , 'olive'      ,10, basedir, postfix, False, True, False, 1.,  0.01568  , toplot=False),
#         Sample('HN3L_M_8_V_0p000316227766017_mu_Dirac_massiveAndCKM_LO'     , 'm=8 GeV, |V|^{2}=1.0 10^{-7}, Dirac'    , selection, 'hnl_m_8_v2_1p0Em07_dirac'    , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.0002387, toplot=False),
#         Sample('HN3L_M_8_V_0p000415932686862_mu_Dirac_cc_massiveAndCKM_LO'  , 'm=8 GeV, |V|^{2}=1.7 10^{-7}, Dirac cc' , selection, 'hnl_m_8_v2_1p7Em07_dirac_cc' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.0003071, toplot=False),
#         Sample('HN3L_M_8_V_0p000547722557505_mu_Dirac_massiveAndCKM_LO'     , 'm=8 GeV, |V|^{2}=3.0 10^{-7}, Dirac'    , selection, 'hnl_m_8_v2_3p0Em07_dirac'    , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.0007165, toplot=False),
#         Sample('HN3L_M_8_V_0p000547722557505_mu_massiveAndCKM_LO'           , 'm=8 GeV, |V|^{2}=3.0 10^{-7}, Majorana' , selection, 'hnl_m_8_v2_3p0Em07_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.00123  , toplot=False),
#         Sample('HN3L_M_8_V_0p001_mu_Dirac_massiveAndCKM_LO'                 , 'm=8 GeV, |V|^{2}=1.0 10^{-6}, Dirac'    , selection, 'hnl_m_8_v2_1p0Em06_dirac'    , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.002389 , toplot=False),
# #         Sample('HN3L_M_8_V_0p001_mu_massiveAndCKM_LO'                       , 'm=8 GeV, |V|^{2}=1.0 10^{-6}, Majorana' , selection, 'hnl_m_8_v2_1p0Em06_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.004104 , toplot=False),
# #         Sample('HN3L_M_8_V_0p00151327459504_mu_massiveAndCKM_LO'            , 'm=8 GeV, |V|^{2}=2.3 10^{-6}, Majorana' , selection, 'hnl_m_8_v2_2p3Em06_majorana' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.009374 , toplot=False),
# #         Sample('HN3L_M_8_V_0p00214242852856_mu_Dirac_massiveAndCKM_LO'      , 'm=8 GeV, |V|^{2}=4.6 10^{-6}, Dirac'    , selection, 'hnl_m_8_v2_4p6Em06_dirac'    , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.01096  , toplot=False),
#         Sample('HN3L_M_8_V_0p00363318042492_mu_Dirac_cc_massiveAndCKM_LO'   , 'm=8 GeV, |V|^{2}=1.3 10^{-5}, Dirac cc' , selection, 'hnl_m_8_v2_1p3Em05_dirac_cc' , 'darkgray'   ,10, basedir, postfix, False, True, False, 1.,  0.02351  , toplot=False),
#         Sample('HN3L_M_10_V_0p000208566536146_mu_Dirac_cc_massiveAndCKM_LO' , 'm=10 GeV, |V|^{2}=4.3 10^{-8}, Dirac cc', selection, 'hnl_m_10_v2_4p3Em08_dirac_cc', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  7.797e-05, toplot=False),
#         Sample('HN3L_M_10_V_0p000316227766017_mu_Dirac_massiveAndCKM_LO'    , 'm=10 GeV, |V|^{2}=1.0 10^{-7}, Dirac'   , selection, 'hnl_m_10_v2_1p0Em07_dirac'   , 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.0002398, toplot=False),
# #         Sample('HN3L_M_10_V_0p000316227766017_mu_massiveAndCKM_LO'          , 'm=10 GeV, |V|^{2}=1.0 10^{-7}, Majorana', selection, 'hnl_m_10_v2_1p0Em07_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.0004118, toplot=False),
#         Sample('HN3L_M_10_V_0p000547722557505_mu_Dirac_massiveAndCKM_LO'    , 'm=10 GeV, |V|^{2}=3.0 10^{-7}, Dirac'   , selection, 'hnl_m_10_v2_3p0Em07_dirac'   , 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.0007193, toplot=False),
#         Sample('HN3L_M_10_V_0p000547722557505_mu_massiveAndCKM_LO'          , 'm=10 GeV, |V|^{2}=3.0 10^{-7}, Majorana', selection, 'hnl_m_10_v2_3p0Em07_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.001237 , toplot=False),
#         Sample('HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO'          , 'm=10 GeV, |V|^{2}=5.7 10^{-7}, Majorana', selection, 'hnl_m_10_v2_5p7Em07_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002362 , toplot=False),
#         Sample('HN3L_M_10_V_0p001_mu_Dirac_massiveAndCKM_LO'                , 'm=10 GeV, |V|^{2}=1.0 10^{-6}, Dirac'   , selection, 'hnl_m_10_v2_1p0Em06_dirac'   , 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002405 , toplot=False),
#         Sample('HN3L_M_10_V_0p001_mu_massiveAndCKM_LO'                      , 'm=10 GeV, |V|^{2}=1.0 10^{-6}, Majorana', selection, 'hnl_m_10_v2_1p0Em06_majorana', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.004121 , toplot=True ),
#         Sample('HN3L_M_10_V_0p00107238052948_mu_Dirac_massiveAndCKM_LO'     , 'm=10 GeV, |V|^{2}=1.2 10^{-6}, Dirac'   , selection, 'hnl_m_10_v2_1p2Em06_dirac'   , 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.002761 , toplot=False),
#         Sample('HN3L_M_10_V_0p00112249721603_mu_Dirac_cc_massiveAndCKM_LO'  , 'm=10 GeV, |V|^{2}=1.3 10^{-6}, Dirac cc', selection, 'hnl_m_10_v2_1p3Em06_dirac_cc', 'teal'       ,10, basedir, postfix, False, True, False, 1.,  0.00227  , toplot=False),
#         Sample('HN3L_M_15_V_0p00003021588986_mu_Dirac_cc_massiveAndCKM_LO'  , 'm=15 GeV, |V|^{2}=9.1E-10}, Dirac cc', selection, 'hnl_m_15_v2_9p1Em10_dirac_cc', 'gold'       ,10, basedir, postfix, False, True, False, 1.,  1.606e-06, toplot=False),
#         Sample('HN3L_M_15_V_0p00006760177512_mu_Dirac_cc_massiveAndCKM_LO'  , 'm=15 GeV, |V|^{2}=4.6 10^{-9}, Dirac cc', selection, 'hnl_m_15_v2_4p6Em09_dirac_cc', 'gold'       ,10, basedir, postfix, False, True, False, 1.,  8.068e-06, toplot=False),
#         Sample('HN3L_M_20_V_0p00001224744871_mu_Dirac_cc_massiveAndCKM_LO'  , 'm=20 GeV, |V|^{2}=1.5E-10}, Dirac cc', selection, 'hnl_m_20_v2_1p5Em10_dirac_cc', 'crimson'    ,10, basedir, postfix, False, True, False, 1.,  2.524e-07, toplot=False),
#         Sample('HN3L_M_20_V_0p00002734958866_mu_Dirac_cc_massiveAndCKM_LO'  , 'm=20 GeV, |V|^{2}=7.5E-10}, Dirac cc', selection, 'hnl_m_20_v2_7p5Em10_dirac_cc', 'crimson'    ,10, basedir, postfix, False, True, False, 1.,  1.246e-06, toplot=False),
#         Sample('HN3L_M_20_V_0p001_mu_Dirac_massiveAndCKM_LO'                , 'm=20 GeV, |V|^{2}=1.0 10^{-6}, Dirac'   , selection, 'hnl_m_20_v2_1p0Em06_dirac'   , 'crimson'    ,10, basedir, postfix, False, True, False, 1.,  0.00224  , toplot=False),
#         Sample('HN3L_M_20_V_0p001_mu_massiveAndCKM_LO'                      , 'm=20 GeV, |V|^{2}=1.0 10^{-6}, Majorana', selection, 'hnl_m_20_v2_1p0Em06_majorana', 'crimson'    ,10, basedir, postfix, False, True, False, 1.,  0.003856 , toplot=False),
#         Sample('HN3L_M_20_V_0p00316227766017_mu_Dirac_massiveAndCKM_LO'     , 'm=20 GeV, |V|^{2}=1.0 10^{-5}, Dirac'   , selection, 'hnl_m_20_v2_1p0Em05_dirac'   , 'crimson'    ,10, basedir, postfix, False, True, False, 1.,  0.02239  , toplot=False),
#         Sample('HN3L_M_20_V_0p00316227766017_mu_massiveAndCKM_LO'           , 'm=20 GeV, |V|^{2}=1.0 10^{-5}, Majorana', selection, 'hnl_m_20_v2_1p0Em05_majorana', 'crimson'    ,10, basedir, postfix, False, True, False, 1.,  0.03854  , toplot=False),
#     ]
#     
#     return signal
