from ROOT import (
    ROOT, 
    RDataFrame,
)

ROOT.EnableImplicitMT()

#get file and tree from directory
input_ntuple = "/data/bfys/valukash/forAli/DaVinci_jpsiphi_MC_upgrade.root"
input_tree_name = "Bs2jpsiphi/DecayTree"

dataframe = RDataFrame(input_tree_name, input_ntuple)
trigger_cuts = "(Bs_TAU > 0.0015) && (Bs_M > 5150) && (Bs_M < 5550) && (Jpsi_M > 3020) && (Jpsi_M < 3170) && (Phi_M > 980) && (Phi_M < 1050) && (muplus_PT > 500) && (mumin_PT > 500) && ((Bs_ENDVERTEX_CHI2/Bs_ENDVERTEX_NDOF) < 20) && (Jpsi_ENDVERTEX_CHI2/Jpsi_ENDVERTEX_NDOF < 16) && (Phi_ENDVERTEX_CHI2/Phi_ENDVERTEX_NDOF < 25)"
muon_cuts = "!eventmuons_BPVIPCHI2[eventmuons_BPVIPCHI2 < 8].empty() && Bs_len > 0" 
df_cuts1 = dataframe.Filter(trigger_cuts)
df_cuts2 = df_cuts1.Filter(muon_cuts)

nentries = dataframe.Count().GetValue()
ntriggered = df_cuts1.Count().GetValue()
ncut = df_cuts2.Count().GetValue()
print("entries: " + str(nentries))
print("triggered: " + str(ntriggered))
print("cut: " + str(ncut))

TrueBs = df_cuts2.Filter("Bs_TRUEID == 531").Count().GetValue()
TrueBsbar = df_cuts2.Filter("Bs_TRUEID == -531").Count().GetValue()

#define right tags, wrong tags and untagged; tagging efficiency, mistag probability and tagging performance 
R = df_cuts2.Filter("(Bs_OSMuon_TAGDEC == 1 && Bs_TRUEID == 531) || (Bs_OSMuon_TAGDEC == -1 && Bs_TRUEID == -531)").Count().GetValue()
W = df_cuts2.Filter("(Bs_OSMuon_TAGDEC == 1 && Bs_TRUEID != 531) || (Bs_OSMuon_TAGDEC == -1 && Bs_TRUEID != -531)").Count().GetValue()
U = df_cuts2.Filter("Bs_OSMuon_TAGDEC == 0").Count().GetValue()
print("R, W, U: ")
print(R)
print(W)
print(U)

tag_eff = (R + W) / (R + W + U)
mistag_prob = W/(R + W + U)
tag_performance = tag_eff*(1-2*mistag_prob)**2

print("Tagging efficiency = " + str(tag_eff))
print("Mistag probability = " + str(mistag_prob))
print("Tagging performance = " + str(tag_performance))
print("True Bs0: " + str(TrueBs))
print("True Bs0bar: " + str(TrueBsbar))
