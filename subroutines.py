# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 13:50:02 2014

@author: liu
"""
import pickle
import os
import re
def saveFile(fileName,data):
    with open(fileName, 'wb') as f:
        pickle.dump(data,f)
    return 0
    
def readFile(fileName):
    if os.path.isfile(fileName):
        with open(fileName,'rb') as f:
            data = pickle.load(f)
        return data
    else:
        raise Exception('the file'+str(fileName)+'does not exist')
def getString(s):
    match = re.match(r"([a-zA-Z]+)([\d]+)", s, re.I)
    if match:
        items = match.groups()
        print items
        return items[0]
    else:
        raise Exception('no matching string found')
    # items is ("foo", "21")