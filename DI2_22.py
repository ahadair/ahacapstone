#import needed functions
import re, string, os
import csv
import math
from operator import itemgetter


#import ROOT functions
from ROOT import gROOT, TCanvas, TF1
from ROOT import TFile, TDirectory, TTree
from ROOT import AddressOf
from ROOT import TH1D, TH2D, TObjArray, TProfile




def AAcompare(in1, method, in2):
    #Is in1 method in2?
    if method == '=':
        if in1==in2:
            return True
        else:
            return False
    elif method == '>=':
        if in1 >= in2:
            return True
        else:
            return False
    elif method == '<=':
        if in1 <= in2:
            return True
        else:
            return False
    elif method == '>':
        if in1 > in2:
            return True
        else:
            return False
    elif method == '<':
        if in1 < in2:
            return True
        else:
            return False
    else:
        print "AAcompare ERROR"




def AAcompareDict(SPD, SD):
    #SPD = SearchPatternDictonary 2D Dictonary
    #SD = Dictonary to search for
    #Return 1  = Match
    #Return 0  = No Match
    #Return -1 = Keys not found
    #Cycle through SearchPatternDictonary 
    #print "AAcompareDict"

    if type(SPD) is not dict:
        print "AAcompareDict Input1 ERROR "
    if type(SD) is not dict:
        print "AAcompareDict Input2 ERROR "

    for key in SPD.keys():
        #print key
        #if key was not in the Dictonary to search for
        if key not in SD.keys():
            print "Key Not found in" , SD
            return -1
        #key was in the Dictonary to search for
        else:
            SDValue = SD[key]
            SPDValue = SPD[key]
            #Is SubDictonary
            if type(SPDValue) is dict:
                #print "         Is SubDict"
                for subkey in SPDValue.keys():
                    SPDSubValue = SPD[key][subkey]
                    if AAcompare(SDValue, subkey, SPDSubValue) == False:
                        return 0
            #Not subdictonary
            else:
                if AAcompare(SDValue, '=', SPDValue) == False:
                    return 0

    #made it through all tests
    return 1



print "START"


print "Setting Inputs"
DataSetPath = 'DataSets\\FromWebDirect\\100k\\ml-100k\\'
DataFile = 'u.data'
InfoFile = 'u.info'
ItemFile = 'u.item'
GenreFile = 'u.genre'
UserFile = 'u.user'
OccupationFile = 'u.occupation'




DataFullFile       = DataSetPath + DataFile
InfoFullFile       = DataSetPath + InfoFile
ItemFullFile       = DataSetPath + ItemFile
GenreFullFile      = DataSetPath + GenreFile
UserFullFile       = DataSetPath + UserFile
OccupationFullFile = DataSetPath + OccupationFile



#Get Info Dict
print "Getting Info Dict"
InfoDict = {}
with open(InfoFullFile) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        InfoDict[row[0].split()[1]] = row[0].split()[0]
        #InfoDict[row[0].split()[1]] = int(row[0].split()[0])
print InfoDict


#Get Genre Dict
print "Getting Genre Dict"
GenreDict = {}
with open(GenreFullFile) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) == 1:
            if len(row[0].split("|"))==2:
                GenreDict[row[0].split("|")[1]] = row[0].split("|")[0]
print GenreDict


#Genre Binary Code to Dec Code Transform
def AAcombined_genre_to_list(input_number):
    binarystring = bin(input_number)[2:].zfill(19)
    GenreAAList = []
    for i in range(0, 19):
        if binarystring[i] == '1':
            #print GenreDict[str(i)]
            GenreAAList.append(GenreDict[str(i)])
    return GenreAAList
#AADecNumber = 55
#print "Dec =", AADecNumber, ", Binary =", bin(AADecNumber)[2:].zfill(19), ", Genres =", AAcombined_genre_to_list(AADecNumber)


#Get Item Dict
print "Getting Item Dict"
ItemInfo = ['item_id', 'movie_title', 'release_date', 'video_release_date', 'IMDb_URL']
for i in range(0, 19):
    ItemInfo.append('%s' % (i))
ItemDict = {}
with open(ItemFullFile) as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|', fieldnames = ItemInfo)
    for row in reader:
        BinaryString = ''
        for i in range(0, 19):
            if row[str(i)] == '0'  or  row[str(i)] == '1':
                BinaryString = BinaryString + row[str(i)]
            else:
                BinaryString = BinaryString + '0'
        ItemDict[row['item_id']] = {'movie_title': row['movie_title'], 'combined_genre': int(BinaryString,2)}


#Movie ID to Movie Title
def AAItemIDtoTitle(input_number):
    return ItemDict[str(input_number)]['movie_title']


#Movie ID to Genre
def AAItemIDtoGenres(input_number):
    return AAcombined_genre_to_list(int( ItemDict[str(input_number)]['combined_genre']))

##AAItemID = 55
##print "ID =", AAItemID, ", Title =", AAItemIDtoTitle(AAItemID), ", Genres =", AAItemIDtoGenres(AAItemID)

       


OutPutROOTFileName = "DI2_Finalist.root"

#make the output root file
file_obj = TFile(OutPutROOTFileName, "RECREATE")





#ListOfsearchpatternDict = [{ 'item_id': '242', 'rating': {'>=':'3'}}]
#ListOfsearchpatternDict = [{ 'item_id': '242', 'rating': {'>=':'3'}}, { 'item_id': '80', 'rating': {'>=':'3'}} ]
#ListOfsearchpatternDict = [{ 'item_id': '242', 'rating': {'>=':'3'}}, { 'item_id': '80', 'rating': {'>=':'3'}} ]

ListOfsearchpatternDict = []
for aaa in range(1, int(InfoDict['items'])+1):
    ListOfsearchpatternDict.append({ 'item_id': str(aaa), 'rating': {'>=':'3'}})   
#print ListOfsearchpatternDict


#searchpatternDict = { 'item_id': {'=': '242'}, 'rating': {'>=':'3'}}                   
#searchpatternDict = { 'item_id': '242', 'rating': {'>=':'3'}}






# ['Total Rating','Users','Ave Rating','Per of Users','Norm Ave Rating']







aaaindex = 0
for searchpatternDict in ListOfsearchpatternDict:
    print "Running Over = ", aaaindex#, "," , searchpatternDict
    aaaindex = aaaindex + 1

    #print "     GET_USERS_WITH_SIMILAR_TASTES"
    founduserlist = []
    with open(DataFullFile) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t', fieldnames = ['user_id', 'item_id', 'rating', 'timestamp'])
        for row in reader:
            if row['user_id'] not in founduserlist:
                if AAcompareDict(searchpatternDict, row) == 1:
                    founduserlist.append(row['user_id'])
                    
    founduserlist = list(set(founduserlist))
    #print founduserlist



    #print "     GETTTING_SIMILAR_TASTES"
    foundusermoviescoresDict = {}
    with open(DataFullFile) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t', fieldnames = ['user_id', 'item_id', 'rating', 'timestamp'])
        for row in reader:

            if row['user_id'] in founduserlist:

                if row['item_id'] not in foundusermoviescoresDict:
                    foundusermoviescoresDict[row['item_id']] = {'item_id': int(row['item_id']), 'Total Rating' : int(row['rating']), 'Users': int('1')}                
                else:
                    foundusermoviescoresDict[row['item_id']]['Total Rating'] = foundusermoviescoresDict[row['item_id']]['Total Rating'] + int(row['rating'])
                    foundusermoviescoresDict[row['item_id']]['Users'] = foundusermoviescoresDict[row['item_id']]['Users'] + 1

                              

    ##Dict--->List
    foundusermoviescoresList = []
    for key in foundusermoviescoresDict.keys():
        foundusermoviescoresList.append(foundusermoviescoresDict[key])



                    
    for row in foundusermoviescoresList:

        #for similar users
        #total rating divides by the number of users who rated this movie
        row['Ave Rating'] = math.ceil(float(row['Total Rating'])/float(row['Users']) *10)/10
        #percent of similar users who liked this movie
        row['Per of Users'] = math.ceil(float(row['Users'])/float(len(founduserlist))*100)/100
        row['Norm Ave Rating'] = math.ceil(float( row['Ave Rating']*row['Per of Users'])*10)/10


    #print "     MAKING HISTO"
    HList1 = TObjArray(0)
    MovieName = AAItemIDtoTitle(int(searchpatternDict['item_id']))
    SearchStragedy = ' '
    for key in searchpatternDict['rating'].keys():
        SearchStragedy = SearchStragedy + key + " " + searchpatternDict['rating'][key]



    newlist = sorted(foundusermoviescoresList, key=itemgetter('Per of Users'))
    nbinsx = 21
    xmin = 1
    xmax = 5.2
    nbinsy = 50
    ymin = 0
    ymax = 1
    Captions = MovieName + ", Match" + SearchStragedy + " Stars" + "; Ave Rating; Per of Users" 
    Names = MovieName + ' '+ 'Ave Rating vs Per of Users' + ' 2D'
    #print "MAKING HISTO"
    h_yyy = TH2D(Names, Captions, nbinsx, xmin, xmax, nbinsy, ymin, ymax)

    for row in newlist:
        h_yyy.Fill(row['Ave Rating'], row['Per of Users'] )    
            
    HList1.Add(h_yyy)



    ##print "FULL AVE RATING"
    ##newlist = sorted(foundusermoviescoresList, key=itemgetter('Ave Rating'))
    ##for row in newlist:
    ##    print (row['item_id'], row['Total Rating'], row['Users'], row['Ave Rating'], row['Per of Users'])


  
    #AAAR = sorted(foundusermoviescoresList, key=itemgetter('Ave Rating'))[-2]
    #AATR = sorted(foundusermoviescoresList, key=itemgetter('Total Rating'))[-2]

    
    ##for row in newlist:
    ##    print (row['item_id'], row['Total Rating'], row['Users'], row['Ave Rating'], row['Per of Users'])







    onlyhighest = 10
    basic_histo_types = ['Total Rating','Users','Ave Rating','Per of Users','Norm Ave Rating']
    colors = [4,2,3,6,7]
    fills = [3001,3007,3006,3004,3005]

    for uuu in range(0, len(basic_histo_types)):
        sortedby = str(basic_histo_types[uuu])
    #    print sortedby

        newlist = sorted(foundusermoviescoresList, key=itemgetter(sortedby))[-onlyhighest:]

    ##    for row in newlist:
    ##        print (row['item_id'], row['Total Rating'], row['Users'], row['Ave Rating'], row['Per of Users'])
    ####        print (row['item_id'], AAItemIDtoTitle(row['item_id']), AAItemIDtoGenres(row['item_id']), row['Total Rating'], row['Users'], row['Ave Rating'], row['Per of Users'], row['Norm Ave Rating'])

        nbins = len(newlist)
        xmin = 0
        xmax = len(newlist)
        #MovieName = AAItemIDtoTitle(int(searchpatternDict['item_id']))
        #SearchStragedy = ' '
        #for key in searchpatternDict['rating'].keys():
        #    SearchStragedy = SearchStragedy + key + " " + searchpatternDict['rating'][key]
        Captions = MovieName + ", Match" + SearchStragedy + " Stars, Top" + str(onlyhighest) + "; ; " + sortedby
        Names = MovieName + ' '+ sortedby + ' Top' + str(onlyhighest)
        #print "MAKING HISTO"
        h_xxx = TH1D(Names, Captions, nbins, xmin, xmax)
        #print "HISTO MADE"

        iii=0
        for row in newlist:
            #print (row['item_id'], row['Total Rating'], row['Users'], row['Ave Rating'], row['Per of Users'])
            #h_xxx.Fill(int(row['item_id']), row[sortedby] )
            if uuu < 2:
                for jjj in range(0,row[sortedby]):
                    h_xxx.Fill(iii)
            else:
                h_xxx.Fill(iii, row[sortedby] )
                
            h_xxx.GetXaxis().SetBinLabel(iii+1,AAItemIDtoTitle(row['item_id']))
            iii=iii+1

        h_xxx.SetFillStyle(fills[uuu])
        h_xxx.SetFillColor(colors[uuu])
        #add histograms to histo arrays
        HList1.Add(h_xxx)





    ROOTDir1 = MovieName

    #declare + initilze directory
    dir_obj = file_obj.mkdir(ROOTDir1)

    ##this goes to the directory we just created, tree will be put in there
    ##if you want tree to just be put in the master directory (root file), just dont include this command
    file_obj.cd(ROOTDir1)
    HList1.Write()
    

#write to the output root file
#file_obj.Write()



##
##
##OutPutROOTFileName = "DI2_Finalist.root"
##ROOTDir1 = MovieName
##
###make the output root file
##file_obj = TFile(OutPutROOTFileName, "RECREATE")
##
###declare + initilze directory
##dir_obj = file_obj.mkdir(ROOTDir1)
##
####this goes to the directory we just created, tree will be put in there
####if you want tree to just be put in the master directory (root file), just dont include this command
##file_obj.cd(ROOTDir1)
##HList1.Write()
##
##
##
###write to the output root file
##file_obj.Write()


print "END"
