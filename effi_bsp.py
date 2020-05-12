from ROOT import (
    ROOT, 
    RDataFrame,
    TCanvas,
    TH1D
)
import numpy as np

ROOT.EnableImplicitMT()

#get file and tree from directory
input_ntuple = "/data/bfys/valukash/forAli/DaVinci_jpsiphi_MC_upgrade.root"
input_tree_name = "Bs2jpsiphi/DecayTree"

dataframe = RDataFrame(input_tree_name, input_ntuple)
#dataframe_with_truep = dataframe.Define('Bs_momentum', 'pow( Bs_TRUEP_X*Bs_TRUEP_X + Bs_TRUEP_Y*Bs_TRUEP_Y + Bs_TRUEP_Z*Bs_TRUEP_Z , 0.5)')
df_bkg = dataframe.Filter("Bs_BKGCAT == 0 || Bs_BKGCAT == 50")
#df_cuts1 = dataframe_with_truep.Filter("(Bs_TAU > 0.0015) && (Bs_M > 5150) && (Bs_M < 5550) && (Jpsi_M > 3020) && (Jpsi_M < 3170) && (Phi_M > 980) && (Phi_M < 1050) && (muplus_PT > 500) && (mumin_PT > 500) && ((Bs_ENDVERTEX_CHI2/Bs_ENDVERTEX_NDOF) < 20) && (Jpsi_ENDVERTEX_CHI2/Jpsi_ENDVERTEX_NDOF < 16) && (Phi_ENDVERTEX_CHI2/Phi_ENDVERTEX_NDOF < 25)", "trigger_cuts")
cut1 = df_bkg.Filter("(Bs_TAU > 0.0015)", "tau_cut")
cut2 = cut1.Filter("(Bs_M > 5150) && (Bs_M < 5550)", "b_mass_cut")
cut3 = cut2.Filter("(Jpsi_M > 3020) && (Jpsi_M < 3170)", "jpsi_mass_cut")
cut4 = cut3.Filter("(Phi_M > 980) && (Phi_M < 1050)", "phi_mass_cut")
cut5 = cut4.Filter("(muplus_PT > 500) && (mumin_PT > 500)", "mu_pt_cut")
cut6 = cut5.Filter("(Bs_ENDVERTEX_CHI2/Bs_ENDVERTEX_NDOF) < 20", "b_vtx_cut")
cut7 = cut6.Filter("(Jpsi_ENDVERTEX_CHI2/Jpsi_ENDVERTEX_NDOF < 16)", "jpsi_vtx_cut")
cut8 = cut7.Filter("(Phi_ENDVERTEX_CHI2/Phi_ENDVERTEX_NDOF < 25)", "phi_vtx_cut")
cut9 = cut8.Filter("mumin_PIDmu > 0 && muplus_PIDmu > 0", "mu_id_cut")
cut10 = cut9.Filter("Kmin_PIDK > 0 && Kplus_PIDK > 0", "k_id_cut")

#print("Mumin eff: ")
#mumincut = cut9.Report()
#mumincut.Print()
print("All stats: ")
cutsreport = dataframe.Report()
cutsreport.Print()

#c1 = TCanvas()
#h = dataframe_with_truep.Histo1D("Bs_momentum")
#num_bins = 10
#from ostap.histos import *
#edges = h.equal_edges(num_bins)
#print(edges)
#h1 = h1_axis(edges, "")
#h1.Draw()
#h2 = df_cuts1.Histo1D("Bs_momentum")
#h2.Draw()
#h3 = h1.Clone()
#h3.Divide(h1, h2)
#h3.Draw
