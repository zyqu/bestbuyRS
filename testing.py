# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 20:09:26 2014

@author: liu
"""
import json
import nltk
import csv
resdict = json.loads(open('./smalldataset/boolean_prefict.json','r').read())
productdict=json.load(open('./smalldataset/small_product_data.json','r'))
with open("./smalldataset/test.csv") as infile:
    reader = csv.reader(infile, delimiter=",")
    reader.next()
    counter = 0
    result = {}
    for (user, category, query, click_time, query_time) in reader:
        counter = counter + 1
        query=query.replace('_',' ')
        querytoken=nltk.word_tokenize(query.lower().strip())
        for sku2 in productdict.keys():
            productelem=productdict[sku2]	
            rankNum = 0            
            for key in resdict.keys():
                if key=='name':
                    name = productelem['name']
                    nametoken = nltk.word_tokenize(name.lower().strip())
                    nameRank = len(list(set(querytoken) & set(nametoken)))*1.0/len(querytoken)
                    rankNum+=(nameRank - resdict[key])*0.6
                elif key=='desc':
                    desc = productelem['desc']
                    desctoken = nltk.word_tokenize(desc.lower().strip())
                    descRank = len(list(set(querytoken) & set(desctoken)))*1.0/len(querytoken)
                    rankNum+=(descRank - resdict[key])*0.3
                else:
                    rankNum += (productelem[key]-resdict[key])*0.02
            if result.get(query)==None:
                result[query]=[]
            result[query].append((rankNum,sku2))
        result[query] = sorted(result[query],reverse=True)[0:5]
open('./smalldataset/result.json','w').write(json.dumps(result))