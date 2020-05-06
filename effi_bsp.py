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
dataframe_with_truep = dataframe.Define('Bs_momentum', 'pow( Bs_TRUEP_X*Bs_TRUEP_X + Bs_TRUEP_Y*Bs_TRUEP_Y + Bs_TRUEP_Z*Bs_TRUEP_Z , 0.5)')
trigger_cuts = "(Bs_TAU > 0.0015) && (Bs_M > 5150) && (Bs_M < 5550) && (Jpsi_M > 3020) && (Jpsi_M < 3170) && (Phi_M > 980) && (Phi_M < 1050) && (muplus_PT > 500) && (mumin_PT > 500) && ((Bs_ENDVERTEX_CHI2/Bs_ENDVERTEX_NDOF) < 20) && (Jpsi_ENDVERTEX_CHI2/Jpsi_ENDVERTEX_NDOF < 16) && (Phi_ENDVERTEX_CHI2/Phi_ENDVERTEX_NDOF < 25)"
muon_cuts = "!eventmuons_BPVIPCHI2[eventmuons_BPVIPCHI2 < 8].empty() && Bs_len > 0" 
df_cuts1 = dataframe_with_truep.Filter(trigger_cuts)
df_cuts2 = df_cuts1.Filter(muon_cuts)

nentries = dataframe_with_truep.Count().GetValue()
ntriggered = df_cuts1.Count().GetValue()
print(nentries)
print(ntriggered)

c1 = TCanvas()
h1 = TH1D(dataframe_with_truep.Histo1D("Bs_momentum"))
h1.Draw()
h2 = df_cuts1.Histo1D("Bs_momentum")
h2.Draw()
h3 = h1.Clone()
h3.Divide(h1, h2)
#h3.Draw()

