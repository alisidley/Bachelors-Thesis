from ROOT import (
    ROOT, 
    RDataFrame,
)

ROOT.EnableImplicitMT()
#get file and tree from directory
input_ntuple = "/data/bfys/katya/forAli/DaVinci_jpsiphi_MC_upgrade.root"
input_tree_name = "Bs2jpsiphi/DecayTree"
dataframe = RDataFrame(input_tree_name, input_ntuple)
trigger_cuts = "(Bs_M > 5150) && (Bs_M < 5550) && (Jpsi_M > 3020) && (Jpsi_M < 3170) && (Phi_M > 980) && (Phi_M < 1050) && (muplus_PT > 500) && (mumin_PT > 500) && ((Bs_ENDVERTEX_CHI2/Bs_ENDVERT\
EX_NDOF) < 20) && (Jpsi_ENDVERTEX_CHI2/Jpsi_ENDVERTEX_NDOF < 16) && (Phi_ENDVERTEX_CHI2/Phi_ENDVERTEX_NDOF < 25)"
muon_cuts = '!eventmuons_P.empty() && eventmuons_PT > 1500' 
df_cuts = dataframe.Filter(trigger_cuts, muon_cuts)

nentries = dataframe.Count().GetValue()
ntriggered = df_cuts.Count().GetValue()

TrueBs = df_cuts.Filter("Bs_TRUEID == 0")
R = df_cuts.Filter("(Bs_OSMuon_TAGDEC == 1 && Bs_TRUEID == 531) || (Bs_OSMuon_TAGDEC == -1 && Bs_TRUEID == -531)").Count().GetValue()
W = df_cuts.Filter("(Bs_OSMuon_TAGDEC == 1 && Bs_TRUEID != 531) || (Bs_OSMuon_TAGDEC == -1 && Bs_TRUEID != -531)").Count().GetValue()
U = df_cuts.Filter("Bs_OSMuon_TAGDEC == 0").Count().GetValue()
rate = ntriggered / nentries
print(R)
print(W)
print(U)
nTrueBs = TrueBs.Count().GetValue()
tag_eff = (R + W) / (R + W + U)
mistag_prob = R/(R + W + U)
tag_performance = tag_eff*(1-2*mistag_prob)**2
print("Tagging efficiency = " + str(tag_eff))
print("Mistag probability = " + str(mistag_prob))
print("Tagging performance = " + str(tag_performance))
