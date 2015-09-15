from ROOT import gROOT, TCanvas, TF1
from ROOT import TFile, TDirectory, TTree
from ROOT import AddressOf



#The user can find a number of examples in $ROOTSYS/tutorials/pyroot


gROOT.ProcessLine(
"struct MyStruct {\
   Int_t     run_num;\
   Int_t     lumi_num;\
   Int_t     event_num;\
   Int_t     lumi;\
   Int_t     pileup;\
};" );


##gROOT.ProcessLine(
##"struct MyStruct {\
##   Int_t     run_num;\
##   Int_t     lumi_num;\
##   Int_t     event_num;\
##   Int_t     lumi;\
##   Int_t     pileup;\
##   Char_t    fMyCode[4];\
##};" );


from ROOT import MyStruct
parameters = MyStruct()

 
print "START"


#make the output root file
file_obj = TFile("Make_Dir_Tree_MultiLeaveBranch1_OUTPUT.root", "RECREATE")

#declare + initilze directory
dir_obj = file_obj.mkdir("name_of_directory")

##this goes to the directory we just created, tree will be put in there
##if you want tree to just be put in the master directory (root file), just dont include this command
file_obj.cd("name_of_directory")

##declare and iniltize TTree
tree_obj = TTree("rttreename", "disciption")


##create a Branch, with leaves
tree_obj.Branch("Name_of_branch", parameters, "the_run_number/I:the_lumi_number/I:the_event_number/I:the_lumi/I:the_pileup/I");


for i in range(0, 10):

    parameters.run_num = 1 * i
    parameters.lumi_num = 2 * i
    parameters.event_num = 3 * i
    parameters.lumi = 4 * i
    parameters.pileup = 5 * i
    tree_obj.Fill()

    print i


#write to the output root file
file_obj.Write()



print "END"
