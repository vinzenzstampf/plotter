import ROOT as rt

fin_mmm = '/eos/home-v/vstampf/HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO/HNLTreeProducer_mmm/tree.root'
fin_mem = '/eos/home-v/vstampf/HN3L_M_4_V_0p00290516780927_mu_massiveAndCKM_LO/HNLTreeProducer_mem/tree.root'

tf_in_mmm = rt.TFile(fin_mmm)
tf_in_mem = rt.TFile(fin_mem)

tree_mmm = tf_in_mmm.Get('tree')
tree_mem = tf_in_mem.Get('tree')

tree_mmm.SetScanField(0)
tree_mem.SetScanField(0)

# tree.Scan("run:lumi:event:l0_pdgid:l0_pt:l1_pdgid:l1_pt:abs(l1_dxy):l2_pdgid:l2_pt:abs(l2_dxy):puppimet_pt:pfmet_pt:pass_mmm:pass_mem:pass_eem:pass_eee", "l0_id_m & l1_reliso_rho_03 < 1.2 & l2_reliso_rho_03 < 1.2", "col=3:4:5:3:9.4f:3:9.4f:9.4f:3:9.4f:9.4f:9.4f:9.4f:1:1:1:1")

# print '\n\nNOW MMM\n\n'

# cut_string_mmm = 'l0_pt > 28 & l1_id_m & l2_id_m & l1_reliso_rho_03 < 2 & l2_reliso_rho_03 < 2 & l1_pt > 5 & l2_pt > 5'
# cut_string_mem = 'l0_pt > 28 & l1_LooseNoIso & l2_id_m & l1_reliso_rho_03 < 2 & l2_reliso_rho_03 < 2 & l1_pt > 5 & l2_pt > 5'

# tree_mmm.Scan("run:lumi:event:l0_pdgid:l0_pt:l1_pdgid:l1_pt:abs(l1_dxy):l2_pdgid:l2_pt:abs(l2_dxy):pass_mmm:pass_mem:pass_eem:pass_eee", 
  # cut_string_mmm, 
  # # "col=3:4:5:3:9.4f:3:9.4f:9.4f:3:9.4f:9.4f:1:1:1:1")
  # "precision=4 col=:::::::::::1:1:1:1")

# print '\n\nNOW MEM\n\n'


# tree_mem.Scan("run:lumi:event:l0_pdgid:l0_pt:l1_pdgid:l1_pt:abs(l1_dxy):l2_pdgid:l2_pt:abs(l2_dxy):pass_mmm:pass_mem:pass_eem:pass_eee", 
  # cut_string_mem, 
  # # "col=3:4:5:3:9.4f:3:9.4f:9.4f:3:9.4f:9.4f:1:1:1:1")
  # "precision=4 col=:::::::::::1:1:1:1")

# VS: 13/12/19


# print '\n\nNOW MMM\n\n'

selection_data = [
    'l0_pt > 25 & l2_pt > 5 & l1_pt > 5 & l0_id_m == 1 & l1_Medium == 1 & l2_Medium == 1',

    'abs(l0_eta) < 2.4 & abs(l0_dxy) < 0.05 & abs(l0_dz) < 0.2 & l0_reliso_rho_03 < 0.2 & abs(l1_eta) < 2.4 & l1_reliso_rho_03 < 10',
    'abs(l2_eta) < 2.4 & l2_reliso_rho_03 < 10 & hnl_q_12 == 0 & nbj == 0 & hnl_dr_12 < 1. & hnl_m_12 < 12 & sv_cos > 0.9 & abs(hnl_dphi_01)>1',
    'abs(hnl_dphi_02)>1. & abs(l1_dxy) > 0.01 & abs(l2_dxy) > 0.01',

    'abs(hnl_m_12-3.0969) > 0.08 & abs(hnl_m_12-3.6861) > 0.08 & abs(hnl_m_12-0.7827) > 0.08 & abs(hnl_m_12-1.0190) > 0.08',

    '!(hnl_q_01==0 & abs(hnl_m_01-91.1876) < 10) & !(hnl_q_01==0 & abs(hnl_m_01- 9.4603) < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-10.0233) < 0.08)',
    '!(hnl_q_01==0 & abs(hnl_m_01-10.3552) < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-3.0969)  < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-3.6861)  < 0.08)',
    '!(hnl_q_01==0 & abs(hnl_m_01-0.7827)  < 0.08) & !(hnl_q_01==0 & abs(hnl_m_01-1.0190)  < 0.08)',

    '!(hnl_q_02==0 & abs(hnl_m_02-91.1876) < 10) & !(hnl_q_02==0 & abs(hnl_m_02- 9.4603) < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-10.0233) < 0.08)',
    '!(hnl_q_02==0 & abs(hnl_m_02-10.3552) < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-3.0969)  < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-3.6861)  < 0.08)',
    '!(hnl_q_02==0 & abs(hnl_m_02-0.7827)  < 0.08) & !(hnl_q_02==0 & abs(hnl_m_02-1.0190)  < 0.08)',

    '(hnl_w_vis_m > 50. & hnl_w_vis_m < 80.)',

    'hnl_2d_disp_sig>20',

    'hnl_pt_12>15',

    'sv_cos>0.99',

    'sv_prob>0.001',

    'abs(l1_dz) < 10 & abs(l2_dz) < 10',

    'l0_reliso_rho_03<0.1',

    # selection_tight 
    'l1_reliso_rho_03 < 0.2 & l2_reliso_rho_03 < 0.2'
]

selection_data = ' & '.join(selection_data)


# tree_mmm.Scan("run:lumi:event:l0_pdgid:l0_pt:l1_pdgid:l1_pt:abs(l1_dxy):l2_pdgid:l2_pt:abs(l2_dxy):pass_mmm:pass_mem:pass_eem:pass_eee", 
  # selection_data, 
  # # "col=3:4:5:3:9.4f:3:9.4f:9.4f:3:9.4f:9.4f:1:1:1:1")
  # "precision=4 col=:::::::::::1:1:1:1")


to_check= [
'run==1 & lumi==1 & event==510', 
'run==6 & lumi==1 & event==65',
'run==9 & lumi==1 & event==186',
'run==9 & lumi==1 & event==625',
'run==11 & lumi==1 & event==838',
'run==13 & lumi==1 & event==231',
'run==13 & lumi==1 & event==775',
'run==13 & lumi==1 & event==999',
'run==14 & lumi==1 & event==86',
'run==16 & lumi==1 & event==219',
'run==16 & lumi==1 & event==686',
'run==17 & lumi==1 & event==666',
'run==18 & lumi==1 & event==371',
'run==18 & lumi==1 & event==622',
'run==21 & lumi==1 & event==892',
'run==23 & lumi==1 & event==978',
'run==24 & lumi==1 & event==42',
'run==25 & lumi==1 & event==530',
'run==25 & lumi==1 & event==827',
'run==27 & lumi==1 & event==298',
'run==30 & lumi==1 & event==754',
'run==32 & lumi==1 & event==275',
'run==32 & lumi==1 & event==327',
'run==33 & lumi==1 & event==722',
'run==34 & lumi==1 & event==966',
'run==37 & lumi==1 & event==606',
'run==37 & lumi==1 & event==876',
'run==39 & lumi==1 & event==403',
'run==40 & lumi==1 & event==222',
'run==40 & lumi==1 & event==299',
'run==41 & lumi==1 & event==570',
'run==41 & lumi==1 & event==728',
'run==41 & lumi==1 & event==887',
'run==42 & lumi==1 & event==590',
'run==47 & lumi==1 & event==478',
'run==47 & lumi==1 & event==629',
'run==51 & lumi==1 & event==295',
'run==51 & lumi==1 & event==725',
'run==52 & lumi==1 & event==10',
'run==54 & lumi==1 & event==336',
'run==54 & lumi==1 & event==444',
'run==55 & lumi==1 & event==241',
'run==56 & lumi==1 & event==27',
'run==56 & lumi==1 & event==862',
'run==58 & lumi==1 & event==303',
'run==58 & lumi==1 & event==895',
'run==60 & lumi==1 & event==734',
'run==62 & lumi==1 & event==954',
'run==63 & lumi==1 & event==398',
'run==63 & lumi==1 & event==939',
'run==64 & lumi==1 & event==239',
'run==64 & lumi==1 & event==296',
'run==65 & lumi==1 & event==130',
'run==67 & lumi==1 & event==284',
'run==67 & lumi==1 & event==585',
'run==69 & lumi==1 & event==271',
'run==70 & lumi==1 & event==532',
'run==71 & lumi==1 & event==347',
'run==73 & lumi==1 & event==298',
'run==74 & lumi==1 & event==33',
'run==75 & lumi==1 & event==566',
'run==76 & lumi==1 & event==242',
'run==77 & lumi==1 & event==37',
'run==77 & lumi==1 & event==378',
'run==77 & lumi==1 & event==565',
'run==78 & lumi==1 & event==580',
'run==79 & lumi==1 & event==14',
'run==82 & lumi==1 & event==122',
'run==82 & lumi==1 & event==234',
'run==86 & lumi==1 & event==747',
'run==88 & lumi==1 & event==88',
'run==91 & lumi==1 & event==34',
'run==92 & lumi==1 & event==81',
'run==92 & lumi==1 & event==251',
'run==92 & lumi==1 & event==800',
'run==92 & lumi==1 & event==819',
'run==92 & lumi==1 & event==839',
'run==93 & lumi==1 & event==157',
'run==93 & lumi==1 & event==534',
'run==94 & lumi==1 & event==467',
'run==95 & lumi==1 & event==893',
'run==96 & lumi==1 & event==466',
'run==98 & lumi==1 & event==69',
'run==99 & lumi==1 & event==233',
'run==100 & lumi==1 & event==362',
'run==101 & lumi==1 & event==650',
'run==103 & lumi==1 & event==388',
'run==105 & lumi==1 & event==280',
'run==106 & lumi==1 & event==507',
'run==107 & lumi==1 & event==56',
'run==107 & lumi==1 & event==106',
'run==107 & lumi==1 & event==392',
'run==109 & lumi==1 & event==505',
'run==110 & lumi==1 & event==831',
'run==112 & lumi==1 & event==935',
'run==115 & lumi==1 & event==793',
'run==116 & lumi==1 & event==450',
'run==117 & lumi==1 & event==518',
'run==117 & lumi==1 & event==977',
'run==117 & lumi==1 & event==986',
'run==119 & lumi==1 & event==962',
'run==119 & lumi==1 & event==967',
'run==120 & lumi==1 & event==78',
'run==120 & lumi==1 & event==179',
'run==121 & lumi==1 & event==729',
'run==124 & lumi==1 & event==238',
'run==124 & lumi==1 & event==391',
'run==130 & lumi==1 & event==863',
'run==131 & lumi==1 & event==258',
'run==131 & lumi==1 & event==960',
'run==133 & lumi==1 & event==542',
'run==136 & lumi==1 & event==383',
'run==136 & lumi==1 & event==859',
'run==136 & lumi==1 & event==933',
'run==137 & lumi==1 & event==790',
'run==138 & lumi==1 & event==760',
'run==139 & lumi==1 & event==718',
'run==143 & lumi==1 & event==278',
'run==144 & lumi==1 & event==482',
'run==144 & lumi==1 & event==653',
'run==144 & lumi==1 & event==755',
'run==144 & lumi==1 & event==978',
'run==145 & lumi==1 & event==910',
'run==146 & lumi==1 & event==320',
'run==147 & lumi==1 & event==148',
'run==147 & lumi==1 & event==856',
'run==148 & lumi==1 & event==110',
'run==148 & lumi==1 & event==160',
'run==149 & lumi==1 & event==988',
'run==150 & lumi==1 & event==984',
'run==151 & lumi==1 & event==188',
'run==153 & lumi==1 & event==287',
'run==154 & lumi==1 & event==283',
'run==154 & lumi==1 & event==453',
'run==155 & lumi==1 & event==749',
'run==156 & lumi==1 & event==56',
'run==157 & lumi==1 & event==112',
'run==157 & lumi==1 & event==165',
'run==157 & lumi==1 & event==555',
'run==157 & lumi==1 & event==916',
'run==162 & lumi==1 & event==37',
'run==162 & lumi==1 & event==440',
'run==163 & lumi==1 & event==865',
'run==165 & lumi==1 & event==933',
'run==166 & lumi==1 & event==22',
'run==167 & lumi==1 & event==931',
'run==170 & lumi==1 & event==62',
'run==170 & lumi==1 & event==734',
'run==172 & lumi==1 & event==82',
'run==172 & lumi==1 & event==758',
'run==172 & lumi==1 & event==879',
'run==177 & lumi==1 & event==694',
'run==181 & lumi==1 & event==513',
'run==188 & lumi==1 & event==362',
'run==189 & lumi==1 & event==270',
'run==190 & lumi==1 & event==43',
'run==192 & lumi==1 & event==246',
'run==194 & lumi==1 & event==38',
'run==195 & lumi==1 & event==125',
'run==198 & lumi==1 & event==480',
'run==198 & lumi==1 & event==816',
'run==200 & lumi==1 & event==39',
'run==200 & lumi==1 & event==834',
'run==205 & lumi==1 & event==153',
'run==208 & lumi==1 & event==60',
'run==208 & lumi==1 & event==529',
'run==208 & lumi==1 & event==697',
'run==210 & lumi==1 & event==807',
'run==210 & lumi==1 & event==901',
'run==211 & lumi==1 & event==383',
'run==212 & lumi==1 & event==946',
'run==214 & lumi==1 & event==848',
'run==217 & lumi==1 & event==213',
'run==217 & lumi==1 & event==685',
'run==224 & lumi==1 & event==246',
'run==224 & lumi==1 & event==943',
'run==225 & lumi==1 & event==77',
'run==225 & lumi==1 & event==850',
'run==227 & lumi==1 & event==671',
'run==228 & lumi==1 & event==128',
'run==228 & lumi==1 & event==289',
'run==228 & lumi==1 & event==929',
'run==230 & lumi==1 & event==943',
'run==231 & lumi==1 & event==133',
'run==231 & lumi==1 & event==880',
'run==233 & lumi==1 & event==78',
'run==234 & lumi==1 & event==617',
'run==234 & lumi==1 & event==884',
'run==235 & lumi==1 & event==488',
'run==235 & lumi==1 & event==675',
'run==237 & lumi==1 & event==517',
'run==239 & lumi==1 & event==485',
'run==241 & lumi==1 & event==674',
'run==242 & lumi==1 & event==891',
'run==243 & lumi==1 & event==621',
'run==243 & lumi==1 & event==914',
'run==244 & lumi==1 & event==43',
'run==244 & lumi==1 & event==253',
'run==244 & lumi==1 & event==628',
'run==245 & lumi==1 & event==739',
'run==246 & lumi==1 & event==301',
'run==246 & lumi==1 & event==573',
'run==246 & lumi==1 & event==974',
'run==247 & lumi==1 & event==289',
'run==248 & lumi==1 & event==893',
'run==249 & lumi==1 & event==765',
'run==250 & lumi==1 & event==1',
'run==250 & lumi==1 & event==435',
]

from collections import OrderedDict
check = OrderedDict()
 
count_0 =0
count_1 =0

for iev in to_check:
    check [iev] = tree_mmm.GetEntries(iev)
    print iev, check[iev]
    if check[iev] == 0: count_0 += 1
    if check[iev] == 1: count_1 += 1

print count_0, count_1




