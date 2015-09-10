
#import needed functions
import re, string, os
import csv
#import enum
import math


def spcompare(SF, S, SP):
    #equal case
    if(SP == 0):
        if(SF == S):
            return True
        else:
            return False
    #great than or equal case
    if(SP == 2):
        if(SF <= S):
            return True
        else:
            return False
    return False


#ExactMatch         = 0, SF =  S
#LessThan           = 1, SF <  S
#LessThanOrEqual    = 2, SF <= S
#GreaterThan        = 3, SF >  S
#GreaterThanOrEqual = 4, SF >= S


print "START"



searchfor = [{'item_id': '242', 'rating': '3'}]

searchpattern = {'item_id': '0', 'rating': '2'}                     
founduserlist = []
foundusermoviescores = []


print "GET_USERS_WITH_SIMILAR_TASTES"
sss = ""
iii = 0

with open('u.data') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t', fieldnames = ['user_id', 'item_id', 'rating', 'timestamp'])
    for row in reader:
        for srow in searchfor:
            somethinglikesrowfound = True;

            rowset = set(row)
            srowset = set(srow)

            
            for name in rowset.intersection(srowset):
                somethinglikesrowfound = somethinglikesrowfound and spcompare(int(srow[name]), int(row[name]), int(searchpattern[name]))
                
            if(somethinglikesrowfound):
                #print row
                founduserlist.append(row['user_id'])

        iii = iii +1        


founduserlist = list(set(founduserlist))

#print "len =", len(founduserlist)
#print founduserlist

print "GETTTING_SIMILAR_TASTES"
with open('u.data') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t', fieldnames = ['user_id', 'item_id', 'rating', 'timestamp'])

    for row in reader:

        for i in range(len(founduserlist)):

            if(int(founduserlist[i]) == int(row['user_id'])):

                Moviewasfound = False
                for frow in foundusermoviescores:
                    if( int(frow['item_id']) == int(row['item_id'])):
                        frow['totalrating'] = int(frow['totalrating']) + int(row['rating'])
                        frow['users'] = int(frow['users']) + 1  
                        #found movies listing
                        Moviewasfound = True
                        break

                    #MOVIE WAS NOT FOUND
                    
                if(not Moviewasfound):
                    foundusermoviescores.append({'item_id': int(row['item_id']), 'totalrating' : int(row['rating']), 'users':int('1')})




for row in foundusermoviescores:
  
    row['percent'] = math.ceil(float(row['users'])/float(len(founduserlist))*100)/100  
    row['rating'] = math.ceil(float(row['totalrating'])/float(row['users']) *10)/10



from operator import itemgetter

newlist = sorted(foundusermoviescores, key=itemgetter('totalrating'))


for row in newlist:
    print (row['item_id'], row['totalrating'], row['users'], row['rating'], row['percent'])





print "END"
