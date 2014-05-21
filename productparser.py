#!/bin/python

import xml.etree.ElementTree as ET
import json
tree = ET.parse('./smalldataset/small_product_data.xml')

def str2bool(str):
	if str=='true':
		return True 
	return False

root = tree.getroot()
resdict={}
for product in root.findall('product'):
	sku = product.find('sku').text.strip()

#string type feature
	name = product.find('name').text.strip()
	longDescription = product.find('longDescription').text.strip()

	orderable = ""
	if  product.find('orderable') != None:
		orderable = product.find('orderable').text.strip().lower()



	format=""
	if product.find('format').text != None:
		format = product.find('format').text.strip().lower()

	categorylst=[]
	for elem in product.find('categoryPath'):
		categorylst.append( elem.find('id').text.strip())


	relateditem=[]
	for elem in product.find('frequentlyPurchasedWith'):
		if elem.text != None:
			if len(elem.text.strip())>0:
				relateditem.append( elem.text.strip())


#bool type feature
	new = str2bool(product.find('new').text.strip().lower())
	active = str2bool(product.find('active').text.strip().lower())
	onsale = str2bool(product.find('onSale').text.strip().lower())
	preowned = str2bool(product.find('preowned').text.strip().lower())
	freeShipping = str2bool(product.find('freeShipping').text.strip().lower())
	inStoreAvailability = str2bool(product.find('inStoreAvailability').text.strip().lower())
	onlineAvailability = str2bool(product.find('onlineAvailability').text.strip().lower())

	inStorePickup = False
	if product.find('inStorePickup') != None:
		inStorePickup = str2bool(product.find('inStorePickup').text.strip().lower())

	friendsAndFamilyPickup = False
	if product.find('friendsAndFamilyPickup') != None:
		friendsAndFamilyPickup = str2bool(product.find('friendsAndFamilyPickup').text.strip().lower())

	homeDelivery = False
	if product.find('homeDelivery') != None:
		homeDelivery = str2bool(product.find('homeDelivery').text.strip().lower())
	advertisedPriceRestriction = str2bool(product.find('advertisedPriceRestriction').text.strip().lower())
	digital = str2bool(product.find('digital').text.strip().lower())
	specialOrder = str2bool(product.find('specialOrder').text.strip().lower())

	hasimg=False
	if product.find('image') != None and product.find('image').text != None:
		hasimg=True

	haslargefrontimg=False
	if product.find('largeFrontImage') != None and product.find('largeFrontImage').text != None:
		haslargefrontimg=True

	hasmediumImage=False
	if product.find('mediumImage') != None and product.find('mediumImage').text != None:
		hasmediumImage=True

	hasthumbnailImage=False
	if product.find('thumbnailImage') != None and product.find('thumbnailImage').text != None:
		hasthumbnailImage=True

	haslargeImage=False
	if product.find('largeImage') != None and product.find('largeImage').text != None:
		haslargeImage=True






# rank type feature	
	if  product.find('salesRankShortTerm').text != None:
		shorttermrank = int(product.find('salesRankShortTerm').text.strip())
	elif  product.find('salesRankShortTerm').text == None:
		shorttermrank = -1

	if  product.find('salesRankMediumTerm').text != None:
		medtermrank = int(product.find('salesRankMediumTerm').text.strip())
	elif product.find('salesRankMediumTerm').text == None:
		medtermrank = -1

	if product.find('salesRankLongTerm').text != None:
		longtermrank = int(product.find('salesRankLongTerm').text.strip())
	elif product.find('salesRankLongTerm').text == None:
		longtermrank = -1

	if  product.find('bestSellingRank').text != None:
		besttermrank = int(product.find('bestSellingRank').text.strip())
	elif  product.find('bestSellingRank').text == None:
		besttermrank = -1

#num type feture
	if product.find('customerReviewCount').text != None:
		reviewcount = int(product.find('customerReviewCount').text.strip())
	elif product.find('customerReviewCount').text == None:
		reviewcount = 0

	if product.find('customerReviewAverage').text != None:
		reviewavg = float(product.find('customerReviewAverage').text.strip())
	elif product.find('customerReviewAverage').text == None:
		reviewavg = 0


	if product.find('regularPrice').text != None:
		regularPrice = float(product.find('regularPrice').text.strip())
	elif product.find('regularPrice').text == None:
		regularPrice = -1

	if product.find('salePrice').text != None:
		salePrice = float(product.find('salePrice').text.strip())
	elif product.find('salePrice').text == None:
		salePrice = -1

	if product.find('restrictedSalePrice').text != None:
		restrictedSalePrice = float(product.find('restrictedSalePrice').text.strip())
	elif product.find('restrictedSalePrice').text == None:
		restrictedSalePrice = -1

	if product.find('shippingCost').text != None:
		shippingCost = float(product.find('shippingCost').text.strip())
	elif product.find('shippingCost').text == None:
		shippingCost = 0

	numofoffers=len(product.find('offers'))

	productelem={
	'name' : name,
	'desc' : longDescription,
	'orderable' : orderable,
	'format': format,
	'categorylst': categorylst,
	'relateditem': relateditem,
	'new':new,
	'active':active,
	'onsale':onsale,
	'preowned':preowned,
	'freeShipping':freeShipping,
	'inStoreAvailability':inStoreAvailability,
	'onlineAvailability':onlineAvailability,
	'inStorePickup':inStorePickup,
	'friendsAndFamilyPickup':friendsAndFamilyPickup,
	'homeDelivery':homeDelivery,
	'advertisedPriceRestriction':advertisedPriceRestriction,
	'digital':digital,
	'specialOrder':specialOrder,
	'hasimg':hasimg,
	'haslargefrontimg':haslargefrontimg,
	'hasmediumImage':hasmediumImage,
	'hasthumbnailImage':hasthumbnailImage,
	'haslargeImage':haslargeImage,
	'shorttermrank':shorttermrank,
	'medtermrank':medtermrank,
	'longtermrank':longtermrank,
	'besttermrank':besttermrank,
	'reviewcount':reviewcount,
	'reviewavg':reviewavg,
	'regularPrice':regularPrice,
	'salePrice':salePrice,
	'restrictedSalePrice':restrictedSalePrice,
	'shippingCost':shippingCost,
	'numofoffers':numofoffers
	}
	if sku not in resdict:
		resdict[sku]=productelem

open('./smalldataset/small_product_data.json','w').write(json.dumps(resdict))




