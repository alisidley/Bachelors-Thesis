from ROOT import (
    ROOT,
    RDataFrame,
    TCanvas
)

ROOT.EnableImplicitMT()

#get file and tree from directory                                               
                        
minbias_ntuple = "/user/egovorko/work/public/minbias_JpsiPhi.root"
signal_ntuple = "/data/bfys/valukash/forAli/DaVinci_jpsiphi_MC_upgrade.root"
input_tree_name = "Bs2jpsiphi/DecayTree"

minbias_df = RDataFrame(input_tree_name, minbias_ntuple)
signal_df = RDataFrame(input_tree_name, signal_ntuple)
PIDmu_cut = "eventmuons_PIDmu[eventmuons_PIDmu > 0].size() >= 1"
#pt_cut = "eventmuons_PT[eventmuons_PT > 500].size() >= 1"
minbias_pidmu = minbias_df.Filter(PIDmu_cut)
#minbias_pt = minbias_pidmu.Filter(pt_cut)
signal_pidmu = signal_df.Filter(PIDmu_cut)
#signal_pt = signal_pidmu.Filter(pt_cut)

c1 = TCanvas()
c1.Divide(2,2)
c1.cd(1)
pidmu1 = minbias_df.Histo1D("eventmuons_PIDmu")
pidmu1.SetTitle("Event muon PIDmu distribution (min bias)")
pidmu1.GetXaxis().SetTitle("PIDmu")
pidmu1.Draw()
c1.cd(2)
pidmu2 = signal_df.Histo1D("eventmuons_PIDmu")
pidmu2.SetTitle("Event muon PIDmu distribution (signal)")
pidmu2.GetXaxis().SetTitle("PIDmu")
pidmu2.SetLineColor(2)
pidmu2.Draw()
c1.cd(3)
pt1 = minbias_df.Histo1D("eventmuons_PT")
pt1.SetTitle("Event muon PT distribution (min bias)")
pt1.GetXaxis().SetTitle("pt")
pt1.GetXaxis().SetLimits(0,500)
pt1.Draw()
c1.cd(4)
pt2 = signal_df.Histo1D("eventmuons_PT")
pt2.SetTitle("Event muon PT distribution (signal)")
pt2.GetXaxis().SetLimits(0,500)
pt2.SetLineColor(2)
pt2.GetXaxis().SetTitle("pt")
pt2.Draw()
