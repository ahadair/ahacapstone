#import needed functions
import re, string, os
import csv
import math
from operator import itemgetter

#print "0"
##import ROOT functions
#from ROOT import gROOT, TCanvas, TF1
#print "1"
#from ROOT import TFile, TDirectory, TTree
#print "2"
#from ROOT import AddressOf
#print "3"
#from ROOT import TH1D, TH2D, TObjArray, TProfile
#print "4"



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



#print "START"




#Genre Binary Code to Dec Code Transform
def AAcombined_genre_to_list(input_number):
    binarystring = bin(input_number)[2:].zfill(19)
    GenreAAList = []
    for i in range(0, 19):
        if binarystring[i] == '1':
            #print GenreDict[str(i)]
            GenreAAList.append(GenreDict[str(i)])
    return GenreAAList







def AAMainCode(The_input_movie, The_input_score):
    #print "Setting Inputs"
    #DataSetPath = 'DataSets\\FromWebDirect\\100k\\ml-100k\\'
    DataSetPath = 'DataSets/FromWebDirect/100k/ml-100k/'
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




    #Get Item Dict
    #print "Getting Item Dict"
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

    #Movie Moive Title to ID
    def AATitletoItemID(input_string):
        for input_number in range(1, len(ItemDict)):
            #print input_number
            if ItemDict[str(input_number)]['movie_title'] == input_string:
                return input_number
        return None

    #Movie ID to Genre
    def AAItemIDtoGenres(input_number):
        return AAcombined_genre_to_list(int( ItemDict[str(input_number)]['combined_genre']))






    #Get Info Dict
    #print "Getting Info Dict"
    InfoDict = {}
    with open(InfoFullFile) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            InfoDict[row[0].split()[1]] = row[0].split()[0]
            #InfoDict[row[0].split()[1]] = int(row[0].split()[0])
    #print InfoDict


    #Get Genre Dict
    #print "Getting Genre Dict"
    GenreDict = {}
    with open(GenreFullFile) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 1:
                if len(row[0].split("|"))==2:
                    GenreDict[row[0].split("|")[1]] = row[0].split("|")[0]
    #print GenreDict




    #1 == Toy Story


    #The_input_movie = "Toy Story (1995)"
    #The_input_score = "3"


    movienumber = str(AATitletoItemID(The_input_movie))
    ListOfsearchpatternDict = [{ 'item_id': movienumber, 'rating': {'>=':The_input_score}}]
    #ListOfsearchpatternDict = [{ 'item_id': '1', 'rating': {'>=':'3'}}]

    # ['Total Rating','Users','Ave Rating','Per of Users','Norm Ave Rating']







    aaaindex = 0
    for searchpatternDict in ListOfsearchpatternDict:
        #print "Running Over = ", aaaindex#, "," , searchpatternDict
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



        onlyhighest = 10
        basic_histo_types = ['Total Rating','Users','Ave Rating','Per of Users','Norm Ave Rating']
        colors = [4,2,3,6,7]
        fills = [3001,3007,3006,3004,3005]

        for uuu in range(len(basic_histo_types)-1, len(basic_histo_types)):
            sortedby = str(basic_histo_types[uuu])

            newlist = sorted(foundusermoviescoresList, key=itemgetter(sortedby))[-onlyhighest:]

            nbins = len(newlist)
            xmin = 0
            xmax = len(newlist)
            
            Captions = "Profile = " + MovieName + ", Match" + SearchStragedy + " Stars" + ", " + sortedby
            Names = MovieName + ' '+ sortedby + ' Top' + str(onlyhighest)

            print Captions
            OKAYlistRank = []
            OKAYlistScore = []
            OKAYlistMovie = []
            iii=0
            for row in newlist:
                OKAYlistRank.append("%d" % (iii+1))
                OKAYlistScore.append("%s" % (row[sortedby]))
                OKAYlistMovie.append("%s" % (AAItemIDtoTitle(row['item_id'])))
                
        
                iii=iii+1
                
            #print OKAYlist

            #print OKAYlistRank[-1], OKAYlistScore[-1], OKAYlistMovie[-1]
            #print OKAYlistRank[-2], OKAYlistScore[-2], OKAYlistMovie[-2]

    return OKAYlistRank, OKAYlistScore, OKAYlistMovie



#WhatRank = []
#WhatScore = []
#WhatMovie = []
#WhatRank, WhatScore, WhatMovie = AAMainCode("Toy Story (1995)", "3")
#print WhatRank[-1], WhatScore[-1], WhatMovie[-1]
#print WhatRank[-2], WhatScore[-2], WhatMovie[-2]




