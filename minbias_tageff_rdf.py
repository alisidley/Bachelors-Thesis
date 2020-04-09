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
cuts_loose = "(Bs_M > 5150) && (Bs_M < 5550)"
df_cuts = dataframe.Filter(cuts_loose)

nentries = df_cuts.Count().GetValue()
print(nentries)

R = df_cuts.Filter("(Bs_OSMuon_TAGDEC == 1 && Bs_TRUEID == 531) || (Bs_OSMuon_TAGDEC == -1 && Bs_TRUEID == -531)").Count().GetValue()
W = df_cuts.Filter("(Bs_OSMuon_TAGDEC == 1 && Bs_TRUEID != 531) || (Bs_OSMuon_TAGDEC == -1 && Bs_TRUEID != -531)").Count().GetValue()
U = df_cuts.Filter("Bs_OSMuon_TAGDEC == 0").Count().GetValue()

print(R)
print(W)
print(U)

tag_eff = (R + W) / (R + W + U)
print(tag_eff)
