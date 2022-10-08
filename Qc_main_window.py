import this
import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip
from email.quoprimime import quote
import typing
import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip
import sys
import sqlite3
from PyQt6 import QtWidgets, uic,QtGui
from Qc_vendor_window import vendor_window
from QuoteCreatorQT.Ui_main_window import Ui_MainWindow
import Qc_DataClasses

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.openWindow = None
        self.vendor_Array = []

        #Button Setup
        self.vendor_add_window_button.clicked.connect(lambda: self.showVendorMenu())
        self.vendor_remove_button.clicked.connect(lambda: self.removeVendor(self.vendor_list.currentRow()))
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
    
        
    def closeOpenWindow(self):
        self.openWindow.close()
        self.openWindow = None

    def showVendorMenu(self):
        if(self.openWindow != None):
            return

        self.openWindow = vendor_window(self)
        self.openWindow.show()

    def refreshVendors(self):
        self.vendor_list.clear()

        for vendor in self.vendor_Array:
            self.vendor_list.addItem(vendor.vendorName)

    def removeVendor(self,vendorIndex):
        if(vendorIndex == -1):
            return
        
        self.vendor_Array.pop(vendorIndex)
        self.refreshVendors()

    def errorMessage(self,string):
        errMsg=QtWidgets.QMessageBox()
        errMsg.setText(string)
        errMsg.setWindowTitle("Error")
        errMsg.exec()

    def generate_excel(self):
        pass
    
    def generate_pdf(self):
        pass
    
    def save_file(self):
        allQuoteData={}
        return


            
                

'''class Quote():
    def __init__(self,allQuoteInformation):
        if(allQuoteInformation != None):
            self.quoteInformation = allQuoteInformation["quoteInformation"]
            self.allVendorData = allQuoteInformation["allVendorData"]
            #self.allItemData = [allQuoteInformation["allVendorData"]["key"] for key in dict.fromkeys(allQuoteInformation["allVendorData"])]

            for i in range(len(allQuoteInformation['allVendorData'])):'''