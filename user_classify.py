# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 14:11:55 2014

@author: liu
"""

from subroutines import *
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

#now all we left to do is to classfy the users, and also to classify the items. 
#The items are all stored in catSku. I assume that the item type would be good enough to classfy the items? I dont know. 
#We will see. 

