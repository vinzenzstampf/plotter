from ROOT import TLatex, TStyle, kBird, kTRUE
from ROOT.TGaxis import SetMaxDigits
from ROOT.TH1 import SetDefaultSumw2
from ROOT.gROOT import SetStyle

def set_style():
    style = TStyle('hnl_style','hnl_style')

    style.SetOptStat(0)
    style.SetPalette(kBird) # look up the color palette options in https://root.cern.ch/doc/master/classTColor.html

    # Canvas
    style.SetCanvasDefH(500)
    style.SetCanvasDefW(550)
    
    # Use plain black on white colors
    icol = 0
    style.SetFrameBorderMode(icol)
    style.SetCanvasBorderMode(icol)
    style.SetPadBorderMode(icol)
    style.SetPadColor(icol)
    style.SetCanvasColor(icol)
    style.SetStatColor(icol)

    # Set the paper & margin sizes
    style.SetPaperSize(20,26)
    style.SetPadTopMargin(0.08)
    style.SetPadRightMargin(0.17)
    style.SetPadBottomMargin(0.12)
    style.SetPadLeftMargin(0.15)

    # Use large fonts
    font = 42
    tsize = 0.045
    style.SetTextFont(font)

    # Global Title Properties
    style.SetOptTitle(0)
    style.SetTitleFont(font)
    style.SetTitleSize(tsize)
    style.SetTitleBorderSize(0)
    style.SetTitleColor(1)
    style.SetTitleTextColor(1)
    style.SetTitleFillColor(0)
    style.SetTitleFontSize(tsize)
    style.SetTitleH(0.05)
    style.SetTitleW(0.)
    style.SetTitleStyle(1001)
    style.SetTitleAlign(13)

    # Axis Titles and Labels
    SetMaxDigits(3)
    style.SetTextSize(tsize)
    style.SetLabelFont(font,"x")
    style.SetTitleFont(font,"x")
    style.SetLabelFont(font,"y")
    style.SetTitleFont(font,"y")
    style.SetLabelFont(font,"z")
    style.SetTitleFont(font,"z")

    style.SetLabelSize(tsize,"x")
    style.SetTitleSize(tsize,"x")
    style.SetLabelSize(tsize,"y")
    style.SetTitleSize(tsize,"y")
    style.SetLabelSize(tsize,"z")
    style.SetTitleSize(tsize,"z")

    style.SetTitleOffset(1.1,"x")
    style.SetTitleOffset(1.3,"y")
    style.SetTitleOffset(1.35,"z")

    style.SetMarkerStyle(20)
    style.SetMarkerSize(0.75)
    style.SetLineWidth(1)
    # style.SetHistLineWidth(2.)
    style.SetLineStyleString(2,'[12 12]') # postscript dashes
    
    # Draw horizontal and vertical grids
    style.SetPadGridX(kTRUE)
    style.SetPadGridY(kTRUE)
    style.SetGridStyle(3)
    style.SetPadTickX(1)
    style.SetPadTickY(1)

    # Legend
    style.SetLegendBorderSize(1)
    style.SetLegendFont(font)
    # style.SetFillColor(0) # White
    # style.SetfillStyle(4000) # Transparent
   
    #Statistics
    style.SetOptFit(111)
    style.SetStatX(.80)
    style.SetStatY(0.26)
    style.SetStatBorderSize(1)
    style.SetStatW(0.16)
    style.SetStatH(0.15)
    style.SetStatFont(font)
    style.SetStatFontSize(0.01)
    
    # for 'colztexte' restrict digits after comma
    style.SetPaintTextFormat('4.2f')

    # When this static function is called with sumw2=kTRUE, all new histograms will automatically activate the storage of the sum of squares of errors
    SetDefaultSumw2()

    SetStyle('hnl_style')

def draw_logo_prelim():
    logo = TLatex()
    logo.SetNDC()
    logo.SetTextAlign(11)
    logo.SetTextFont(61)
    logo.SetTextSize(0.045)
    logo.DrawLatex(0.15,0.94,'CMS')
    
    preliminary = TLatex()
    preliminary.SetNDC()
    preliminary.SetTextAlign(11)
    preliminary.SetTextFont(52)
    preliminary.SetTextSize(0.038)
    preliminary.DrawLatex(0.24,0.94,'Preliminary')
