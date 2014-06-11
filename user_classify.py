# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 14:11:55 2014

@author: liu
"""

from subroutines import *
from fastcluster import linkage
from scipy.cluster.hierarchy import dendrogram
catSku = {}
#catsku is the category sku dictionary. For each category, there are multiple skus. This is a dictionary of key->list
userSku = {}
#for each user, he/she has different sku purchased. This is a dictionary of key -> list
userCat = {}
#for each user, he/she must have bought items from different catagories. 
#his is a dictionary of key->dictionary
catSku = readFile('./data/catSku.dat')
userSku = readFile('./data/userSku.dat')
userCat = readFile('./data/userCat.dat')
resdict = {}
#now all we left to do is to classfy the users, and also to classify the items. 
#The items are all stored in catSku. I assume that the item type would be good enouguh to classfy the items? I dont know. 
#We will see. 
def convertNumber(s):
    return [[float(ord(c))] for c in s]
def getWeight():
    global resdict
    resdict = json.loads(open('./smalldataset/boolean_prefict.json','r').read())

def createLinkageArray(catSku, userSku, userCat):
    for user in userSku.keys():
        #if the user has not bought more than 3 items, they are new and thus dont need to be classfied. 
        #if len(userSku[user])>=3:
            #we use the most frequent buy and least frequent buy to identify user groups. 
           
        '''
        We want to create an array of corrolation for cluster function to calculate
        which users are more closely related to each other, and which is not. 
        
        We will need to get the 3 most bought items to identify and compare the users. 
        '''
    
    return 0