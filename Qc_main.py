from email.quoprimime import quote
import typing
import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip, Qc_gui
import sys
from PyQt6 import QtWidgets
from QuoteCreatorQT.Ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    vendors = []

    def __init__(self, *args, obj=None, **kwargs):
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
        vendorComission=float(self.vendor_comission_field.text())
        vendorPackingCost=float(self.packing_cost_field.text())
        vendorShippingCost=float(self.shipping_cost_field.text())
        vendorCustoms=float(self.vendor_comission_field.text())
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
        self.vendor_list.clear()

        for vendor in self.vendors:
            self.vendor_list.addItem(vendor.vendorName)    
        
    def addNewVendor(self):
        self.vendors.append(Vendor())
        self.vendor_list.addItem("New Vendor")


    def add_item(self):
        pass
    
    def generate_excel(self):
        pass
    
    def generate_pdf(self):
        pass
    
    def save_file(self):
        currentQuoteDataJson={}
        return

class Quote:
     def __init__(self,qouteData = None):
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()