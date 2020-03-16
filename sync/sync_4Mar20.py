import ROOT as rt

fin_mem = '/Users/cesareborgia/cernbox/hnl/2017/mc/DYJetsToLL_M50_ext/HNLTreeProducer_mem/tree.root'
fin_eee = '/Users/cesareborgia/cernbox/hnl/2017/mc/DYJetsToLL_M50_ext/HNLTreeProducer_eee/tree.root'


tf_in_mem = rt.TFile(fin_mem)
tf_in_eee = rt.TFile(fin_eee)

tree_mem = tf_in_mem.Get('tree')
tree_eee = tf_in_eee.Get('tree')

tree_mem.SetScanField(0)
tree_eee.SetScanField(0)


selection_data_eee = [
    'l0_pt > 30 & l2_pt > 5 & l1_pt > 5 & l0_eid_mva_noniso_wp90 == 1 & l1_LooseNoIso == 1 & l2_LooseNoIso == 1',
    'abs(l0_eta) < 2.4 & abs(l0_dxy) < 0.05 & abs(l0_dz) < 0.1 & l0_reliso_rho_03 < 0.1 & abs(l1_eta) < 2.4 & l1_reliso_rho_03 < 10 & abs(l2_eta) < 2.4 & l2_reliso_rho_03 < 10 & hnl_q_12 == 0 & nbj == 0 & hnl_dr_12 < 1. & hnl_m_12 < 12 & sv_cos > 0.9 & abs(hnl_dphi_01)>1. & abs(hnl_dphi_02)>1. & abs(l1_dxy) > 0.01 & abs(l2_dxy) > 0.01',
    '!(hnl_2d_disp<1.5 & abs(hnl_m_12-3.0969) < 0.08) & !(hnl_2d_disp<1.5 & abs(hnl_m_12-3.6861) < 0.08) & !(hnl_2d_disp<1.5 & abs(hnl_m_12-0.7827) < 0.08) & !(hnl_2d_disp<1.5 & abs(hnl_m_12-1.0190) < 0.08)',
    '!(hnl_q_01==0 & abs(hnl_m_01-91.1876) < 10) & !(hnl_q_01==0 & abs(hnl_m_01- 9.4603) < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-10.0233) < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-10.3552) < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-3.0969)  < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-3.6861)  < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-0.7827)  < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-1.0190)  < 0.08)',
    '!(hnl_q_02==0 & abs(hnl_m_02-91.1876) < 10) & !(hnl_q_02==0 & abs(hnl_m_02- 9.4603) < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-10.0233) < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-10.3552) < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-3.0969)  < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-3.6861)  < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-0.7827)  < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-1.0190)  < 0.08)',
    '!(hnl_w_vis_m > 50. & hnl_w_vis_m < 80.)',
    'l1_pt>7',
    'l2_pt>7',
    'hnl_pt_12>15',
    'sv_cos>0.99',
    'sv_prob>0.001',
    'l0_pt>35', # 2017!!
    'abs(l1_dz)<10',
    'abs(l2_dz)<10',
    'l0_reliso_rho_03<0.1',
    'l1_reliso_rho_03 < 0.2',
    'l2_reliso_rho_03 < 0.2',
    '(l1_gen_match_isPrompt==1 | l1_gen_match_pdgid==22 | l2_gen_match_isPrompt==1 | l2_gen_match_pdgid==22)',
]

selection_data_mme_os = [
    'l0_pt > 25 & l2_pt > 5 & l1_pt > 5 & l0_id_m == 1 & l1_LooseNoIso == 1 & l2_Medium == 1',
    'abs(l0_eta) < 2.4 & abs(l0_dxy) < 0.05 & abs(l0_dz) < 0.1 & l0_reliso_rho_03 < 0.1 & abs(l1_eta) < 2.5 & l1_reliso_rho_03 < 10 & abs(l2_eta) < 2.4 & l2_reliso_rho_03 < 10 & hnl_q_12 == 0 & nbj == 0 & hnl_dr_12 < 1. & hnl_m_12 < 12 & sv_cos > 0.9 & abs(hnl_dphi_01)>1. & abs(hnl_dphi_02)>1. & abs(l1_dxy) > 0.01 & abs(l2_dxy) > 0.01',
    '!(hnl_q_02==0 & abs(hnl_m_02-91.1876) < 10) & !(hnl_q_02==0 & abs(hnl_m_02- 9.4603) < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-10.0233) < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-10.3552) < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-3.0969)  < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-3.6861)  < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-0.7827)  < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-1.0190)  < 0.08)',
    'l0_q!=l2_q',
    '!(hnl_w_vis_m > 50. & hnl_w_vis_m < 80.)',
    'l1_pt>7',
    'hnl_pt_12>15',
    'sv_cos>0.99',
    'sv_prob>0.001',
    'l0_reliso_rho_03<0.1',
    'l0_pt>25',
    'abs(l1_dz)<10',
    'abs(l2_dz)<10',
    'l1_reliso_rho_03 < 0.2',
    'l2_reliso_rho_03 < 0.2',
    '(l1_gen_match_isPrompt==1 | l1_gen_match_pdgid==22 | l2_gen_match_isPrompt==1 | l2_gen_match_pdgid==22)',
]

selection_data_eee_full    = ' & '.join(selection_data_eee)
selection_data_mme_os_full = ' & '.join(selection_data_mme_os)

# tree_eee.Scan("run:lumi:event:l0_pdgid:l0_pt:l1_pdgid:l1_pt:abs(l1_dxy):l2_pdgid:l2_pt:abs(l2_dxy):hnl_m_12:hnl_2d_disp", 
              # selection_data_eee_full, 
              # "precision=4 col=1:6:9.0f:4")

# print('='*30)

# tree_mem.Scan("run:lumi:event:l0_pdgid:l0_pt:l1_pdgid:l1_pt:abs(l1_dxy):l2_pdgid:l2_pt:abs(l2_dxy):hnl_m_12:hnl_2d_disp", 
              # selection_data_mme_os_full, 
              # "precision=4 col=1:6:9.0f:4")

to_check_martina_doesnt_have = [
# eee
'run == 1 & lumi == 119098 & event == 269424234',
'run == 1 & lumi == 59071 & event == 133630051',
'run == 1 & lumi == 62631 & event == 141683112',
# mem_os
# 'run == 1 & lumi == 142236 & event == 321765876',
# 'run == 1 & lumi == 222567 & event == 503490272',
# 'run == 1 & lumi == 52077 & event == 117809463',
]

to_check_i_dont_have = [
# eee
'run == 1 & lumi == 122708 & event == 277589688',
'run == 1 & lumi == 127797 & event == 289102176',
'run == 1 & lumi == 135493 & event == 306512460',
'run == 1 & lumi == 13791 & event == 31198175',  
'run == 1 & lumi == 138743 & event == 313863816',
'run == 1 & lumi == 148808 & event == 336634066',
'run == 1 & lumi == 165037 & event == 373346804',
'run == 1 & lumi == 181798 & event == 411263972',
'run == 1 & lumi == 186659 & event == 422259793',
'run == 1 & lumi == 206262 & event == 466604276',
'run == 1 & lumi == 209608 & event == 474175765',
'run == 1 & lumi == 214894 & event == 486133246',
'run == 1 & lumi == 226689 & event == 512816380',
'run == 1 & lumi == 29497 & event == 66727256',  
'run == 1 & lumi == 38304 & event == 86651108',  
'run == 1 & lumi == 43407 & event == 98194032',  
'run == 1 & lumi == 46261 & event == 104651064', 
'run == 1 & lumi == 97356 & event == 220237943', 
### not in ntuple
'run == 1 & lumi == 18187  & event == 31690514',  
'run == 1 & lumi == 21955  & event == 38256226',  
'run == 1 & lumi == 41908  & event == 73024119',  
'run == 1 & lumi == 130611 & event == 295467446',
'run == 1 & lumi == 133014 & event == 300904752',
# mem_os
# 'run == 1 & lumi == 186067 & event == 420918977',
# 'run == 1 & lumi == 85866 & event == 194246274',
]



from collections import OrderedDict
check = OrderedDict()

# for i in selection_data_eee + ['l0_eid_mva_noniso_wp90 == 1', 'l1_LooseNoIso == 1', 'l2_LooseNoIso == 1', '1 == 1']:
# for i in selection_data_eee + ['sv_cos > 0.99 & l0_reliso_rho_03 < 0.1', '1 == 1']:
# for i in [#'sv_cos > 0.99 & l0_reliso_rho_03 < 0.1 & (l1_gen_match_isPrompt==1 | l1_gen_match_pdgid==22 | l2_gen_match_isPrompt==1 | l2_gen_match_pdgid==22) & nbj==0 & l2_reliso_rho_03 < 0.2', 
          # 'nbj == 0', 
          # 'sv_cos > 0.9',
# for i in [#'abs(l0_eta) < 2.5',
          # 'abs(l0_dxy) < 0.05 ',
          # ' abs(l0_dz) < 0.1 ',
          # ' abs(l1_eta) < 2.5 ',
          # ' l1_reliso_rho_03 < 10 ',
          # ' abs(l2_eta) < 2.5 ',
          # ' l2_reliso_rho_03 < 10 ',
          # ' hnl_q_12 == 0 ',
          # ' hnl_dr_12 < 1. ',
          # ' hnl_m_12 < 12 ',
          # ' abs(hnl_dphi_01)>1. ',
          # ' abs(hnl_dphi_02)>1. ',
          # ' abs(l1_dxy) > 0.01 ',
          # ' abs(l2_dxy) > 0.01',
          # 'abs(l0_eta) < 2.4 & abs(l1_eta) < 2.4 & abs(l2_eta) < 2.4 ',
for i in ['1 == 1']:
    count_not_found =0
    count_exists    =0
    # i += '| l0_reliso_rho_03 > 0.1'
    # i += '& l1_LooseNoIso'
    for iev in to_check_i_dont_have:
        check [iev] = tree_eee.GetEntries(iev) # all found
        check [iev] = tree_eee.GetEntries(iev + ' & ' + i) # all found
        if check[iev] == 0: print(iev, check[iev])
        if check[iev] == 0: count_not_found += 1
        if check[iev] == 1: count_exists    += 1

    print(i)
    print('not found: {nf}, found: {ex} \n'.format(nf=count_not_found, ex=count_exists))


# double_cross_check_sv_cos_and_sv_prob = [
# 'run == 104 & lumi == 1 & event == 194',
# 'run == 30  & lumi == 1 & event == 304',
# ]

# for iev in double_cross_check_sv_cos_and_sv_prob:
    # tree_eem.Scan("run:lumi:event:l0_pdgid:l0_pt:l1_pdgid:l1_pt:abs(l1_dxy):l1_reliso_rho_03:l2_pdgid:l2_pt:abs(l2_dxy):l2_reliso_rho_03:hnl_m_12:hnl_2d_disp:sv_cos:sv_prob", 
                  # iev + ' & ' + selection_data_eem_os_full, 
                  # "precision=4 ")


