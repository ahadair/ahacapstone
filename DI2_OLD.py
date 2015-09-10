#import needed functions
import re, string, os
import csv
import math



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



#Get Info
print "Getting Info Dict"
InfoDict = {}
with open(InfoFullFile) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        InfoDict[row[0].split()[1]] = row[0].split()[0]
        #InfoDict[row[0].split()[1]] = int(row[0].split()[0])
print InfoDict







#searchpatternDict = { 'item_id': {'=': '242'}, 'rating': {'>=':'3'}}                   
searchpatternDict = { 'item_id': '242', 'rating': {'>=':'3'}}


print "GET_USERS_WITH_SIMILAR_TASTES"
founduserlist = []
with open(DataFullFile) as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t', fieldnames = ['user_id', 'item_id', 'rating', 'timestamp'])
    for row in reader:
        if row['user_id'] not in founduserlist:
            if AAcompareDict(searchpatternDict, row) == 1:
                founduserlist.append(row['user_id'])
                
founduserlist = list(set(founduserlist))
#print founduserlist



print "GETTTING_SIMILAR_TASTES"
foundusermoviescoresDict = {}
foundusermoviescoresList = []
with open(DataFullFile) as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t', fieldnames = ['user_id', 'item_id', 'rating', 'timestamp'])
    for row in reader:

        if row['user_id'] in founduserlist:

            if row['item_id'] not in foundusermoviescoresDict:
                foundusermoviescoresDict[row['item_id']] = {'item_id': int(row['item_id']), 'totalrating' : int(row['rating']), 'users': int('1')}                
            else:
                foundusermoviescoresDict[row['item_id']]['totalrating'] = foundusermoviescoresDict[row['item_id']]['totalrating'] + int(row['rating'])
                foundusermoviescoresDict[row['item_id']]['users'] = foundusermoviescoresDict[row['item_id']]['users'] + 1

                                                                                                                
##############UNFINISHED IDEA                
##            xxx = [item for item in foundusermoviescores if int(item['item_id']) == int(row['item_id'])]
##            if not xxx:
##                print xxx, "EMPTY"
##                foundusermoviescores.append({'item_id': int(row['item_id']), 'totalrating' : int(row['rating']), 'users':int('1')})
##            else:
##                print xxx, "NOT EMPTY"


###############ALTERNATIVE METHOD, WORKS, SLOW      
##            Moviewasfound = False            
##            
##            #Search to see if movie already exists
##            for frow in foundusermoviescoresList:
##                #movie found
##                if( int(frow['item_id']) == int(row['item_id'])):
##                    frow['totalrating'] = int(frow['totalrating']) + int(row['rating'])
##                    frow['users'] = int(frow['users']) + 1  
##                    #found movies listing
##                    Moviewasfound = True
##                    break
##
##            #movie not found    
##            if(not Moviewasfound):
##                foundusermoviescoresList.append({'item_id': int(row['item_id']), 'totalrating' : int(row['rating']), 'users':int('1')})
##
##


##Dict--->List
for key in foundusermoviescoresDict.keys():
    foundusermoviescoresList.append(foundusermoviescoresDict[key])



                
for row in foundusermoviescoresList:
  
    row['percent'] = math.ceil(float(row['users'])/float(len(founduserlist))*100)/100  
    row['rating'] = math.ceil(float(row['totalrating'])/float(row['users']) *10)/10



from operator import itemgetter

newlist = sorted(foundusermoviescoresList, key=itemgetter('totalrating'))


for row in newlist:
    print (row['item_id'], row['totalrating'], row['users'], row['rating'], row['percent'])





print "END"
