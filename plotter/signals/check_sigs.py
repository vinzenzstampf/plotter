
fs = [
'/Users/cesareborgia/cernbox/hnl/2016/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_eee/tree.root',
'/Users/cesareborgia/cernbox/hnl/2016/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_eem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2016/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_mem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2016/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_mmm/tree.root',
'/Users/cesareborgia/cernbox/hnl/2016/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_eee/tree.root',
'/Users/cesareborgia/cernbox/hnl/2016/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_eem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2016/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_mem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2016/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_mmm/tree.root',
'/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_eee/tree.root',
'/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_eem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_mem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_mmm/tree.root',
'/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_eee/tree.root',
'/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_eem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_mem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_mmm/tree.root',
'/Users/cesareborgia/cernbox/hnl/2018/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_eee/tree.root',
'/Users/cesareborgia/cernbox/hnl/2018/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_eem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2018/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_mem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2018/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_mmm/tree.root',
'/Users/cesareborgia/cernbox/hnl/2018/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_eee/tree.root',
'/Users/cesareborgia/cernbox/hnl/2018/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_eem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2018/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_mem/tree.root',
'/Users/cesareborgia/cernbox/hnl/2018/sig/HN3L_M_10_V_0p000756967634711_mu_massiveAndCKM_LO/HNLTreeProducer_mmm/tree.root',]

import ROOT as rt

for f in fs:
    tf = rt.TFile(f)
    tr = tf.Get('tree')
    print(tr.GetEntries(), f)
