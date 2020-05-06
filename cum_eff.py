from ROOT import (
    ROOT, 
    RDataFrame,
)

ROOT.EnableImplicitMT()

#get file and tree from directory
input_ntuple = "/data/bfys/valukash/forAli/DaVinci_jpsiphi_MC_upgrade.root"
input_tree_name = "Bs2jpsiphi/DecayTree"
dataframe = RDataFrame(input_tree_name, input_ntuple)
nentries = dataframe.Count().GetValue()
bs_tau = "(Bs_TAU > 0.002)"
bs_m = "(Bs_M > 5150) && (Bs_M < 5550)"
jpsi_m = "(Jpsi_M > 3020) && (Jpsi_M < 3170)"
phi_m = "(Phi_M > 980) && (Phi_M < 1050)"
bs_vtx = "(Bs_ENDVERTEX_CHI2/Bs_ENDVERTEX_NDOF < 20)"
jpsi_vtx = "(Jpsi_ENDVERTEX_CHI2/Jpsi_ENDVERTEX_NDOF < 16)"
phi_vtx = "(Phi_ENDVERTEX_CHI2/Phi_ENDVERTEX_NDOF < 25)"
mu_pt = "(muplus_PT > 500) && (mumin_PT > 500)"

trigger_cut_list = [bs_tau, bs_m, jpsi_m, phi_m, bs_vtx, jpsi_vtx, phi_vtx, mu_pt] 
efficiency_list = []
cum_efficiency_list = []
cum_eff_df = dataframe
for i in range(len(trigger_cut_list)):
   eff_df =  dataframe.Filter(trigger_cut_list[i])
   eff = (eff_df.Count().GetValue())/nentries
   efficiency_list.append(eff)

   cum_eff_df = cum_eff_df.Filter(trigger_cut_list[i])
   cum_eff = (cum_eff_df.Count().GetValue())/nentries
   cum_efficiency_list.append(cum_eff)

print(efficiency_list)
print(cum_efficiency_list)


