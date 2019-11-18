from plotter import Plotter
from selections import Selections
from utils import set_paths
from os import environ as env

ch = 'mmm'

set_paths(ch)
cuts = Selections(ch)

# regular
plotter = Plotter (channel         = ch,
                   base_dir        = env['BASE_DIR'],
                   post_fix        = 'HNLTreeProducer_%s/tree.root' %ch,

                   selection_data  = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['baseline'], cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'], 
                                                  cuts.selections['vetoes_02_OS'], ]),

                   selection_mc    = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['baseline'], cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'], 
                                                  cuts.selections['vetoes_02_OS'], cuts.selections['is_prompt_lepton'] ]),

                   selection_tight = cuts.selections_pd['tight'],

                   lumi            = 59700.,
                   model           = env['NN_DIR'] + '/12Nov19_v0/net_model_weighted.h5', 
                   transformation  = env['NN_DIR'] + '/12Nov19_v0/input_tranformation_weighted.pck',
                   features        = env['NN_DIR'] + '/12Nov19_v0/input_features.pck',
                   plot_signals    = True,
                   blinded         = True,
                   )
# plotter.plot()

# for LLP talk: check LNT and T distros for data
plotter_llp_v0 = Plotter (channel         = ch,
                   base_dir        = env['BASE_DIR'],
                   post_fix        = 'HNLTreeProducer_%s/tree.root' %ch,

                   # selection_data  = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['baseline'], cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'], 
                                                  # cuts.selections['vetoes_02_OS'], ]),

                   selection_data  = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['SR_sb_no_dxy'], ]),

                   selection_mc    = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['SR_sb_no_dxy'], cuts.selections['is_prompt_lepton'] ]),

                   selection_tight = cuts.selections_pd['tight'],

                   lumi            = 59700.,
                   model           = env['NN_DIR'] + '/12Nov19_v0/net_model_weighted.h5', 
                   transformation  = env['NN_DIR'] + '/12Nov19_v0/input_tranformation_weighted.pck',
                   features        = env['NN_DIR'] + '/12Nov19_v0/input_features.pck',
                   plot_signals    = True,
                   blinded         = True,
                   )

# plotter_llp_v0.plot()

plotter_llp_v1 = Plotter (channel         = ch,
                   base_dir        = env['BASE_DIR'],
                   post_fix        = 'HNLTreeProducer_%s/tree.root' %ch,

                   # selection_data  = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['baseline'], cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'], 
                                                  # cuts.selections['vetoes_02_OS'], ]),

                   selection_data  = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['SR_sb_no_dxy'], cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'],
                                                  cuts.selections['vetoes_02_OS'] ]),

                   selection_mc    = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['SR_sb_no_dxy'], cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'],
                                                  cuts.selections['vetoes_02_OS'], cuts.selections['is_prompt_lepton'] ]),

                   selection_tight = cuts.selections_pd['tight'],

                   lumi            = 59700.,
                   model           = env['NN_DIR'] + '/12Nov19_v0/net_model_weighted.h5', 
                   transformation  = env['NN_DIR'] + '/12Nov19_v0/input_tranformation_weighted.pck',
                   features        = env['NN_DIR'] + '/12Nov19_v0/input_features.pck',
                   plot_signals    = True,
                   blinded         = True,
                   )

# plotter_llp_v1.plot()

plotter_llp_v2 = Plotter (channel         = ch,
                   base_dir        = env['BASE_DIR'],
                   post_fix        = 'HNLTreeProducer_%s/tree.root' %ch,

                   # selection_data  = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['baseline'], cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'], 
                                                  # cuts.selections['vetoes_02_OS'], ]),

                   selection_data  = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['SR_sb_w_dxy'], cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'],
                                                  cuts.selections['vetoes_02_OS'] ]),

                   selection_mc    = ' & '.join([ cuts.selections['pt_iso'], cuts.selections['SR_sb_w_dxy'], cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'],
                                                  cuts.selections['vetoes_02_OS'], cuts.selections['is_prompt_lepton'] ]),

                   selection_tight = cuts.selections_pd['tight'],

                   lumi            = 59700.,
                   model           = env['NN_DIR'] + '/191118_14h_45m/net_model_weighted.h5', 
                   transformation  = env['NN_DIR'] + '/191118_14h_45m/input_tranformation_weighted.pck',
                   features        = env['NN_DIR'] + '/191118_14h_45m/input_features.pck',
                   plot_signals    = True,
                   blinded         = True,
                   )

plotter_llp_v2.plot()
