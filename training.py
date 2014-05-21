#!/bin.python

from collections import defaultdict
import csv,json
import nltk
import numpy as np

productdict=json.load(open('./smalldataset/small_product_data.json','r'))
predictdict={}

def training(productdict,predictdict):
    with open("./smalldataset/train.csv") as infile:
	    reader = csv.reader(infile, delimiter=",")
	    reader.next() # burn the header

	    weightname=[]
	    weightdesc=[]
	    weightnew=[]
	    weightactive=[]
	    weightonsale=[]
	    weigthpreowned=[]
	    weightfreeShipping=[]
	    weightinStoreAvailability=[]
	    weightonlineAvailability=[]
	    weightinStorePickup=[]
	    weightfriendsAndFamilyPickup=[]
	    weighthomeDelivery=[]
	    weightadvertisedPriceRestriction=[]
	    weightdigital=[]
	    weightspecialOrder=[]
	    weighthasimg=[]
	    weighthaslargefrontimg=[]
	    weighthasmediumImage=[]
	    weighthasthumbnailImage=[]
	    weighthaslargeImage=[]

	    counter=0
	    for (user, sku, category, query, click_time, query_time) in reader:
	    	counter=counter+1
	    	if sku not in productdict:
	    		continue

	    	query=query.replace('_',' ')
	    	querytoken=nltk.word_tokenize(query.lower().strip())

	    	productelem=productdict[sku]
	    	
    		name = productelem['name']
    		desc = productelem['desc']

    		nametoken = nltk.word_tokenize(name.lower().strip())
    		desctoken = nltk.word_tokenize(desc.lower().strip())

    		weightname.append( len(list(set(querytoken) & set(nametoken)))*1.0/len(querytoken))
    		weightdesc.append( len(list(set(querytoken) & set(desctoken)))*1.0/len(querytoken))


    		new = productelem['new']
    		if new==True:
    			weightnew.append(1)
    		elif new==False:
    			weightnew.append(0)

    		active = productelem['active']
    		if active==True:
    			weightactive.append(1)
    		elif active==False:
    			weightactive.append(0)

    		onsale = productelem['onsale']
    		if onsale==True:
    			weightonsale.append(1)
    		elif onsale==False:
    			weightonsale.append(0)

    		preowned = productelem['preowned']
    		if preowned==True:
    			weigthpreowned.append(1)
    		elif preowned==False:
    			weigthpreowned.append(0)

    		freeShipping = productelem['freeShipping']
    		if freeShipping==True:
    			weightfreeShipping.append(1)
    		elif freeShipping==False:
    			weightfreeShipping.append(0)

    		inStoreAvailability = productelem['inStoreAvailability']
    		if inStoreAvailability==True:
 				weightinStoreAvailability.append(1)
    		elif inStoreAvailability==False:
    			weightinStoreAvailability.append(0)

    		onlineAvailability=productelem['onlineAvailability']
    		if onlineAvailability==True:
				weightonlineAvailability.append(1)
    		elif onlineAvailability==False:
    			weightonlineAvailability.append(0)

    		inStorePickup=productelem['inStorePickup']
    		if inStorePickup==True:
 				weightinStorePickup.append(1)
    		elif inStorePickup==False:
    			weightinStorePickup.append(0)

    		friendsAndFamilyPickup=productelem['friendsAndFamilyPickup']
    		if friendsAndFamilyPickup==True:
 				weightfriendsAndFamilyPickup.append(1)
    		elif friendsAndFamilyPickup==False:
    			weightfriendsAndFamilyPickup.append(0)

    		homeDelivery=productelem['homeDelivery']
    		if homeDelivery==True:
 				weighthomeDelivery.append(1)
    		elif homeDelivery==False:
    			weighthomeDelivery.append(0)

    		advertisedPriceRestriction=productelem['advertisedPriceRestriction']
    		if advertisedPriceRestriction==True:
 				weightadvertisedPriceRestriction.append(1)
    		elif advertisedPriceRestriction==False:
    			weightadvertisedPriceRestriction.append(0)

    		digital=productelem['digital']
    		if digital==True:
 				weightdigital.append(1)
    		elif digital==False:
    			weightdigital.append(0)

    		specialOrder=productelem['specialOrder']
    		if specialOrder==True:
 				weightspecialOrder.append(1)
    		elif specialOrder==False:
    			weightspecialOrder.append(0)

    		hasimg=productelem['hasimg']
    		if hasimg==True:
 				weighthasimg.append(1)
    		elif hasimg==False:
    			weighthasimg.append(0)

    		haslargefrontimg=productelem['haslargefrontimg']
    		if haslargefrontimg==True:
 				weighthaslargefrontimg.append(1)
    		elif haslargefrontimg==False:
    			weighthaslargefrontimg.append(0)    

    		hasmediumImage=productelem['hasmediumImage']
    		if hasmediumImage==True:
 				weighthasmediumImage.append(1)
    		elif hasmediumImage==False:
    			weighthasmediumImage.append(0) 

    		hasthumbnailImage=productelem['hasthumbnailImage']
    		if hasthumbnailImage==True:
 				weighthasthumbnailImage.append(1)

    		elif hasthumbnailImage==False:
    			weighthasthumbnailImage.append(0) 

    		haslargeImage=productelem['haslargeImage']
    		if haslargeImage==True:
 				weighthaslargeImage.append(1)
    		elif haslargeImage==False:
    			weighthaslargeImage.append(0) 


    		print '%s'%counter
    	
		resdict={
			'name' : np.mean(weightname),
			'desc' : np.mean(weightdesc),
			'new'  : np.mean(weightnew),
			'active':np.mean(weightactive),
			'onsale':np.mean(weightonsale),
			'preowned':np.mean(weigthpreowned),
			'freeShipping':np.mean(weightfreeShipping),
			'inStoreAvailability':np.mean(weightinStoreAvailability),
			'onlineAvailability':np.mean(weightonlineAvailability),
			'inStorePickup':np.mean(weightinStorePickup),
			'friendsAndFamilyPickup':np.mean(weightfriendsAndFamilyPickup),
			'homeDelivery':np.mean(weighthomeDelivery),
			'advertisedPriceRestriction':np.mean(weightadvertisedPriceRestriction),
			'digital':np.mean(weightdigital),
			'specialOrder':np.mean(weightspecialOrder),
			'hasimg':np.mean(weighthasimg),
			'haslargefrontimg':np.mean(weighthaslargefrontimg),
			'hasmediumImage':np.mean(weighthasmediumImage),
			'hasthumbnailImage':np.mean(weighthasthumbnailImage),
			'haslargeImage':np.mean(weighthaslargeImage),
		}

		open('./smalldataset/boolean_prefict.json','w').write(json.dumps(resdict))

if __name__ == "__main__":
	training(productdict,predictdict)