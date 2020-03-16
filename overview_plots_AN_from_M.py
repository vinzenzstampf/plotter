#from martina


TH1D *HistDiv(TH1D *h1, TH1D *h2, const bool abs)
  TH1D *h1c = (TH1D*) h1.Clone()
  TH1D *h2c = (TH1D*) h2.Clone()
  if(!abs)
    h1c.Scale(1/h1c.Integral(), 'width')
    h2c.Scale(1/h2c.Integral(), 'width')
  
  h1c.Divide(h2c)


void yieldOrder(TH1D**& hists, unsigned* histInd, const unsigned nHist)
  unsigned ordered[nHist]
  for(unsigned h = 0 h < nHist ++h) ordered[h] = 999
  for(unsigned h = 0 h < nHist ++h)
    #unsigned maxH = 999
    double maxYield = -9999.
    for(unsigned k = 0 k <nHist ++k)
      bool found = false
      for(unsigned i = 0 i < nHist ++i)
	if(ordered[i] == k)
	  found = true
	  break
	
      
      if(!found)
	double yield = hists[k].GetSumOfWeights()
	if(yield > maxYield)
	  maxYield = yield
	  #maxH = k
	
     
    
    #ordered[h] = maxH
    ordered[h] = h
        
  
  TH1D* histC[nHist]
  for(unsigned h = 0 h < nHist ++h)
    histC[h] = (TH1D*) hists[ordered[h]].Clone()
    histInd[h] = ordered[h]
  
  for(unsigned h = 0 h < nHist ++h)
    hists[h] = (TH1D*) histC[h].Clone()
  


    
  #Order background histograms in terms of yields
  unsigned histI[nHist]
  yieldOrder(bkg, histI, nHist)
  #Calculate total Bkg yields
  TH1D* bkgTot = (TH1D*) bkg[0].Clone()
  for(unsigned int i = 1 i <  nHist ++i)
    bkgTot.Add(bkg[i])
  
# create stack containing all backgrounds
bkgStack = rt.THStack('bkgStack', 'bkgStack')
for(int effsam = nHist -1 effsam > -1  --effsam):
	bkg[effsam].SetLineColor(colors[effsam])
    bkg[effsam].SetMarkerColor(colors[effsam])
    bkg[effsam].SetLineWidth(2)

	bkg[effsam].SetFillColor(colors[effsam])
	bkg[effsam].SetLineWidth(1)
	bkg[effsam].SetLineColor(colors[effsam])
    #if (names[histI[effsam] + 1 + nSig] == 'nonprompt DF' ) bkg[effsam].SetFillStyle(3020) 
    bkgStack.Add(bkg[effsam], 'f')
  
    
# legend for data and all backgrounds
legend = rt.TLegend(0.16,0.75,0.92,0.87)#,NULL,'brNDC')
legend.SetFillStyle(0)

  const int signal_out= 14	 
  int list_signal_out[signal_out] = [1,3,4,5,6,7,9,11,13,14,15,16,17,19]
	  
  for(int effsam = nHist - 1 effsam > -1 --effsam)
legend.SetTextFont(42)
legend.AddEntry(bkg[effsam], 'nonprompt')
legend.AddEntry(bkg[effsam], 'prompt')
legend.SetNColumns(4)

 	
labels_sr=['0-0.5','0.5-1.5','1.5-4','>4','0-0.5','0.5-1.5','1.5-4','>4',
		   '0-0.5','0.5-1.5','1.5-4','>4','0-0.5','0.5-1.5','1.5-4','>4',
		   '0-0.5','0.5-1.5','1.5-4','>4','0-0.5','0.5-1.5','1.5-4','>4']



data.SetStats(0)
data.GetXaxis().LabelsOption('vu')
data.GetXaxis().SetTitle ('#Delta (PV-SV)_2D (cm)')	  
data.GetXaxis().SetTitleSize(0.06)
data.GetXaxis().SetTitleOffset(1.1)
data.GetXaxis().SetTitleFont(132)

# bin labels
for (int i =0 i<24 i++)	  
  data.GetXaxis().SetBinLabel(i+1, labels_sr[i])

data.GetXaxis().SetLabelSize(0.045)
data.GetXaxis().SetLabelOffset(0.005)
data.GetXaxis().SetLabelSize(0.045)
data.GetXaxis().SetLabelOffset(0.005)	    	    

   
    
# canvas and pads
width  = 800
height = 500

c = rt.TCanvas(name_histo,'',width*(1-xPad),height)   #1000/500
c.cd()

# data and MC yields in first pad
p1 = rt.TPad(name_histo,'',0,xPad,1,1)
p1.Draw()
p1.cd()
p1.SetTopMargin(0.1) #0.1*(width*(1-xPad)/650) FIXME CHANGE THIS BACK
p1.SetBottomMargin(0.)
bkgTot.SetFillStyle(3005)
bkgTot.SetFillColor(kGray+2)
bkgTot.SetMarkerStyle(1)
data.SetMinimum(0.1)
bkgTot.SetMinimum(0.1)
bkgStack.SetMinimum(0.1)

data.GetXaxis().SetTitleFont(42)
data.GetYaxis().SetTitleFont(42)
data.GetXaxis().SetLabelSize(0.1)
data.GetXaxis().SetTitleSize(0.07)
data.GetYaxis().SetLabelSize(0.04)
data.GetYaxis().SetTitleSize(0.07)

data.SetMaximum(data.GetBinContent(data.GetMaximumBin())*1.5)
data.GetYaxis().SetRangeUser(0.1,data.GetBinContent(data.GetMaximumBin())*1.5)

  
data.SetMarkerStyle(20)
data.SetMarkerColor(1)
data.SetLineColor(1) 
data.Draw('pe')	#The range used is now that of the data histogra
bkgStack.Draw('hist same')
data.Draw('pe same')
legend.AddEntry(data, 'data')
legend.Draw('same')
bkgTot.Draw('e2same')
  

high_flav=(data.GetBinContent(data.GetMaximumBin())*1.2)*2
high_mll=data.GetBinContent(data.GetMaximumBin())*1.05
left_mll=0.97

  
line0 = rt.TLine(8.5,0.07,8.5, high_flav/2)
line0.SetLineWidth(2)
line0.Draw()

line1 = rt.TLine(16.5,0.07,16.5, high_flav/2)
line1.SetLineWidth(2)
line1.Draw()

line2 = rt.TLine(4.5,high_mll,4.5,0.1)
#ci = TColor::GetColor('#ff6600')
line2.SetLineStyle(2)
line2.SetLineWidth(1)
line2.Draw()
line3 = rt.TLine(12.5,high_mll,12.5,0.1)
#ci = TColor::GetColor('#ff6600')
line3.SetLineStyle(2)
line3.SetLineWidth(1)
line3.Draw()
line4 = rt.TLine(20.5,high_mll,20.5,0.1)
#ci = TColor::GetColor('#ff6600')
line4.SetLineStyle(2)
line4.SetLineWidth(1)
line4.Draw()


tex0 = rt.TLatex(0.8748578,17546.74,'')
tex0 = rt.TLatex(left_mll,high_mll,'M_ll < 4 GeV')
tex0.SetTextSize(0.03)
tex0.SetTextFont(42)
tex0.SetLineWidth(2)
tex0.Draw()
tex1 = rt.TLatex(left_mll+4,high_mll,'M_ll > 4 GeV')
tex1.SetTextSize(0.03)
tex1.SetTextFont(42)
tex1.SetLineWidth(2)
tex1.Draw()

tex2 = rt.TLatex(left_mll+8,high_mll,'M_ll < 4 GeV')
tex2.SetTextSize(0.03)
tex2.SetTextFont(42)
tex2.SetLineWidth(2)
tex2.Draw()
tex2 = rt.TLatex(left_mll+12,high_mll,'M_ll > 4 GeV')
tex2.SetTextSize(0.03)
tex2.SetTextFont(42)
tex2.SetLineWidth(2)
tex2.Draw()

tex3 = rt.TLatex(left_mll+16,high_mll,'M_ll < 4 GeV')
tex3.SetTextSize(0.03)
tex3.SetTextFont(42)
tex3.SetLineWidth(2)
tex3.Draw()
tex4 = rt.TLatex(left_mll+20,high_mll,'M_ll > 4 GeV')
tex4.SetTextSize(0.03)
tex4.SetTextFont(42)
tex4.SetLineWidth(2)
tex4.Draw()
   
			
# mu channels

tex = rt.TLatex(3.857013,high_flav/2,'#mu#mu#mu')
tex.SetTextColor(1)
tex.SetTextSize(0.06)
tex.SetLineWidth(2)
tex.Draw()
tex = rt.TLatex(10.857013,high_flav/2,'#mu^#pm#mu^#mpe')
tex.SetTextColor(1)
tex.SetTextSize(0.06)
tex.SetLineWidth(2)
tex.Draw()
tex = rt.TLatex(17.857013,high_flav/2,'#mu^#pm#mu^#pme')
tex.SetTextColor(1)
tex.SetTextSize(0.06)
tex.SetLineWidth(2)
tex.Draw()
    	
# e channels
tex = rt.TLatex(3.857013,high_flav/2,'eee')
tex.SetTextColor(1)
tex.SetTextSize(0.06)
tex.SetLineWidth(2)
tex.Draw()
tex = rt.TLatex(10,high_flav/2,'e^#pme^#mp#mu')
tex.SetTextColor(1)
tex.SetTextSize(0.06)
tex.SetLineWidth(2)
tex.Draw()
tex = rt.TLatex(17.857013,high_flav/2,'e^#pme^#pm#mu')
tex.SetTextColor(1)
tex.SetTextSize(0.06)
tex.SetLineWidth(2)
tex.Draw()
    	
  
  



