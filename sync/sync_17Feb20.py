import ROOT as rt
import subprocess

fin_mmm = '/eos/home-v/vstampf/HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO/HNLTreeProducer_mmm/tree.root'
#fin_mem = '/eos/home-v/vstampf/HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO/HNLTreeProducer_mem/tree.root'
fin_mem = '/Users/cesareborgia/cernbox/hnl/2017/sig/HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO/HNLTreeProducer_mem/tree.root'

#tf_in_mmm = rt.TFile(fin_mmm)
tf_in_mem = rt.TFile(fin_mem)

#tree_mmm = tf_in_mmm.Get('tree')
tree_mem = tf_in_mem.Get('tree')

#tree_mmm.SetScanField(0)
tree_mem.SetScanField(0)


selection_data_mem_ss = [
  'l0_pt > 25 & l2_pt > 5 & l1_pt > 5 & l0_id_m == 1 & l1_LooseNoIso == 1 & l2_Medium == 1',
  'abs(l0_eta) < 2.4 & abs(l0_dxy) < 0.05 & abs(l0_dz) < 0.1 & l0_reliso_rho_03 < 0.1 & abs(l1_eta) < 2.4 & l1_reliso_rho_03 < 10 & abs(l2_eta) < 2.4 & l2_reliso_rho_03 < 10 & hnl_q_12 == 0 & nbj == 0 & hnl_dr_12 < 1. & hnl_m_12 < 12 & sv_cos > 0.9 & abs(hnl_dphi_01)>1. & abs(hnl_dphi_02)>1. & abs(l1_dxy) > 0.01 & abs(l2_dxy) > 0.01',
  'l0_q==l2_q',
  '(hnl_w_vis_m > 50. & hnl_w_vis_m < 80.)',
  'l1_pt>7',
  'hnl_pt_12>15',
  'sv_cos>0.99',
  'sv_prob>0.001',
  'l0_reliso_rho_03<0.1',
  'l0_pt>25',
  'abs(l1_dz)<10',
  'abs(l2_dz)<10',
  'l1_reliso_rho_03 < 0.2 & l2_reliso_rho_03 < 0.2'
]

selection_data_mem_ss_full = ' & '.join(selection_data_mem_ss)

# tree_mem.Scan("run:lumi:event:l0_pdgid:l0_pt:l2_pdgid:l2_pt:abs(l2_dxy):l1_pdgid:l1_pt:abs(l1_dxy):hnl_m_12:hnl_2d_disp", 
              # selection_data_mem_ss_full, 
              # "precision=4 ")


to_check_martina_doesnt_have = [
'run==101 & lumi==1 & event==255',
'run==120 & lumi==1 & event==195',
'run==134 & lumi==1 & event==790',
'run==14 & lumi==1 & event==561',
'run==140 & lumi==1 & event==331',
'run==153 & lumi==1 & event==481',
'run==164 & lumi==1 & event==162',
'run==171 & lumi==1 & event==737',
'run==191 & lumi==1 & event==773',
'run==199 & lumi==1 & event==475',
'run==200 & lumi==1 & event==442',
'run==204 & lumi==1 & event==384',
'run==214 & lumi==1 & event==651',
'run==223 & lumi==1 & event==753',
'run==23 & lumi==1 & event==458',
'run==245 & lumi==1 & event==286',
'run==249 & lumi==1 & event==237',
'run==30 & lumi==1 & event==770',
'run==44 & lumi==1 & event==914',
'run==7 & lumi==1 & event==962',
'run==87 & lumi==1 & event==932',
]

to_check_i_dont_have = [
# 'run == 10 & lumi==1 & event==792',
# 'run == 13 & lumi==1 & event==758',
# 'run == 21 & lumi==1 & event==866',
# 'run == 22 & lumi==1 & event==794',
'run == 27 & lumi==1 & event==537',
'run == 3 & lumi==1 & event==779',
# 'run == 47 & lumi==1 & event==766',
'run == 58 & lumi==1 & event==550',
'run == 58 & lumi==1 & event==993',
# 'run == 7 & lumi==1 & event==363',
# 'run == 73 & lumi==1 & event==430',
# 'run == 8 & lumi==1 & event==559',
# 'run == 84 & lumi==1 & event==826',
# 'run == 84 & lumi==1 & event==924',
# 'run == 86 & lumi==1 & event==541',
# 'run == 88 & lumi==1 & event==714',
# 'run == 89 & lumi==1 & event==593',
# 'run == 91 & lumi==1 & event==288',
# 'run == 98 & lumi==1 & event==738',
# 'run == 112 & lumi==1 & event==297',
'run == 116 & lumi==1 & event==326',
# 'run == 141 & lumi==1 & event==484',
# 'run == 142 & lumi==1 & event==53',
# 'run == 144 & lumi==1 & event==411',
# 'run == 153 & lumi==1 & event==173',
# 'run == 156 & lumi==1 & event==139',
# 'run == 169 & lumi==1 & event==314',
# 'run == 170 & lumi==1 & event==935',
# 'run == 182 & lumi==1 & event==687',
# 'run == 189 & lumi==1 & event==880',
# 'run == 191 & lumi==1 & event==543',
# 'run == 196 & lumi==1 & event==538',
# 'run == 205 & lumi==1 & event==747',
# 'run == 206 & lumi==1 & event==666',
# 'run == 207 & lumi==1 & event==395',
# 'run == 207 & lumi==1 & event==519',
# 'run == 212 & lumi==1 & event==936',
# 'run == 217 & lumi==1 & event==373',
# 'run == 220 & lumi==1 & event==873',
# 'run == 222 & lumi==1 & event==647',
# 'run == 225 & lumi==1 & event==711',
# 'run == 232 & lumi==1 & event==188',
# 'run == 241 & lumi==1 & event==383',
# 'run == 241 & lumi==1 & event==633',
]

from collections import OrderedDict
check = OrderedDict()

# for i in selection_data_mem_ss + ['l1_reliso_rho_03 < 0.2', 'l2_reliso_rho_03 < 0.2']:
    # count_not_found =0
    # count_exists    =0
    # for iev in to_check:
        # check [iev] = tree_mem.GetEntries(iev) # all found
        # check [iev] = tree_mem.GetEntries(iev + ' & ' + i) # all found
            # print(iev, check[iev])
            # if check[iev] == 0: count_not_found += 1
            # if check[iev] == 1: count_exists    += 1

    # print(i)
    # print('not found: {nf}, found: {ex} \n'.format(nf=count_not_found, ex=count_exists))


for iev in to_check_i_dont_have:
    tree_mem.Scan("run:lumi:event:l0_pdgid:l0_pt:l2_pdgid:l2_pt:abs(l2_dxy):l2_reliso_rho_03:l1_pdgid:l1_pt:abs(l1_dxy):l1_reliso_rho_03:hnl_m_12:hnl_2d_disp", 
                  iev + ' & ' + selection_data_mem_ss_full, 
                  "precision=4 ")
        # print(iev, check[iev])


