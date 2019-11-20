import ROOT as rt
from rootpy.plotting import Canvas, Pad
from ROOT import RDataFrame as rdf
from plotter.selections import Selections as sel
from plotter.cmsstyle import CMS_lumi
import numpy as np

def show_logo_in_prog():
    logo = rt.TLatex()
    logo.SetNDC()
    logo.SetTextAlign(11)
    logo.SetTextFont(61)
    logo.SetTextSize(0.041)
    logo.DrawLatex(0.15,0.88,'CMS')
    
    preliminary = rt.TLatex()
    preliminary.SetNDC()
    preliminary.SetTextAlign(11)
    preliminary.SetTextFont(52)
    preliminary.SetTextSize(0.035)
    preliminary.DrawLatex(0.25,0.88,'In Progress')

def show_lumi(title):
    latex = rt.TLatex()
    latex.SetNDC()
    latex.SetTextAlign(31)
    latex.SetTextFont(42)
    latex.SetTextSize(0.031)
    latex.DrawLatex(0.83,0.88,title)

rt.ROOT.EnableImplicitMT()

rt.gStyle.SetOptStat(0)

cuts = sel('mmm')

tch = rt.TChain('tree')

tch.Add('/Users/cesareborgia/cernbox/ntuples/2018/mmm/Single_mu_2018A/HNLTreeProducer/tree.root')
tch.Add('/Users/cesareborgia/cernbox/ntuples/2018/mmm/Single_mu_2018B/HNLTreeProducer/tree.root')
tch.Add('/Users/cesareborgia/cernbox/ntuples/2018/mmm/Single_mu_2018C/HNLTreeProducer/tree.root')
tch.Add('/Users/cesareborgia/cernbox/ntuples/2018/mmm/Single_mu_2018D/HNLTreeProducer/tree.root')

df = rdf(tch)

# b_dxy  = np.logspace(-2, 1, 10)
# b_dxy  = np.logspace(-2, 1, 25)
b_dxy  = np.logspace(-2, 1, 26)
b_disp = np.logspace(-2, 1.5, 20)
# b_disp = np.logspace(-2, 1.5, 21)
b_dr12 = np.linspace(0, 1., 21)
# b_dr12 = np.linspace(0, 1., 20)
b_m12  = np.linspace(0, 12, 25)
b_sv_cos = np.linspace(0.5, 1.2, 21)

# cut = ' & '.join( [ cuts.selections['SR_sb_no_dxy'], cuts.selections['pt_iso'] ] ) ## v0: no vetoes --> doesn't work that well

# cut = ' & '.join( [ cuts.selections['SR_sb_no_dxy'], cuts.selections['pt_iso'], ## v1: add  vetoes 
                    # cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'], cuts.selections['vetoes_02_OS'] ] )

cut = ' & '.join( [ cuts.selections['SR_sb_w_dxy'], cuts.selections['pt_iso'], ## v2: add  dxy
                    cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'], cuts.selections['vetoes_02_OS'] ] ) 

# cut = ' & '.join( [ cuts.selections['baseline'], cuts.selections['pt_iso'], ## v3: SR, as before
                    # cuts.selections['vetoes_12_OS'], cuts.selections['vetoes_01_OS'], cuts.selections['vetoes_02_OS'] ] )

df_0 = df.Filter(cut)

df_0 = df_0.Define('abs_l1_dxy', 'abs(l1_dxy)')
df_0 = df_0.Define('abs_l2_dxy', 'abs(l2_dxy)')

df_lnt = df_0.Filter( '! (' +cuts.selections['tight'] + ' )' )
df_t   = df_0.Filter(cuts.selections['tight'])
# from pdb import set_trace as st; st()

dxy  = True
disp = True
dr   = True
sv   = True
m12  = True

# histos
if dxy:
    ph_1dxy_t = df_t.Histo1D(('abs_l1_dxy_t', 'abs_l1_dxy_t', len(b_dxy) -1, b_dxy), 'abs_l1_dxy')
    ph_2dxy_t = df_t.Histo1D(('abs_l2_dxy_t', 'abs_l2_dxy_t', len(b_dxy) -1, b_dxy), 'abs_l2_dxy')

    ph_1dxy_lnt = df_lnt.Histo1D(('abs_l1_dxy_lnt', 'abs_l1_dxy_lnt', len(b_dxy) -1, b_dxy), 'abs_l1_dxy')
    ph_2dxy_lnt = df_lnt.Histo1D(('abs_l2_dxy_lnt', 'abs_l2_dxy_lnt', len(b_dxy) -1, b_dxy), 'abs_l2_dxy')

    h_1dxy_t = ph_1dxy_t.GetPtr()
    h_2dxy_t = ph_2dxy_t.GetPtr()

    h_1dxy_lnt = ph_1dxy_lnt.GetPtr()
    h_2dxy_lnt = ph_2dxy_lnt.GetPtr()

    h_1dxy_t  .Add(h_2dxy_t)
    h_1dxy_lnt.Add(h_2dxy_lnt)

    h_1dxy_lnt.SetTitle('; d_{xy} (cm); %')
    h_1dxy_lnt.SetName('loose-not-tight')
    h_1dxy_lnt.SetLineColor(rt.kCyan+1)
    h_1dxy_lnt.SetLineWidth(2)

    h_1dxy_t  .SetTitle('tight')
    h_1dxy_t  .SetLineColor(rt.kBlue+2)
    h_1dxy_t  .SetLineWidth(2)
    

if disp:
    ph_disp_t = df_t.Histo1D(('2d_disp_t', '2d_disp_t', len(b_disp) -1, b_disp), 'hnl_2d_disp')

    ph_disp_lnt = df_lnt.Histo1D(('2d_disp_lnt', '2d_disp_lnt', len(b_disp) -1, b_disp), 'hnl_2d_disp')

    h_disp_t = ph_disp_t.GetPtr()

    h_disp_lnt = ph_disp_lnt.GetPtr()

    h_disp_lnt.SetTitle('; L_{xy} (cm); %')
    h_disp_lnt.SetName('loose-not-tight')
    h_disp_lnt.SetLineColor(rt.kCyan+1)
    h_disp_lnt.SetLineWidth(2)

    h_disp_t  .SetTitle('tight')
    h_disp_t  .SetLineColor(rt.kBlue+2)
    h_disp_t  .SetLineWidth(2)


if dr:
    ph_dr12_t = df_t.Histo1D(('dr12_t', 'dr12_t', len(b_dr12) -1, b_dr12), 'hnl_dr_12')

    ph_dr12_lnt = df_lnt.Histo1D(('dr12_lnt', 'dr12_lnt', len(b_dr12) -1, b_dr12), 'hnl_dr_12')

    h_dr12_t = ph_dr12_t.GetPtr()

    h_dr12_lnt = ph_dr12_lnt.GetPtr()

    h_dr12_lnt.SetTitle('; #Delta R_{23}; %')
    h_dr12_lnt.SetName('loose-not-tight')
    h_dr12_lnt.SetLineColor(rt.kCyan+1)
    h_dr12_lnt.SetLineWidth(2)

    h_dr12_t  .SetTitle('tight')
    h_dr12_t  .SetLineColor(rt.kBlue+2)
    h_dr12_t  .SetLineWidth(2)

if sv:
    ph_sv_cos_t = df_t.Histo1D(('sv_cos_t', 'sv_cos_t', len(b_sv_cos) -1, b_sv_cos), 'sv_cos')

    ph_sv_cos_lnt = df_lnt.Histo1D(('sv_cos_lnt', 'sv_cos_lnt', len(b_sv_cos) -1, b_sv_cos), 'sv_cos')

    h_sv_cos_t = ph_sv_cos_t.GetPtr()

    h_sv_cos_lnt = ph_sv_cos_lnt.GetPtr()

    h_sv_cos_lnt.SetTitle('; sv_cos; %')
    h_sv_cos_lnt.SetName('loose-not-tight')
    h_sv_cos_lnt.SetLineColor(rt.kCyan+1)
    h_sv_cos_lnt.SetLineWidth(2)

    h_sv_cos_t  .SetTitle('tight')
    h_sv_cos_t  .SetLineColor(rt.kBlue+2)
    h_sv_cos_t  .SetLineWidth(2)

if m12:
    ph_m12_t = df_t.Histo1D(('m12_t', 'm12_t', len(b_m12) -1, b_m12), 'hnl_m_12')

    ph_m12_lnt = df_lnt.Histo1D(('m12_lnt', 'm12_lnt', len(b_m12) -1, b_m12), 'hnl_m_12')

    h_m12_t = ph_m12_t.GetPtr()

    h_m12_lnt = ph_m12_lnt.GetPtr()

    h_m12_lnt.SetTitle('; m_{23} (GeV); %')
    h_m12_lnt.SetName('loose-not-tight')
    h_m12_lnt.SetLineColor(rt.kCyan+1)
    h_m12_lnt.SetLineWidth(2)

    h_m12_t  .SetTitle('tight')
    h_m12_t  .SetLineColor(rt.kBlue+2)
    h_m12_t  .SetLineWidth(2)



if dxy:
    can = Canvas(width=700, height=700) ; can.Draw()
    can.cd() ; main_pad  = Pad(0. , 0. , 1., 1.  ) ; main_pad .Draw()
    main_pad.SetTicks(True)
    main_pad.SetTopMargin(0.15)
    main_pad.SetBottomMargin(0.15)
    main_pad.SetLeftMargin(0.15)
    main_pad.SetRightMargin(0.15)
    main_pad.cd()
    h_1dxy_lnt.GetXaxis().SetNoExponent()
    h_1dxy_lnt.GetXaxis().SetMoreLogLabels()
    h_1dxy_lnt.DrawNormalized('histe')
    h_1dxy_t.DrawNormalized('histesame')
    main_pad.BuildLegend(0.62, 0.6,0.82,0.7)
    show_logo_in_prog()
    show_lumi('2018, L = 59.7 fb^{-1}, 13 TeV')
    main_pad.SetLogx()
    can.Modified(); can.Update()
    can.SaveAs('plots/llp/dxy.pdf')
    can.SaveAs('plots/llp/dxy.root')

if disp:
    can = Canvas(width=700, height=700) ; can.Draw()
    can.cd() ; main_pad  = Pad(0. , 0. , 1., 1.  ) ; main_pad .Draw()
    main_pad.SetTicks(True)
    main_pad.SetTopMargin(0.15)
    main_pad.SetBottomMargin(0.15)
    main_pad.SetLeftMargin(0.15)
    main_pad.SetRightMargin(0.15)
    main_pad.cd()
    h_disp_lnt.GetXaxis().SetNoExponent()
    h_disp_lnt.GetXaxis().SetMoreLogLabels()
    h_disp_lnt.DrawNormalized('histe')
    h_disp_t.DrawNormalized('histesame')
    main_pad.BuildLegend(0.62, 0.6,0.82,0.7)
    show_logo_in_prog()
    show_lumi('2018, L = 59.7 fb^{-1}, 13 TeV')
    main_pad.SetLogx()
    can.Modified(); can.Update()
    can.SaveAs('plots/llp/disp.pdf')
    can.SaveAs('plots/llp/disp.root')

if dr:
    can = Canvas(width=700, height=700) ; can.Draw()
    can.cd() ; main_pad  = Pad(0. , 0. , 1., 1.  ) ; main_pad .Draw()
    main_pad.SetTicks(True)
    main_pad.SetTopMargin(0.15)
    main_pad.SetBottomMargin(0.15)
    main_pad.SetLeftMargin(0.15)
    main_pad.SetRightMargin(0.15)
    main_pad.cd()
    h_dr12_lnt.DrawNormalized('histe')
    h_dr12_t.DrawNormalized('histesame')
    main_pad.BuildLegend(0.62, 0.6,0.82,0.7)
    show_logo_in_prog()
    show_lumi('2018, L = 59.7 fb^{-1}, 13 TeV')
    can.Modified(); can.Update()
    can.SaveAs('plots/llp/dr12.pdf')
    can.SaveAs('plots/llp/dr12.root')
    
if sv:
    can = Canvas(width=700, height=700) ; can.Draw()
    can.cd() ; main_pad  = Pad(0. , 0. , 1., 1.  ) ; main_pad .Draw()
    main_pad.SetTicks(True)
    main_pad.SetTopMargin(0.15)
    main_pad.SetBottomMargin(0.15)
    main_pad.SetLeftMargin(0.15)
    main_pad.SetRightMargin(0.15)
    main_pad.cd()
    h_sv_cos_lnt.DrawNormalized('histe')
    h_sv_cos_t.DrawNormalized('histesame')
    main_pad.BuildLegend(0.62, 0.6,0.82,0.7)
    show_logo_in_prog()
    show_lumi('2018, L = 59.7 fb^{-1}, 13 TeV')
    can.Modified(); can.Update()
    can.SaveAs('plots/llp/sv_cos.pdf')
    can.SaveAs('plots/llp/sv_cos.root')
    
if m12:
    can = Canvas(width=700, height=700) ; can.Draw()
    can.cd() ; main_pad  = Pad(0. , 0. , 1., 1.  ) ; main_pad .Draw()
    main_pad.SetTicks(True)
    main_pad.SetTopMargin(0.15)
    main_pad.SetBottomMargin(0.15)
    main_pad.SetLeftMargin(0.15)
    main_pad.SetRightMargin(0.15)
    main_pad.cd()
    h_m12_lnt.DrawNormalized('histe')
    h_m12_t.DrawNormalized('histesame')
    main_pad.BuildLegend(0.62, 0.6,0.82,0.7)
    show_logo_in_prog()
    show_lumi('2018, L = 59.7 fb^{-1}, 13 TeV')
    can.Modified(); can.Update()
    can.SaveAs('plots/llp/m12.pdf')
    can.SaveAs('plots/llp/m12.root')

