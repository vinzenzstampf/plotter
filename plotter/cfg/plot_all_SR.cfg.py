from os import environ as env
from collections import OrderedDict
from plotter.plotter import Plotter
from plotter.selections import Selections
from plotter.utils import set_paths, save_plotter_and_selections

cuts = OrderedDict()
selection = OrderedDict()

for ch in ['mmm', 'mem', 'eem', 'eee']:
    cuts[ch] = Selections(ch)

selection['eee'] = [ 
    cuts['eee'].selections['pt_iso'], 
    cuts['eee'].selections['baseline'], 
    cuts['eee'].selections['vetoes_12_OS'], 
    cuts['eee'].selections['vetoes_01_OS'], 
    cuts['eee'].selections['vetoes_02_OS'],
    cuts['eee'].selections['signal_region'], 
#     cuts.selections['sideband'], 

    'l1_pt>7',
    'l2_pt>7',
#     'hnl_2d_disp_sig>20',
    'hnl_pt_12>15',
    'sv_cos>0.99',
    'sv_prob>0.001',
    'l0_pt>32',
    'abs(l1_dz)<10',
    'abs(l2_dz)<10',
    'l0_reliso_rho_03<0.1',
]

selection['eem_os'] = [ 
    cuts['eem'].selections['pt_iso'], 
    cuts['eem'].selections['baseline'], 
    cuts['eem'].selections['vetoes_01_OS'],
    'l0_q!=l1_q', 
#     cuts.selections['sideband'], 
    cuts['eem'].selections['signal_region'], 

    'l1_pt>7',
#     'hnl_2d_disp_sig>20',
    'hnl_pt_12>15',
    'sv_cos>0.99',
    'sv_prob>0.001',
    'l0_reliso_rho_03<0.1',
    'l0_pt>32',
    'abs(l1_dz)<10',
    'abs(l2_dz)<10',
]

selection['eem_ss'] = [ 
    cuts['eem'].selections['pt_iso'], 
    cuts['eem'].selections['baseline'], 
    'l0_q==l1_q', 
#     cuts.selections['sideband'], 
    cuts['eem'].selections['signal_region'], 

    'l1_pt>7',
#     'hnl_2d_disp_sig>20',
    'hnl_pt_12>15',
    'sv_cos>0.99',
    'sv_prob>0.001',
    'l0_reliso_rho_03<0.1',
    'l0_pt>32',
    'abs(l1_dz)<10',
    'abs(l2_dz)<10',
]

selection['mem_os'] = [ 
    cuts['mem'].selections['pt_iso'], 
    cuts['mem'].selections['baseline'], 
    cuts['mem'].selections['vetoes_02_OS'],
    'l0_q!=l2_q', 
#     cuts.selections['sideband'], 
    cuts['mem'].selections['signal_region'], 

    'l1_pt>7',
#     'hnl_2d_disp_sig>20',
    'hnl_pt_12>15',
    'sv_cos>0.99',
    'sv_prob>0.001',
    'l0_reliso_rho_03<0.1',
    'l0_pt>25',
    'abs(l1_dz)<10',
    'abs(l2_dz)<10',
]

selection['mem_ss'] = [ 
    cuts['mem'].selections['pt_iso'], 
    cuts['mem'].selections['baseline'], 
    'l0_q==l2_q', 
#     cuts.selections['sideband'], 
    cuts['mem'].selections['signal_region'], 

    'l1_pt>7',
#     'hnl_2d_disp_sig>20',
    'hnl_pt_12>15',
    'sv_cos>0.99',
    'sv_prob>0.001',
    'l0_reliso_rho_03<0.1',
    'l0_pt>25',
    'abs(l1_dz)<10',
    'abs(l2_dz)<10',
]

selection['mmm'] = [ 
    cuts['mmm'].selections['pt_iso'], 
    cuts['mmm'].selections['baseline'], 
    cuts['mmm'].selections['vetoes_12_OS'], 
    cuts['mmm'].selections['vetoes_01_OS'], 
    cuts['mmm'].selections['vetoes_02_OS'],
    cuts['mmm'].selections['signal_region'], 

    'hnl_pt_12>15',
    'sv_cos>0.99',
    'sv_prob>0.001',
    'l0_reliso_rho_03<0.1',
    'l0_pt>25',
    'abs(l1_dz)<10',
    'abs(l2_dz)<10',
]

# extra selection to be applied on variables that don't exist
# in the root tree but they're created for the pandas dataset
# pandas_selection = 'hnl_2d_disp_sig_alt>20'
pandas_selection = '(hnl_2d_disp_sig_alt > 20 & sv_covxx > 0 & sv_covyy > 0 & sv_covzz > 0)' # workaround bug w/ negativ sv_cov_ii entries


if __name__ == '__main__':
    for ch in ['mmm', 'mem_os', 'mem_ss', 'eem_os', 'eem_ss', 'eee']:

        selection_mc = selection[ch] + [cuts[ch[:3]].selections['is_prompt_lepton']]
        selection_tight = cuts[ch[:3]].selections_pd['tight']

        set_paths(ch, 2016) 
        plotter16 = Plotter(
                   channel          = ch,
                   year             = 2016,
                   base_dir         = env['NTUPLE_DIR'],
                   post_fix         = 'HNLTreeProducer/tree.root', # 'HNLTreeProducer_%s/tree.root' %ch,
                   selection_data   = selection[ch],
                   selection_mc     = selection_mc,
                   selection_tight  = selection_tight,
                   pandas_selection = pandas_selection,
                   lumi             = 35900.,
                   # model            = env['NN_DIR'] + '/all_2016_channels_200117_12h_55m/net_model_weighted.h5', 
                   # transformation   = env['NN_DIR'] + '/all_2016_channels_200117_12h_55m/input_tranformation_weighted.pck',
                   # features         = env['NN_DIR'] + '/all_2016_channels_200117_12h_55m/input_features.pck',
                   model            = env['NN_DIR'] + '/all_2016_channels_200210_10h_30m/net_model_weighted.h5', 
                   transformation   = env['NN_DIR'] + '/all_2016_channels_200210_10h_30m/input_tranformation_weighted.pck',
                   features         = env['NN_DIR'] + '/all_2016_channels_200210_10h_30m/input_features.pck',
                   process_signals  = True, # switch off for control regions
                   mini_signals     = False, # process only the signals that you'll plot
                   plot_signals     = True, 
                   blinded          = True,
                   datacards        = ['hnl_m_12_lxy_lt_0p5', 'hnl_m_12_lxy_0p5_to_1p5', 'hnl_m_12_lxy_1p5_to_4p0', 'hnl_m_12_lxy_mt_4p0'], # FIXME! improve this to accept wildcards / regex
                   )
        plotter16.plot()
        save_plotter_and_selections(plotter16, selection[ch], selection_mc, selection_tight)

        set_paths(ch, 2017) 
        plotter17 = Plotter (
                   channel          = ch,
                   year             = 2017,
                   base_dir         = env['NTUPLE_DIR'],
                   post_fix         = 'HNLTreeProducer/tree.root', # 'HNLTreeProducer_%s/tree.root' %ch,
                   selection_data   = selection[ch],
                   selection_mc     = selection_mc,
                   selection_tight  = selection_tight,
                   pandas_selection = pandas_selection,
                   lumi             = 41500.,
                   # model            = env['NN_DIR'] + '/all_2017_channels_200117_12h_44m/net_model_weighted.h5', 
                   # transformation   = env['NN_DIR'] + '/all_2017_channels_200117_12h_44m/input_tranformation_weighted.pck',
                   # features         = env['NN_DIR'] + '/all_2017_channels_200117_12h_44m/input_features.pck',
                   model            = env['NN_DIR'] + '/all_2017_channels_200210_10h_38m/net_model_weighted.h5', 
                   transformation   = env['NN_DIR'] + '/all_2017_channels_200210_10h_38m/input_tranformation_weighted.pck',
                   features         = env['NN_DIR'] + '/all_2017_channels_200210_10h_38m/input_features.pck',
                   process_signals  = True, # switch off for control regions
                   mini_signals     = False, # process only the signals that you'll plot
                   plot_signals     = True, 
                   blinded          = True,
                   datacards        = ['hnl_m_12_lxy_lt_0p5', 'hnl_m_12_lxy_0p5_to_1p5', 'hnl_m_12_lxy_1p5_to_4p0', 'hnl_m_12_lxy_mt_4p0'], # FIXME! improve this to accept wildcards / regex
                   )
        plotter17.plot()
        save_plotter_and_selections(plotter17, selection[ch], selection_mc, selection_tight)

        set_paths(ch, 2018) 
        plotter18 = Plotter (
                   channel          = ch,
                   year             = 2018,
                   base_dir         = env['NTUPLE_DIR'],
                   post_fix         = 'HNLTreeProducer/tree.root', # 'HNLTreeProducer_%s/tree.root' %ch,
                   selection_data   = selection[ch],
                   selection_mc     = selection_mc,
                   selection_tight  = selection_tight,
                   pandas_selection = pandas_selection,
                   lumi             = 59700.,
                   # model            = env['NN_DIR'] + '/all_2018_channels_200117_11h_43m/net_model_weighted.h5',             # plots from 1/17/20 
                   # transformation   = env['NN_DIR'] + '/all_2018_channels_200117_11h_43m/input_tranformation_weighted.pck',
                   # features         = env['NN_DIR'] + '/all_2018_channels_200117_11h_43m/input_features.pck',
                   # model            = env['NN_DIR'] + '/fixed_from_R/all_channels_191126_9h_45m/net_model_weighted.h5', 
                   # transformation   = env['NN_DIR'] + '/fixed_from_R/all_channels_191126_9h_45m/input_tranformation_weighted.pck',
                   # features         = env['NN_DIR'] + '/fixed_from_R/all_channels_191126_9h_45m/input_features.pck',
                   model            = env['NN_DIR'] + '/all_2018_channels_200210_10h_44m/net_model_weighted.h5',             # plots from 1/17/20 
                   transformation   = env['NN_DIR'] + '/all_2018_channels_200210_10h_44m/input_tranformation_weighted.pck',
                   features         = env['NN_DIR'] + '/all_2018_channels_200210_10h_44m/input_features.pck',
                   process_signals  = True, # switch off for control regions
                   mini_signals     = False, # process only the signals that you'll plot
                   plot_signals     = True, 
                   blinded          = True,
                   datacards        = ['hnl_m_12_lxy_lt_0p5', 'hnl_m_12_lxy_0p5_to_1p5', 'hnl_m_12_lxy_1p5_to_4p0', 'hnl_m_12_lxy_mt_4p0'], # FIXME! improve this to accept wildcards / regex
                   )
        plotter18.plot()
        save_plotter_and_selections(plotter18, selection[ch], selection_mc, selection_tight)
        
        pass
