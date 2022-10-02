import openpyxl
import math



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
            #self.allItemData = [allQuoteInformation["allVendorData"]["key"] for key in dict.fromkeys(allQuoteInformation["allVendorData"])]

            for i in range(len(allQuoteInformation['allVendorData'])):
                print(1)

                


















'''#def final_vendor_prices(list_of_vendor_unit_prices,list_of_vendor_qty, 
                        vendor_packing, vendor_shipping, vendor_customs, vendor_comission):
    cumulative_sum=0
    
    return
    

def get_item_weights(list_of_all_item_unit_prices, list_of_all_item_qty):
    return 0    



def calculate_final_price(list_of_vendor_total_prices, target_profit,
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