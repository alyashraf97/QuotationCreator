import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip
from email.quoprimime import quote
import typing
import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip
import sys
from PyQt6 import QtWidgets, uic
from QuoteCreatorQT.Ui_main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        self.allVendorData=[]
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)    
    
    def get_quote_data(self):
        customer=self.customer_field.text()
        manufacturers=self.manufacturer_field.text()
        request=self.request_field.text()
        paymentTerm=self.payment_term_field.text
        refNo=self.quote_ref_field.text()
        quoteDate=self.quotation_date_entry.text()
        quoteCurrency=self.quote_currency_combo.currentText()
        vatStatus=self.vat_state_combo.currentText()
        targetProfit=float(self.target_profit_field.text())
        offerValidity=int(self.offer_validity_field.text())
        deliveryType=self.delivery_type_field.text()
        
        quoteData = {
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
        }
        return quoteData
    
    
    def get_vendor_data(self):
        vendorName=self.vendor_name_field.text()        
        vendorComission=float(self.vendorComission_field.text())
        vendorPackingCost=float(self.packing_cost_field.text())
        vendorShippingCost=float(self.shipping_cost_field.text())
        vendorCustoms=float(self.vendorComission_field.text())
        vendorCurrency=self.vendor_currency_combo.currentText()
        vendorLeadTime=int(self.vendor_lead_time_field.text())
        
        vendorData={
                "vendorName":vendorName,
                'vendorComission':vendorComission,
                'vendorPackingCost':vendorPackingCost,
                'vendorShippingCost':vendorShippingCost,
                'vendorCustoms':vendorCustoms,
                'vendorCurrency':vendorCurrency,
                'vendorLeadTime':vendorLeadTime,
                }
        return vendorData
        
        
    def refreshVendorlist(self):
        self.allVendorData.clear()

        for vendor in self.allVendorData:
            self.allVendorData.addItem(vendor.vendorName)    
        
    def addNewVendor(self):
        self.allVendorData.append(Vendor(self.get_vendor_data()))
        #self.vendor_list.addItem("New Vendor")


    def add_item(self):
        pass
    
    def generate_excel(self):
        pass
    
    def generate_pdf(self):
        pass
    
    def save_file(self):
        allQuoteData={}
        return

class Quote:
    def __init__(self,qouteData = None):
        #self.listing_of_all_vendors=listing_of_all_vendors
        if(qouteData != None):
            self.customer = qouteData["customer"]
            self.manufacturers = qouteData["manufacturers"]
            self.request = qouteData["request"]
            self.paymentTerm = qouteData["paymentTerm"]
            self.refNo = qouteData["refNo"]
            self.quoteDate = qouteData["quoteDate"]
            self.quoteCurrency = qouteData["quoteCurrency"]
            self.vatStatus = qouteData["vatStatus"]
            self.targetProfit = qouteData["targetProfit"]
            self.offerValidity = qouteData["offerValidity"]
            self.deliveryType = qouteData["deliveryType"]
        

        #def __init__(self,listing_of_all_vendors):
            #self.listing_of_all_vendors=listing_of_all_vendors
           # self.final_prices=self.calculate_final_price'''

        
        #def seperate_vendor(self,vendor_name):
        #vendor_list_of_unit_prices=self.listing_of_all_vendors[f'{vendor_name}']

        #return vendor_list_of_unit_prices'''

    def calculate_vendor_price_data(self, vendorEntryData):
        vendorInitialUnitPrices=vendorEntryData["vendorInitialUnitPrices"]


    
    
    
    
    
    
    
    
    def get_initial_item_weights(self,vendorUnitPrices1):
        #Returns item weights (vendor by vendor basis)
        #Takes a list of item prices (before markup) and returns a list of weights
        item_weights=[]
        total_sum=sum(vendorUnitPrices1)
        for i in range(len(vendorUnitPrices1)):
            item_weights[i]=vendorUnitPrices1[i]/total_sum
        return item_weights

    def final_vendor_prices(self,vendorUnitPrices1,vendorBoq, 
                            vendorPacking, vendorShipping, vendorCustoms, 
                            vendorComission):
        vendor_price_listing={}
        vendor_sum=int()
        list_of_item_total_prices=[]

        #generating a sum of item total prices & a list of item total prices
        for i in range(len(vendorUnitPrices1)):
            vendor_sum+=vendorUnitPrices1[i]*vendorBoq[i]
            list_of_item_total_prices[i]=(vendorUnitPrices1[i]*(1-vendorComission))*vendorBoq[i]

        vendor_final_sum=vendor_sum+vendorCustoms+vendorPacking+vendorShipping
        item_weights=self.get_initial_item_weights(vendorUnitPrices1)
        vendorFinalPriceList=[vendor_final_sum*item_weights[i] for i in range(len(vendorUnitPrices1))]

        vendor_price_listing={
            "vendorFinalSum": vendor_final_sum,
            "vendorTotalPricesFinal":vendorFinalPriceList
        }    
        
        return vendor_price_listing
    

    def get_vendor_display_unit_price(self, vendorFinalPriceList, vendorBoq):
        vendor_display_unit_prices=[]
        for i in range(len(vendorBoq)):
            vendor_display_unit_prices[i]=vendorFinalPriceList['vendorTotalPricesFinal'][i]/vendorBoq[i]


        

    def calculate_final_price(self, vendorTotalPricesFinal, target_profit,
                            sales_tax, vat_state):
        cumulative_sum=sum(vendorTotalPricesFinal)
        #for i in range(len(list_of_item_prices)):
            #cumulative_sum+=list_of_item_prices[i]*list_of_item_qty[i]
        
        #final_price=((cumulative_sum/(1-target_profit))*(1+sales_tax))
        if vat_state==True:
            return ((cumulative_sum/(1-target_profit))*(1+sales_tax))
        else:
            return ((cumulative_sum/(1-target_profit))*(1+sales_tax))*1.14

class Vendor:
    def __init__(self,vendorData = None):
        if(vendorData != None):
            self.vendorName = vendorData["vendorName"]
            self.vendorComission = vendorData["vendorComission"]
            self.vendorPackingCost = vendorData["vendorPackingCost"]
            self.vendorShippingCost = vendorData["vendorShippingCost"]
            self.vendorCustoms = vendorData["vendorCustoms"]
            self.vendorCurrency = vendorData["vendorCurrency"]
            self.vendorLeadTime = vendorData["vendorLeadTime"]

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
        self.vendorItems=[]
        if(vendorData != None):
            self.vendorName = vendorData["vendorName"]
            self.vendorComission = float(vendorData["vendorComission"])
            self.vendorPackingCost = float(vendorData["vendorPackingCost"])
            self.vendorShippingCost = float(vendorData["vendorShippingCost"])
            self.vendorCustoms = float(vendorData["vendorCustoms"])
            self.vendorCurrency = vendorData["vendorCurrency"]
            self.vendorLeadTime = int(vendorData["vendorLeadTime"])
    
    #def vendor_add_item(self,itemIndex):
    #    self.vendorItems.append(Item(itemInfo=get_item_info(itemIndex)))
            

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

'''class Quote():
    def __init__(self,allQuoteInformation):
        if(allQuoteInformation != None):
            self.quoteInformation = allQuoteInformation["quoteInformation"]
            self.allVendorData = allQuoteInformation["allVendorData"]
            #self.allItemData = [allQuoteInformation["allVendorData"]["key"] for key in dict.fromkeys(allQuoteInformation["allVendorData"])]

            for i in range(len(allQuoteInformation['allVendorData'])):'''