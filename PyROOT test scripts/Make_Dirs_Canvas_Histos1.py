from ROOT import gROOT, TCanvas, TF1
from ROOT import TFile, TDirectory, TTree
from ROOT import AddressOf

from ROOT import TH1D, TObjArray, TProfile

#The user can find a number of examples in $ROOTSYS/tutorials/pyroot



 
print "START"




nbins = 1000
xmin = 0
xmax = 100


##initilize histos
h_run_num = TH1D("run_num","title;x-axis;y-axis", nbins, xmin, xmax)
h_lumi_num = TH1D("lumi_num","title;x-axis;y-axis", nbins, xmin, xmax)
h_event_num = TH1D("event_num","title;x-axis;y-axis", nbins, xmin, xmax)
h_lumi = TH1D("lumi","title;x-axis;y-axis", nbins, xmin, xmax)
h_pileup = TH1D("pileup","title;x-axis;y-axis", nbins, xmin, xmax)
h_occ = TH1D("occ", "title;x-axis;y-axis", nbins, xmin, xmax)
h_p = TH1D("p","title;x-axis;y-axis", nbins, xmin, xmax)
h_pt = TH1D("pt","title;x-axis;y-axis", nbins, xmin, xmax)
h_xvar = TH1D("xvar","title;x-axis;y-axis", nbins, xmin, xmax)
h_yvar = TH1D("yvar", "title;x-axis;y-axis", nbins, xmin, xmax)

h_xbin = TH1D("xbin", "title;x-axis;y-axis", nbins, xmin, xmax)
h_xmin = TH1D("xmin", "title;x-axis;y-axis", nbins, xmin, xmax)
h_xmax = TH1D("xmax", "title;x-axis;y-axis", nbins, xmin, xmax)






##fill histos
for i in range(0,10):
    h_run_num.Fill(1*i)
    h_lumi_num.Fill(2*i)
    h_event_num.Fill(3*i)
    h_lumi.Fill(4*i)
    h_pileup.Fill(5*i)
    h_occ.Fill(6*i)
    h_p.Fill(7*i)
    h_pt.Fill(8*i)
    h_xvar.Fill(9*i)
    h_yvar.Fill(10*i)

    h_xbin.Fill(11*i)
    h_xmin.Fill(12*i)
    h_xmax.Fill(13*i)





##initilze histo arrays
HList1 = TObjArray(0)
HList2 = TObjArray(0)
HList3 = TObjArray(0)
HList4 = TObjArray(0)
HList5 = TObjArray(0)
HList6 = TObjArray(0)
HList7 = TObjArray(0)


c2 = TCanvas("c2","discription of c2");
c3 = TCanvas("c3","discription of c3");


##set current canvas to c2
c2.cd() 
h_xbin.Draw()


c3.Divide(2,1) #divide canvas c3, into 2 row and 1 col
c3.cd(1) #set the current pad to the first of c3 canvas
h_xmin.Draw()
c3.cd(2) #set the current pad to the second of c3 cavas
h_xmax.Draw()



#add histograms to histo arrays
HList1.Add(h_run_num)
HList1.Add(h_lumi_num)
HList2.Add(h_event_num)
HList2.Add(h_lumi)
HList3.Add(h_pileup)
HList3.Add(h_occ)
HList4.Add(h_p)
HList4.Add(h_pt)
HList5.Add(h_xvar)
HList5.Add(h_yvar)

HList6.Add(c2)
HList7.Add(c3)





##make the output root file
file_obj = TFile("Make_Dirs_Canvas_Histos1_OUTPUT.root", "RECREATE")

file_obj.Append(c2)



##declare + initilze directories
dir1_obj = file_obj.mkdir("directory1")
dir2_obj = file_obj.mkdir("directory2")
##make subdirectory
dir1_obj.mkdir("subdirectory1")
dir2_obj.mkdir("subdirectory2")

##/This is written directoy to the main directory
HList1.Write()
HList6.Write()

##write to directory1
file_obj.cd("directory1")
HList2.Write()
HList7.Write()

##write to directory2
file_obj.cd("directory2")
HList3.Write()

##write to subdirectory1
file_obj.cd("directory1/subdirectory1")
HList4.Write()

##write to subdirectory2
file_obj.cd("directory2/subdirectory2")
HList5.Write()


##write to the output root file
file_obj.Write()



print "END"
