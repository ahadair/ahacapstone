///ROOT HEADERS
#include "TTree.h"
#include "TFile.h"
//////////////
//#include <TTree.h>
//#include <TFile.h>

#include <iostream>
#include <dirent.h>
#include <fstream>
#include <string>
#include <windows.h>
#include <stdio.h>
#include <math.h>

//#include "AA_Organization_Tools.h"


using namespace std;


//declare a generic structure type
struct basic_parameters {
	int run_num;
	int lumi_num;
	int event_num;
	int lumi;
	int pileup;
};



int main()
{





cout << "Starting Program" << endl;




//declare an object of type nameofstruct
basic_parameters parameters;


//make the output root file
//TFile *file_obj = new TFile("Make_Dir_Tree_MultiLeaveBranch1_OUTPUT.root", "RECREATE");


////declare + initilze directory
//TDirectory* dir_obj = file_obj->mkdir("name_of_directory");
//
////this goes to the directory we just created, tree will be put in there
////if you want tree to just be put in the master directory (root file), just dont include this command
//file_obj->cd("name_of_directory");
//
////declare and iniltize TTree
//TTree *tree_obj = new TTree("rttreename", "disciption");
//
////create a Branch, with leaves
//tree_obj->Branch("Name_of_branch", &parameters, "the_run_number/I:the_lumi_number/I:the_event_number/I:the_lumi/I:the_pileup/I");
//
//
//
//for (int i = 0; i<10; i++){
//
//	parameters.run_num = 1 * i;
//	parameters.lumi_num = 2 * i;
//	parameters.event_num = 3 * i;
//	parameters.lumi = 4 * i;
//	parameters.pileup = 5 * i;
//
//	//This fills the leaves, using all the info we have put in our struct
//	tree_obj->Fill();
//
//};

//write to the output root file
//file_obj->Write();




cout << "Done" << endl;

return 0;
















//
//
//DIR *Odir;
//struct dirent *Oent;
//char OFilePath[200];
//char OFileName[200];
//int Olinenum = 0;
//int Odirlineskip = 2;
//int OGline = 0;
//
//
//
//char the_input_path[200];
//char the_output_path[200];
//
//
//
//char pprefix[200];
//char nprefix[200];
//char fffolder[200];
//
//
//
//
/////Inputs
////int trim_off_leading_chars = 5; ///tlib_ size = 5
////sprintf(pprefix, "tlib");
////sprintf(fffolder, "tlib - teens like it big");
/////E:\winpop\Sites\Brazzers\tlib - teens like it big\zzz - to sort\tlib
//
//
//
//
/////Inputs tlb - Teens like it Big
//sprintf(pprefix, "tlb");
//sprintf(nprefix, "Teens like it Big");
//
//
//int trim_off_leading_chars = (get_length_of_chararray(pprefix) + 1); ///bab_ size = 4
////cout << trim_off_leading_chars << endl;
//sprintf(fffolder, "%s - %s", pprefix, nprefix);
//sprintf( the_input_path,  "E:\\winpop\\Sites\\Brazzers\\%s\\zzz - to sort\\%s", fffolder, pprefix);
//sprintf( the_output_path, "E:\\winpop\\Sites\\Brazzers\\%s\\zzz - to sort\\test", fffolder);
//sprintf(OFilePath, the_input_path);
//
//
//
//
//
//Odir = opendir (OFilePath);
//
//
//int Split_Position  = -1;
//
//
//if ( Odir != NULL) {
//
//
/////file name, string position
//int FFlength = 300;
//char oldFile  [FFlength][200];
//char newFolder[FFlength][200];
//char newFile  [FFlength][200];
//
//
//
//
//  //print all the files and directories within directory
//  while ((Oent = readdir (Odir)) != NULL) {
//    Olinenum++;
//    OGline = Olinenum - Odirlineskip;
//
//
//    if ( OGline > 0 ){
//
//
//
//    sprintf(OFileName, "%s" , Oent->d_name);
//    sprintf(oldFile[OGline], "%s\\%s", OFilePath, OFileName);
//    //cout << OGline << ": " << oldFile[OGline] << endl;
//
//
//
//    char extension[200]= {'\0'};
//    get_file_extension( OFileName, extension);
//
//    char file_without_extension[200]= {'\0'};
//    get_file_without_extension( OFileName, file_without_extension);
//
//    //cout << file_without_extension << ":" << extension << endl;
//
//    Split_Position  = -1;
//    Split_Position = get_position_of_chars(" - ", OFileName);
//
//
//    char nameLeft[200]= {'\0'};
//    char nameRight[200]= {'\0'};
//    split_chars_keep_both(file_without_extension, Split_Position + 1, nameLeft, nameRight, 2 );
//    //cout << nameLeft << endl;
//    //cout << nameRight << endl;
//
//
//    ///trim off intial bblib_
//    char Actress[200]= {'\0'};
//    get_section_of_chararray(nameLeft, Actress, offset, trim_off_leading_chars, 0); ///bblib_ size = 6
//    //cout << Actress << endl;
//
//
//    ///trim off ending number
//    int numberSS = -1;
//    numberSS = get_position_of_first_number(Actress);
//    //cout << numberSS << endl;
//    if( numberSS > -1){
//    get_section_of_chararray(Actress, Actress, absolute, 0, numberSS - 1);
//    }
//
//    ///trim off ending -
//    numberSS = get_position_of_chars("-", Actress);
//    //cout << numberSS << endl;
//    if( numberSS > -1){
//    get_section_of_chararray(Actress, Actress, absolute, 0, numberSS - 1);
//    }
//
//
//
//
//    ///get names
//    int number_of_deliminators = get_position_of_chars( "_", Actress, direct, forward, -1, true, offset, 0, 0);
//    char Actress_Names[number_of_deliminators + 1][200];
//    //for(int iii = 0; iii < (number_of_deliminators+1); iii++){
//    //Actress_Names[iii] = "\0";
//    //}
//
//    int left_deliminator = -1;
//    int right_deliminator = -1;
//
//    for (int iii = 0 ; iii < number_of_deliminators; iii++){
//
//        right_deliminator = get_position_of_chars( "_", Actress, direct, forward, iii + 1, true, offset, 0, 0);
//        get_section_of_chararray(Actress, Actress_Names[iii], absolute, left_deliminator + 1, right_deliminator - 1);
//        left_deliminator = right_deliminator;
//    }
//
//    right_deliminator = get_length_of_chararray(Actress);
//    get_section_of_chararray(Actress, Actress_Names[number_of_deliminators], absolute, left_deliminator + 1, right_deliminator - 1);
//
//
//
//
//
//    ///capatilize names
//    for(int iii = 0; iii < number_of_deliminators + 1; iii++){
//    capitalize_word (Actress_Names[iii], Actress_Names[iii]);
//    //cout << Actress_Names[iii] << endl;
//    }
//    //cout << Actress << endl;
//
//
//    ///put all actress names back together
//    char All_Names[200] = {'\0'};
//    for(int iii = 0; iii < number_of_deliminators + 1; iii++){
//    sprintf(All_Names, "%s %s", All_Names, Actress_Names[iii]);
//    }
//    //cout << All_Names << endl;
//
//
//
//    ///get folder name
//    char Folder_Name[200] = {'\0'};
//    sprintf(Folder_Name, "%s -%s" , nameRight, All_Names);
//    //cout << Folder_Name << endl;
//
//
//
//
//    ///make directories
//    char Full_Path[200] = {'\0'};
//    sprintf(Full_Path, "%s\\%s", the_output_path, Folder_Name);
//    //cout << OGline << ": " << Full_Path << endl;
//    //make_directory(Full_Path);
//    sprintf(newFolder[OGline], "%s", Full_Path);
//
//
////    sprintf(newFile[OGline], "%s\\%s", Full_Path, OFileName);
////    //cout << OGline << ": " << newFile[OGline] << endl;
//
//
//    /*
//
//    int i = 0;
//    int the_first_number = -1;
//    int the_last_number  = -1;
//    get_first_number_sequence_positions(OFileName, the_first_number, the_last_number);
//    //cout << "(" << the_first_number << ":" << the_last_number << ")" << endl;
//
//    char pre_number_sequence[200];
//    get_section_of_chararray(OFileName, 0, the_first_number-1, pre_number_sequence);
//
//    char the_number_sequence[200];
//    get_section_of_chararray(OFileName, the_first_number, the_last_number, the_number_sequence);
//
//    sprintf(NNFileName, "%s-%s" , pre_number_sequence, the_number_sequence);
//    cout << OGline << ": " << NNFileName << endl;
//
//    sprintf(OldDirName[OGline-1], "%s", OFileName);
//    sprintf(NewDirName[OGline-1], "%s", NNFileName);
//
//    char OldNames[2][200];
//    char NewNames[2][200];
//
//    */
//
//
//
//    /*
//
//    sprintf(NFilePath, "%s\\%s" , OFilePath, OFileName);
//    Ndir = opendir (NFilePath);
//        if (Ndir !=NULL){
//            Nlinenum = 0;
//            while ((Nent = readdir (Ndir)) != NULL) {
//                Nlinenum++;
//                NGline = Nlinenum - Ndirlineskip;
//
//                if ( NGline > 0){
//                sprintf(NFileName, "%s" , Nent->d_name);
//                //cout << OGline << ":" << NGline << " : " << NFileName << endl;
//                sprintf(OldNames[NGline-1],"%s", NFileName);
//                }
//            }
//            closedir (Ndir);
//        }
//        else {
//        //could not open directory
//        perror ("");
//        return EXIT_FAILURE;
//        }
//
//      */
//
//
//      ////File Renames////////////
//      /*
//      char extents[200];
//      char OFileTotal[500];
//      char NFileTotal[500];
//      for(int iii=0; iii<2; iii++){
//
//            get_file_extension( OldNames[iii] , extents);
//            sprintf( NewNames[iii] ,"%s.%s", NNFileName, extents );
//            sprintf(OFileTotal, "%s\\%s", NFilePath, OldNames[iii]);
//            sprintf(NFileTotal, "%s\\%s", NFilePath, NewNames[iii]);
//            cout << OGline << ":" << (iii+1) << " : Old = " << OldNames[iii] << " : New = " << NewNames[iii] << endl;
//            cout << OGline << ":" << (iii+1) << " : Old = " << OFileTotal << " : New = " << NFileTotal << endl;
//
//            ////renames the files, works
//            ////file_rename(OFileTotal, NFileTotal);
//      }
//      */
//      ///////////////////////////
//
//
//
//
//    }
//
//
//  }
//  closedir (Odir);
//
//
//
//  for(int iii = 1; iii < (OGline + 1); iii++){
//
//
//  cout << iii << ": " << newFolder[iii] << endl;
//  //make_directory(newFolder[iii]);
//  cout << iii << ": " << oldFile  [iii] << endl;
//  cout << iii << ": " << newFile  [iii] << endl;
//  //file_rename(oldFile[iii], newFile[iii]);
//  cout << endl;
//
//  }
//
//
//
//
//
//
//}
//else {
//  /* could not open directory */
//  perror ("");
//  return EXIT_FAILURE;
//}


/*

cout << "............................."<< endl;

char NTotal[500];
char OTotal[500];

for(int iii=0; iii< 33; iii++){

sprintf(NTotal, "%s\\%s", OFilePath, NewDirName[iii]);
sprintf(OTotal, "%s\\%s", OFilePath, OldDirName[iii]);

 cout << "(" << iii << ")" << ": olddir = " << OldDirName[iii] << " : newdir = " << NewDirName[iii] << endl;
 cout << "(" << iii << ")" << ": oldtot = " << OTotal << " : newtot = " << NTotal << endl;


  ////renames the folders, works
  ////file_rename(OTotal, NTotal);

}
*/

cout << "............................." << endl;
cout << "Ending Program" << endl;

    return 0;

}
