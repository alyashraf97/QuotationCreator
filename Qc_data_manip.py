import openpyxl
import math
import json



class QuoteInfo():
    def __init__(self, qouteInfo = None):
        if(qouteInfo != None):
            self.customer = qouteInfo["customer"]
            self.manufacturers = qouteInfo["manufacturers"]
            self.request = qouteInfo["request"]
            self.paymentTerm = qouteInfo["paymentTerm"]
            self.refNo = qouteInfo["refNo"]
            self.quoteDate = qouteInfo["quoteDate"]
            self.quoteCurrency = qouteInfo["quoteCurrency"]
            self.vatStatus = qouteInfo["vatStatus"]
            self.targetProfit = qouteInfo["targetProfit"]
            self.offerValidity = qouteInfo["offerValidity"]
            self.deliveryType = qouteInfo["deliveryType"]


class Vendor():
    def __init__(self,vendorData = None):
        if(vendorData != None):
            self.vendorName = vendorData["vendorName"]
            self.vendorComission = float(vendorData["vendorComission"])
            self.vendorPackingCost = float(vendorData["vendorPackingCost"])
            self.vendorShippingCost = float(vendorData["vendorShippingCost"])
            self.vendorCustoms = float(vendorData["vendorCustoms"])
            self.vendorCurrency = vendorData["vendorCurrency"]
            self.vendorLeadTime = int(vendorData["vendorLeadTime"])

class Item():
    def __init__(self,itemInfo = None):
        if(itemInfo != None):
            self.itemName = itemInfo["itemName"]
            self.itemType = itemInfo["itemType"]
            self.itemPartNumber = itemInfo["itemPartNumber"]
            self.itemQuantity = int(itemInfo["itemQuantity"])
            self.itemDescription = itemInfo["itemDescription"]
            self.vendorCurrency = itemInfo["vendorCurrency"]
            self.vendorLeadTime = itemInfo["vendorLeadTime"]

class Quote():
    def __init__(self,allQuoteInformation):
        if(allQuoteInformation != None):
            self.quoteInformation = allQuoteInformation["quoteInformation"]
            self.allVendorData = allQuoteInformation["allVendorData"]
            self.allItemData = [allQuoteInformation["allVendorData"][key] for key in dict.fromkeys(allQuoteInformation["allVendorData"])]
            
        
















































### INTO THE ANUS OF TIME
'''
Quotation Data JSON

quotation_data =
    "quotationDetails":
        {
            "customer":customer,
            "manufacturers":manufacturers,
            "request":request,
            "paymentTerm":paymentTerm,
            "refNo":refNo,
            "quoteDate":quoteDate,
            "quoteCurrency":quoteCurrency,
            "vatStatus":vatStatus,
            "targetProfit":targetProfit,
            "offerValidity":offerValidity,
            "deliveryType":deliveryType
        },
    "dataByVendors":[
        {
            "vendorName":"vendorA",
            'vendorComission': 0.1,
            'vendorPackingCost':300,
            'vendorShippingCost':250,
            'vendorCustoms':0.05,
            'vendorCurrency':USD,
            'vendorLeadTime':10,
            'vendorItemData'={
                'itemNames'=[itemNameA, itemNameB, itemNameC]
                'itemUnitPrices'=[200,300,500],
                'itemQuantities'=[3,10,5],
                'itemWeights'=[0.2, 0.3, 0.5],
                'itemUnitPriceCom'=[180, 270, 450]
                'vendorTotalPrice'=8000
            }
        },
        {
            "vendorName":"vendorB",
            'vendorComission': 0.05,
            'vendorPackingCost':300,
            'vendorShippingCost':250,
            'vendorCustoms':0.03,
            'vendorCurrency':USD,
            'vendorLeadTime':10,
            'vendorItemData'={
                'itemNames'=[itemNameA, itemNameB, itemNameC]
                'itemUnitPrices'=[100,600, 80],
                'itemQuantities'=[10, 2, 25],
                'itemWeights'=[0.2, 0.3, 0.5],
                'itemUnitPriceCom'=[180, 270, 450]
                'vendorTotalPrice'=8000
            }
        }
    ]
    




class QuotationMath():
    quotationData={}

    def __init__(self,listing_of_all_vendors):
        self.listing_of_all_vendors=listing_of_all_vendors
        self.final_prices=self.calculate_final_price

        
    def seperate_vendor(self,vendor_name):
        vendor_list_of_unit_prices=self.listing_of_all_vendors[f'{vendor_name}']

        return vendor_list_of_unit_prices


    def get_item_weights(self,list_of_all_item_unit_prices):
        #Returns item weights (vendor by vendor basis)
        #Takes a list of item prices (before markup) and returns a list of weights
        item_weights=[]
        total_sum=sum(list_of_all_item_unit_prices)
        for i in range(len(list_of_all_item_unit_prices)):
            item_weights[i]=list_of_all_item_unit_prices[i]/total_sum
        return item_weights

    def final_vendor_prices(self,list_of_vendor_unit_prices,list_of_vendor_qty, 
                            vendor_packing, vendor_shipping, vendor_customs, 
                            vendor_comission):
        vendor_price_listing={}
        vendor_sum=int()
        list_of_item_total_prices=[]

        #generating a sum of item total prices & a list of item total prices
        for i in range(len(list_of_vendor_unit_prices)):
            vendor_sum+=list_of_vendor_unit_prices[i]*list_of_vendor_qty[i]
            list_of_item_total_prices[i]=(list_of_vendor_unit_prices[i]*(1-vendor_comission))*list_of_vendor_qty[i]

        vendor_final_total=vendor_sum+vendor_customs+vendor_packing+vendor_shipping
        item_weights=self.get_item_weights(list_of_vendor_unit_prices)
        vendor_final_price_list=[vendor_final_total*item_weights[i] for i in range(len(list_of_vendor_unit_prices))]

        vendor_price_listing={
            "totalPrice": vendor_final_total,
            "list_of_vendor_total_prices":vendor_final_price_list
        }    
        
        return vendor_price_listing
        

    def calculate_final_price(self, list_of_vendor_total_prices, target_profit,
                            sales_tax, vat_state):
        cumulative_sum=sum(list_of_vendor_total_prices)
        #for i in range(len(list_of_item_prices)):
            #cumulative_sum+=list_of_item_prices[i]*list_of_item_qty[i]
        
        #final_price=((cumulative_sum/(1-target_profit))*(1+sales_tax))
        if vat_state==True:
            return ((cumulative_sum/(1-target_profit))*(1+sales_tax))
        else:
            return ((cumulative_sum/(1-target_profit))*(1+sales_tax))*1.14



















#_______________________________________________________________________________
#----------------Class for the vendors------------------------------------------
#_______________________________________________________________________________

class Vendor():
    def __init__(self, vendor_currency, shipping_cost, packaging_cost, clearing_cost,
                 vendor_comission, vendor_leadtime):
        pass
    
class VendorItem(Vendor):
    def __init__(self, vendor_currency, shipping_cost, packaging_cost, 
                 clearing_cost, vendor_comission, vendor_leadtime, item_cost, 
                 item_type, item_description, item_quantity, item_part_number):
        super().__init__(vendor_currency, shipping_cost, packaging_cost, 
                         clearing_cost, vendor_comission, vendor_leadtime)
                         '''