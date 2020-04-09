from __future__ import division
from ROOT import *
import numpy as np

#get file and tree from directory
file = TFile("/data/bfys/jdevries/gangadir/workspace/jdevries/LocalXML/135/DaVinci_jpsiphiNtuple_MC_minbiasupgrade.root")
tree = file.Get("Bs2jpsiphi/DecayTree")

#function that calculates efficiency given lifetime cut
def tag_eff(cut):
    cut1 = TCut("(Bs_M > 5150) && (Bs_M < 5550) && (Jpsi_M > 3020) && (Jpsi_M < 3170) && (Phi_M > 980) && (Phi_M < 1050) && (muplus_PT > 500) && (mumin_PT > 500) && ((Bs_ENDVERTEX_CHI2/Bs_ENDVERTEX_NDOF) < 20) && (Jpsi_ENDVERTEX_CHI2/Jpsi_ENDVERTEX_NDOF < 16) && (Phi_ENDVERTEX_CHI2/Phi_ENDVERTEX_NDOF < 25)")
    tree.Draw("Bs_TAU>>myhisto(lifetime,100,0,0.02)", cut1)
    myHisto = gDirectory.Get("myhisto")
    nentries = myHisto.GetEntries()
    print(nentries)
    R = 0
    W = 0
    U = 0
    for i in range(int(nentries)):
        tree.GetEntry(i)
        if tree.Bs_TAU > cut:
            if (tree.Bs_OSMuon_TAGDEC == 1 and tree.Bs_TRUEID == 1) or (tree.Bs_OSMuon_TAGDEC == -1 and tree.Bs_TRUEID == -1): 
                R += 1
            elif (tree.Bs_OSMuon_TAGDEC == 1 and tree.Bs_TRUEID != 1) or (tree.Bs_OSMuon_TAGDEC == -1 and tree.Bs_TRUEID != -1):
                W += 1
            else:
                U += 1
        else:
            continue
    eff = (R + W) / (R + W + U)
    return eff
#print("test: " + str(tag_eff(0.0002)))

#function that loops over 100 cuts and calculates efficiency at each one; returns vectors
def tag_eff_loop(xmin, xmax):
    cut_array = []
    effi_array = []
    for i in np.linspace(xmin, xmax, 50):
        effi = tag_eff(i)
        cut_array.append(i)
        effi_array.append(effi)
    cut_vector = TVectorD(len(cut_array))
    effi_vector = TVectorD(len(cut_array))
    for i in range(len(cut_array)):
        cut_vector[i] = cut_array[i]
        effi_vector[i] = effi_array[i]
    return(cut_vector, effi_vector)

#plot efficiency vs cut
efftau = tag_eff_loop(0, 0.00002)
c = efftau[0]
eff = efftau[1]
c2 = TCanvas("Tagging Efficiency vs Lifetime Cut")
efftau_plot = TGraph(c, eff)
efftau_plot.SetTitle("OSmuon tagging efficiency as a function of lifetime cut")
efftau_plot.GetXaxis().SetTitle("tau cut")
efftau_plot.GetYaxis().SetTitle("tagging efficiency")
efftau_plot.Draw()
c2.Update()


