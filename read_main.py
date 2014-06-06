# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\liu\.spyder2\.temp.py
"""

import csv
from fastcluster import *
from subroutines import *
import numpy as np


def readCsv(fileName):
    catSku = {}
    #catsku is the category sku dictionary. For each category, there are multiple skus. This is a dictionary of key->list
    userSku = {}
    #for each user, he/she has different sku purchased. This is a dictionary of key -> list
    userCat = {}
    #for each user, he/she must have bought items from different catagories. 
    #his is a dictionary of key->dictionary

    i = -1
    with open(fileName, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        i=-1
        for row in spamreader:
            if i!=-1:        
                userTemp= row[0]
                skuTemp = row[1]
                catTemp = row[2]
                if catSku.get(catTemp)==None:
                    catSku[catTemp] = []
                if userSku.get(userTemp) == None:
                    userSku[userTemp] = []
                if userCat.get(userTemp) == None:
                    userCat[userTemp] = {}
                if userCat[userTemp].get(catTemp)==None:
                    userCat[userTemp][catTemp]=0
                catSku[catTemp].append(skuTemp)
                catSku[catTemp] = list(set(catSku[catTemp]))
                
                userSku[userTemp].append(skuTemp)
                userSku[userTemp] = list(set(userSku[userTemp]))
                
                userCat[userTemp][catTemp]+=1
            i+=1
    return [catSku,userSku,userCat]
    
def saveToLocal(catSku,userSku,userCat):
    saveFile('./data/catSku.dat',catSku)
    saveFile('./data/usersku.dat',userSku)
    saveFile('./data/userCat.dat',userCat)
    
def main():
     [catSku,userSku,userCat] = readCsv('./smalldataset/train.csv')
     saveToLocal(catSku,userSku,userCat)
     
if __name__=='__main__':
    main()