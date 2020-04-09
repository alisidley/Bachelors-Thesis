from ROOT import (
    ROOT, 
    RDataFrame,
)

ROOT.EnableImplicitMT()
#get file and tree from directory
input_ntuple = "/data/bfys/jdevries/gangadir/workspace/jdevries/LocalXML/135/DaVinci_jpsiphiNtuple_MC_minbiasupgrade.root"
input_tree_name = "Bs2jpsiphi/DecayTree"
dataframe = RDataFrame(input_tree_name, input_ntuple)
cuts = "(Bs_M > 5150) && (Bs_M < 5550) && (Jpsi_M > 3020) && (Jpsi_M < 3170) && (Phi_M > 980) && (Phi_M < 1050) && (muplus_PT > 500) && (mumin_PT > 500) && ((Bs_ENDVERTEX_CHI2/Bs_ENDVERT\
EX_NDOF) < 20) && (Jpsi_ENDVERTEX_CHI2/Jpsi_ENDVERTEX_NDOF < 16) && (Phi_ENDVERTEX_CHI2/Phi_ENDVERTEX_NDOF < 25)"
df_cuts = dataframe.Filter(cuts)

nentries = df_cuts.Count()
print(nentries)

df_right_tag = dataframe.Filter("(Bs_OSMuon_TAGDEC == 1 && Bs_TRUEID == 1) || (Bs_OSMuon_TAGDEC == -1 && Bs_TRUEID == -1)")
df_wrong_tag = dataframe.Filter("(Bs_OSMuon_TAGDEC == 1 && Bs_TRUEID != 1) || (Bs_OSMuon_TAGDEC == -1 && Bs_TRUEID != -1)")
df_untagged = dataframe.Filter("Bs_OSMuon_TAGDEC = 0")

R = df_right_tag.Count().GetValue()
W = df_wrong_tag.Count().GetValue()
U = df_untagged.Count().GetValue()
print(R)
print(W)
print(U)

tag_eff = (R + W) / (R + W + U)
print(tag_eff)
