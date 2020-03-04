import ROOT as rt

fin_eem = '/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_4_V_0p00290516780927_e_massiveAndCKM_LO/HNLTreeProducer_eem/tree.root'

# fin_eem = '/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_10_V_0p000756967634711_e_massiveAndCKM_LO/HNLTreeProducer_eem/tree.root'


tf_in_eem = rt.TFile(fin_eem)

tree_eem = tf_in_eem.Get('tree')

tree_eem.SetScanField(0)

selection_data_eem_os = [
     'l0_pt > 30 & l2_pt > 5 & l1_pt > 5 & l0_eid_mva_noniso_wp90 == 1 & l1_LooseNoIso == 1 & l2_Medium == 1',
     'abs(l0_eta) < 2.4 & abs(l0_dxy) < 0.05 & abs(l0_dz) < 0.1 & l0_reliso_rho_03 < 0.1 & abs(l1_eta) < 2.4 & l1_reliso_rho_03 < 10 & abs(l2_eta) < 2.4 & l2_reliso_rho_03 < 10 & hnl_q_12 == 0 & nbj == 0 & hnl_dr_12 < 1. & hnl_m_12 < 12 & sv_cos > 0.9 & abs(hnl_dphi_01)>1. & abs(hnl_dphi_02)>1. & abs(l1_dxy) > 0.01 & abs(l2_dxy) > 0.01',
    '!(hnl_q_01==0 & abs(hnl_m_01-91.1876) < 10) & !(hnl_q_01==0 & abs(hnl_m_01- 9.4603) < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-10.0233) < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-10.3552) < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-3.0969)  < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-3.6861)  < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-0.7827)  < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-1.0190)  < 0.08)',
    'l0_q!=l1_q',
    '(hnl_w_vis_m > 50. & hnl_w_vis_m < 80.)',
    'l1_pt>7',
    'hnl_pt_12>15',
    'sv_cos>0.99',
    'sv_prob>0.001',
    'l0_reliso_rho_03<0.1',
    'l0_pt>32', # 2018!!
    'abs(l1_dz)<10',
    'abs(l2_dz)<10',
    'l1_reliso_rho_03 < 0.2 & l2_reliso_rho_03 < 0.2'
 ]

selection_data_eem_os_full = ' & '.join(selection_data_eem_os)

tree_eem.Scan("run:lumi:event:l0_pdgid:l0_pt:l1_pdgid:l1_pt:abs(l1_dxy):l2_pdgid:l2_pt:abs(l2_dxy):hnl_m_12:hnl_2d_disp", 
              selection_data_eem_os_full, 
              "precision=4 ")


to_check_martina_doesnt_have = [
'run=10 & lumi = 1 & event = 740',
'run=102 & lumi = 1 & event = 470',
'run=103 & lumi = 1 & event = 261',
'run=103 & lumi = 1 & event = 830',
'run=103 & lumi = 1 & event = 939',
'run=104 & lumi = 1 & event = 194',
'run=106 & lumi = 1 & event = 790',
'run=110 & lumi = 1 & event = 853',
'run=113 & lumi = 1 & event = 354',
'run=114 & lumi = 1 & event = 503',
'run=120 & lumi = 1 & event = 751',
'run=121 & lumi = 1 & event = 708',
'run=126 & lumi = 1 & event = 925',
'run=128 & lumi = 1 & event = 556',
'run==129 & lumi == 1 & event == 759',
'run==137 & lumi == 1 & event == 212',
'run==137 & lumi == 1 & event == 461',
'run==138 & lumi == 1 & event == 872',
'run==139 & lumi == 1 & event == 838',
'run==141 & lumi == 1 & event == 183',
'run==147 & lumi == 1 & event == 629',
'run==152 & lumi == 1 & event == 383',
'run==157 & lumi == 1 & event == 444',
'run==161 & lumi == 1 & event == 194',
'run==168 & lumi == 1 & event == 230',
'run==17 & lumi == 1 & event == 49',
'run==175 & lumi == 1 & event == 919',
'run==182 & lumi == 1 & event == 880',
'run==19 & lumi == 1 & event == 180',
'run==195 & lumi == 1 & event == 455',
'run==202 & lumi == 1 & event == 251',
'run==202 & lumi == 1 & event == 462',
'run==205 & lumi == 1 & event == 715',
'run==220 & lumi == 1 & event == 707',
'run==223 & lumi == 1 & event == 282',
'run==223 & lumi == 1 & event == 363',
'run==223 & lumi == 1 & event == 437',
'run==231 & lumi == 1 & event == 304',
'run==233 & lumi == 1 & event == 196',
'run==243 & lumi == 1 & event == 96',
'run==249 & lumi == 1 & event == 878',
'run==3 & lumi == 1 & event == 624',
'run==30 & lumi == 1 & event == 304',
'run==33 & lumi == 1 & event == 823',
'run==37 & lumi == 1 & event == 889',
'run==39 & lumi == 1 & event == 285',
'run==4 & lumi == 1 & event == 155',
'run==4 & lumi == 1 & event == 452',
'run==43 & lumi == 1 & event == 741',
'run==5 & lumi == 1 & event == 859',
'run==50 & lumi == 1 & event == 9',
'run==60 & lumi == 1 & event == 314',
'run==70 & lumi == 1 & event == 634',
'run==72 & lumi == 1 & event == 353',
'run==73 & lumi == 1 & event == 313',
'run==78 & lumi == 1 & event == 441',
'run==80 & lumi == 1 & event == 133',
'run==87 & lumi == 1 & event == 269',
'run==98 & lumi == 1 & event == 731]',
]

to_check_i_dont_have = [
'run==101 & lumi == 1 & event == 387',
'run==101 & lumi == 1 & event == 881',
'run==109 & lumi == 1 & event == 915',
'run==11  & lumi == 1 & event == 252',
'run==117 & lumi == 1 & event == 959',
'run==12  & lumi == 1 & event == 122',
'run==133 & lumi == 1 & event == 27',
'run==133 & lumi == 1 & event == 767',
'run==136 & lumi == 1 & event == 810',
'run==139 & lumi == 1 & event == 908',
'run==152 & lumi == 1 & event == 493',
'run==154 & lumi == 1 & event == 60',
'run==155 & lumi == 1 & event == 13',
'run==168 & lumi == 1 & event == 95',
'run==171 & lumi == 1 & event == 649',
'run==18  & lumi == 1 & event == 381',
'run==180 & lumi == 1 & event == 989',
'run==187 & lumi == 1 & event == 168',
'run==188 & lumi == 1 & event == 801',
'run==196 & lumi == 1 & event == 564',
'run==203 & lumi == 1 & event == 58',
'run==209 & lumi == 1 & event == 484',
'run==210 & lumi == 1 & event == 470',
'run==217 & lumi == 1 & event == 761',
'run==244 & lumi == 1 & event == 676',
'run==244 & lumi == 1 & event == 751',
'run==59  & lumi == 1 & event == 874',
'run==71  & lumi == 1 & event == 41',
'run==86  & lumi == 1 & event == 710',
'run==96  & lumi == 1 & event == 234',
'run==98  & lumi == 1 & event == 115',
]




from collections import OrderedDict
check = OrderedDict()

# for i in selection_data_eem_os + ['l1_reliso_rho_03 < 0.2', 'l2_reliso_rho_03 < 0.2', 'l1_LooseNoIso']:
for i in ['l0_pt > 30', 'l2_pt > 5', 'l1_pt > 5', 'l0_eid_mva_noniso_wp90 == 1', 'l1_LooseNoIso == 1', 'l2_Medium == 1' ,' l1_LooseNoIso']:
    count_not_found =0
    count_exists    =0
    # i += '| l0_reliso_rho_03 > 0.1'
    # i += '& l1_LooseNoIso'
    for iev in to_check_i_dont_have:
        check [iev] = tree_eem.GetEntries(iev) # all found
        check [iev] = tree_eem.GetEntries(iev + ' & ' + i) # all found
        print(iev, check[iev])
        if check[iev] == 0: count_not_found += 1
        if check[iev] == 1: count_exists    += 1

    print(i)
    print('not found: {nf}, found: {ex} \n'.format(nf=count_not_found, ex=count_exists))


# for iev in to_check_i_dont_have:
    # tree_mem.Scan("run:lumi:event:l0_pdgid:l0_pt:l2_pdgid:l2_pt:abs(l2_dxy):l2_reliso_rho_03:l1_pdgid:l1_pt:abs(l1_dxy):l1_reliso_rho_03:hnl_m_12:hnl_2d_disp", 
                  # iev + ' & ' + selection_data_mem_ss_full, 
                  # "precision=4 ")
        # print(iev, check[iev])


