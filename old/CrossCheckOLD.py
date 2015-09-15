
#import needed functions
import re, string, os
import csv
#import enum
import math



def spcompare(SF, S, SP):
    #print "USING THE FUCNTION"


    #print SF,S,SP

    #equal case
    if(SP == 0):
        if(SF == S):
#            print "GOOD1"
            return True
        else:
            return False

    #great than or equal case
    if(SP == 2):
        if(SF <= S):
#            print "GOOD2"
            return True
        else:
#            print "BAD2"
            return False
    
    #print "BAD3"
    return False





print "START"


#searchfor = [{'user_id': '-1', 'item_id': '200', 'rating': '3', 'timeset': '-1'},
#             {'user_id': '-1', 'item_id': '400', 'rating': '5', 'timeset': '-1'}]

#searchfor = [{'item_id': '242', 'rating': '3'},
#             {'item_id': '302', 'rating': '3'}]

searchfor = [{'item_id': '242', 'rating': '3'}]

searchpattern = {'item_id': '0', 'rating': '2'}                     


founduserlist = []

foundusermoviescores = []
#foundusermoviescores = [{'item_id': '-1', 'totalrating' : '0', 'users':'0'}]


#print "%s" % spcompare(3, 3, 0)
#print "%s" % spcompare(2, 3, 0)
#print "%s" % spcompare(3, 1, 2)
#print "%s" % spcompare(2, 3, 2)

#ExactMatch         = 0, SF =  S
#LessThan           = 1, SF <  S
#LessThanOrEqual    = 2, SF <= S
#GreaterThan        = 3, SF >  S
#GreaterThanOrEqual = 4, SF >= S



print "SEARCHFOR"

#for row in searchfor:
#    for key in row:
#        print "key: %s" % key
#    k = list[row.keys()]
#    print k
#    print (row['user_id'], row['item_id'], row['rating'], row['timeset'])   




print "READER"

sss = ""
iii = 0

with open('u.data') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t', fieldnames = ['user_id', 'item_id', 'rating', 'timestamp'])
#    reader = csv.DictReader(csvfile, delimiter='\t', fieldnames = ("user_id", "item_id", "rating", "timestamp"))
    for row in reader:
#        print (row['user_id'], row['item_id'], row['rating'], row['timestamp'])    
#       print row['user_id']



        for srow in searchfor:
            somethinglikesrowfound = True;

            rowset = set(row)
            srowset = set(srow)

            
            for name in rowset.intersection(srowset):
                #print name, srow[name], row[name], searchpattern[name]
                #print srow[name], row[name], searchpattern[name]
                #print "%s" % spcompare(int(srow[name]), int(row[name]), int(searchpattern[name]))
                somethinglikesrowfound = somethinglikesrowfound and spcompare(int(srow[name]), int(row[name]), int(searchpattern[name]))
                #if( spcompare(srow[name], row[name], searchpattern[name])):
                #    print name, srow[name], row[name], searchpattern[name]
            
            #print (row['user_id'], row['item_id'], row['rating'], row['timeset'])   


            if(somethinglikesrowfound):
#                print (row['user_id'], row['item_id'], row['rating'], row['timestamp'])
                founduserlist.append(row['user_id'])
#                sss = "("
#                for skey in srow:
#                    sss = sss + "%s:%s," % (skey, srow[skey])
#                print sss[:-1] + ")"



        #print sss
        iii = iii +1        
#        if iii == 5:
#            break


founduserlist = list(set(founduserlist))
print "TEST"


with open('u.data') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t', fieldnames = ['user_id', 'item_id', 'rating', 'timestamp'])

    for row in reader:

#        print (row['user_id'], row['item_id'], row['rating'], row['timestamp'])    
#        print row['user_id']

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
    #row.append({'rating': 1})


    row['percent'] = math.ceil(float(row['users'])/float(len(founduserlist))*100)/100

    
    row['rating'] = math.ceil(float(row['totalrating'])/float(row['users']) *10)/10
    #print (row['item_id'], row['totalrating'], row['users'])
    #print row
#    print (row['item_id'], row['totalrating'], row['users'], row['rating'])


#for index in founduserlist:
#    print founduserlist[index]
    

#sorted(foundusermoviescores, key = 0)

from operator import itemgetter

newlist = sorted(foundusermoviescores, key=itemgetter('totalrating'))


for row in newlist:
    print (row['item_id'], row['totalrating'], row['users'], row['rating'], row['percent'])



##Input search number
##AASearchNumberAA = 21
#AASearchNumberAA = options.SearchNumber
#print "SearchNumber = %s" % (AASearchNumberAA)

print "END"
