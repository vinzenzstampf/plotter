from os import environ as env
from collections import OrderedDict
from plotter.plotter import Plotter
from plotter.selections import Selections
from plotter.utils import set_paths, save_plotter_and_selections

year = 2017

lumi = -99

if   year == 2018: lumi = 59700.
elif year == 2017: lumi = 41500.
elif year == 2016: lumi = 35900.

assert lumi > 0, 'Wrong Year'

set_paths('mmm', year) #mmm is dummy here FIXME remove ch specifity in utils.py
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
    # cuts.selections['baseline'], 
    cuts['mmm'].selections['baseline_no_dxy'], 
    cuts['mmm'].selections['vetoes_12_OS'], 
    cuts['mmm'].selections['vetoes_01_OS'], 
    cuts['mmm'].selections['vetoes_02_OS'],
    cuts['mmm'].selections['signal_region'], 
#     cuts.selections['sideband'], 

#     'hnl_2d_disp_sig>20',
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
pandas_selection = 'hnl_2d_disp_sig_alt>20'


if __name__ == '__main__':
    for ch in ['mmm', 'mem_os', 'mem_ss', 'eem_os', 'eem_ss', 'eee']:

        selection_mc = selection[ch] + [cuts[ch[:3]].selections['is_prompt_lepton']]
        selection_tight = cuts[ch[:3]].selections_pd['tight']

        plotter16 = Plotter(
                   channel          = ch,
                   year             = year,
                   base_dir         = env['NTUPLE_DIR'],
                   post_fix         = 'HNLTreeProducer/tree.root', # 'HNLTreeProducer_%s/tree.root' %ch,
                   selection_data   = selection[ch],
                   selection_mc     = selection_mc,
                   selection_tight  = selection_tight,
                   pandas_selection = pandas_selection,
                   lumi             = lumi,
                   model            = env['NN_DIR'] + '/all_2016_channels_200117_12h_55m/net_model_weighted.h5', 
                   transformation   = env['NN_DIR'] + '/all_2016_channels_200117_12h_55m/input_tranformation_weighted.pck',
                   features         = env['NN_DIR'] + '/all_2016_channels_200117_12h_55m/input_features.pck',
                   process_signals  = True, # switch off for control regions
                   mini_signals     = False, # process only the signals that you'll plot
                   plot_signals     = True, 
                   blinded          = True,
                   datacards        = ['hnl_m_12_lxy_lt_0p5', 'hnl_m_12_lxy_0p5_to_1p5', 'hnl_m_12_lxy_1p5_to_4p0', 'hnl_m_12_lxy_mt_4p0'], # FIXME! improve this to accept wildcards / regex
                   )

        plotter17 = Plotter (
                   channel          = ch,
                   year             = year,
                   base_dir         = env['NTUPLE_DIR'],
                   post_fix         = 'HNLTreeProducer/tree.root', # 'HNLTreeProducer_%s/tree.root' %ch,
                   selection_data   = selection[ch],
                   selection_mc     = selection_mc,
                   selection_tight  = selection_tight,
                   pandas_selection = pandas_selection,
                   lumi             = lumi,
                   model            = env['NN_DIR'] + '/all_2017_channels_200117_12h_44m/net_model_weighted.h5', 
                   transformation   = env['NN_DIR'] + '/all_2017_channels_200117_12h_44m/input_tranformation_weighted.pck',
                   features         = env['NN_DIR'] + '/all_2017_channels_200117_12h_44m/input_features.pck',
                   process_signals  = True, # switch off for control regions
                   mini_signals     = False, # process only the signals that you'll plot
                   plot_signals     = True, 
                   blinded          = True,
                   datacards        = ['hnl_m_12_lxy_lt_0p5', 'hnl_m_12_lxy_0p5_to_1p5', 'hnl_m_12_lxy_1p5_to_4p0', 'hnl_m_12_lxy_mt_4p0'], # FIXME! improve this to accept wildcards / regex
                   )

        plotter18 = Plotter (
                   channel          = ch,
                   year             = year,
                   base_dir         = env['NTUPLE_DIR'],
                   post_fix         = 'HNLTreeProducer/tree.root', # 'HNLTreeProducer_%s/tree.root' %ch,
                   selection_data   = selection[ch],
                   selection_mc     = selection_mc,
                   selection_tight  = selection_tight,
                   pandas_selection = pandas_selection,
                   lumi             = lumi,
                   model            = env['NN_DIR'] + '/all_2018_channels_200117_11h_43m/net_model_weighted.h5', 
                   transformation   = env['NN_DIR'] + '/all_2018_channels_200117_11h_43m/input_tranformation_weighted.pck',
                   features         = env['NN_DIR'] + '/all_2018_channels_200117_11h_43m/input_features.pck',
                   process_signals  = True, # switch off for control regions
                   mini_signals     = False, # process only the signals that you'll plot
                   plot_signals     = True, 
                   blinded          = True,
                   datacards        = ['hnl_m_12_lxy_lt_0p5', 'hnl_m_12_lxy_0p5_to_1p5', 'hnl_m_12_lxy_1p5_to_4p0', 'hnl_m_12_lxy_mt_4p0'], # FIXME! improve this to accept wildcards / regex
                   )

        if year == 2016:   plotter = plotter16
        elif year == 2017: plotter = plotter17
        elif year == 2018: plotter = plotter18

        set_paths(ch, year) #in order to get the right folder names for the output 

        plotter.plot()
        # save the plotter and all
        save_plotter_and_selections(plotter, selection, selection_mc, selection_tight)
        pass
