import this
import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip
from email.quoprimime import quote
import typing
import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip
import sys
import sqlite3
from PyQt6 import QtWidgets, uic,QtGui
from QuoteCreatorQT.Ui_main_window import Ui_MainWindow
from QuoteCreatorQT.ui_Vendor import Ui_vendorPopup

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.con = sqlite3.connect("DB.db")
        self.setupUi(self)
        self.openWindow = None
        self.vendor_Array = []

        #Button Setup
        self.Add_Vendor_Button.clicked.connect(lambda: self.VendorWindow(self.Vendor_ComboBox.currentIndex()+1))

        self.refreshVendorChoices()
        self.refreshVendors()
    
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
    
        
        
    def refreshVendorChoices(self):
        results = self.con.execute("Select * FROM Vendors")
        self.Vendor_ComboBox.clear()

        for vendor in results:
            self.Vendor_ComboBox.addItem(vendor[1])    

    def refreshVendors(self):
        self.vendor_list.clear()

        for vendor in self.vendor_Array:
            self.vendor_list.addItem(vendor.vendorName)

    def addNewVendor(self,vendorIndex):
        
        tempVendor = {
            "DBID" : vendorIndex,
            "Name" : self.openWindow.vendor_name_field.text(),
            "Comission" : self.openWindow.vendor_comission_field.text(),
            "Packing Cost" : self.openWindow.packing_cost_field.text(),
            "Shipping Cost" : self.openWindow.shipping_cost_field.text(),
            "Customs" : self.openWindow.customs_percent_field.text(),
            "Currency" : self.openWindow.vendor_currency_combo.currentText(),
            "Lead Time" : self.openWindow.vendor_lead_time_field.text(),
        }

        for key in tempVendor:
            if(tempVendor[key] == ""):
                self.errorMessage(key + " is empty.")
                return

        self.vendor_Array.append(Vendor(tempVendor))
        self.refreshVendors()
        self.openWindow.hide()
        
    def VendorWindow(self,vendorIndex= None):
        self.openWindow = VendorDialog(self)
        onlyFloat = QtGui.QDoubleValidator()
        onlyFloat.setBottom(0)
        onlyInt = QtGui.QIntValidator()
        onlyInt.setBottom(0)
        self.openWindow.packing_cost_field.setValidator(onlyFloat)
        self.openWindow.shipping_cost_field.setValidator(onlyFloat)
        self.openWindow.vendor_comission_field.setValidator(onlyFloat)
        self.openWindow.customs_percent_field.setValidator(onlyFloat)
        self.openWindow.vendor_lead_time_field.setValidator(onlyInt)

        if(vendorIndex == None):
            self.openWindow.show()
        else:
            query = self.con.cursor()
            query.execute("Select * FROM Vendors WHERE ID={} ;".format(vendorIndex))
            result = query.fetchone()

            self.openWindow.setWindowTitle("Add Vendor")
            

            self.openWindow.vendor_name_field.setEnabled(False)
            self.openWindow.vendor_name_field.setText(result[1])

            self.openWindow.vendor_currency_combo.setEnabled(False)
            self.openWindow.vendor_currency_combo.setItemText(0,result[2])
            self.openWindow.show()

        self.openWindow.vendorPopupBtnBox.accepted.connect(lambda: self.addNewVendor(vendorIndex))
        self.openWindow.vendorPopupBtnBox.rejected.connect(lambda: self.openWindow.hide())


    def errorMessage(self,string):
        errMsg=QtWidgets.QMessageBox()
        errMsg.setText(string)
        errMsg.setWindowTitle("Error")
        errMsg.exec()

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
            self.vendorDBID = vendorData["DBID"]
            self.vendorName = vendorData["Name"]
            self.vendorComission = float(vendorData["Comission"])
            self.vendorPackingCost = float(vendorData["Packing Cost"])
            self.vendorShippingCost = float(vendorData["Shipping Cost"])
            self.vendorCustoms = float(vendorData["Customs"])
            self.vendorCurrency = vendorData["Currency"]
            self.vendorLeadTime = int(vendorData["Lead Time"])
    
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

class VendorDialog(QtWidgets.QDialog, Ui_vendorPopup):
        def __init__(self, parent=None):
            QtWidgets.QDialog.__init__(self, parent)
            self.setupUi(self)
            
                

'''class Quote():
    def __init__(self,allQuoteInformation):
        if(allQuoteInformation != None):
            self.quoteInformation = allQuoteInformation["quoteInformation"]
            self.allVendorData = allQuoteInformation["allVendorData"]
            #self.allItemData = [allQuoteInformation["allVendorData"]["key"] for key in dict.fromkeys(allQuoteInformation["allVendorData"])]

            for i in range(len(allQuoteInformation['allVendorData'])):'''