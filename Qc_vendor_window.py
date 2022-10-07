from tokenize import Name
from QuoteCreatorQT.ui_Vendor import Ui_vendorPopup
from QuoteCreatorQT.ui_vendor_window import Ui_Dialog
from Qc_DataClasses import *
from PyQt6 import QtWidgets, uic,QtGui
import sqlite3

class vendor_window(QtWidgets.QDialog,Ui_Dialog):



    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.mainwindow = parent
        self.con = sqlite3.connect("DB.db")
        self.setupUi(self)
        self.setWindowTitle("Vendor Manager")
        self.refreshVendorChoices()
        

        #button setup
        self.make_choice_button.clicked.connect(lambda : self.VendorWindow(self.vendor_list.currentRow()+1))
        self.cancel_button.clicked.connect(lambda: self.hide())

    def refreshVendorChoices(self):
        results = self.con.execute("Select * FROM Vendors")
        self.vendor_list.reset()

        for vendor in results:
            self.vendor_list.addItem(vendor[1])   



    def VendorWindow(self,vendorIndex = None):
        if(vendorIndex == 0):
            self.errorMessage("Please make a Choice")
            return

        for vendor in self.mainwindow.vendor_Array:
            if(vendor.vendorDBID == vendorIndex):
                self.errorMessage("Vendor Already Added")
                return

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

        self.mainwindow.vendor_Array.append(Vendor(tempVendor))
        self.mainwindow.refreshVendors()
        self.openWindow.hide()
        self.hide()


    def errorMessage(self,string):
        errMsg=QtWidgets.QMessageBox()
        errMsg.setText(string)
        errMsg.setWindowTitle("Error")
        errMsg.exec()

class VendorDialog(QtWidgets.QDialog, Ui_vendorPopup):
        def __init__(self, parent=None):
            QtWidgets.QDialog.__init__(self, parent)
            self.setupUi(self)