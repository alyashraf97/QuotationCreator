from locale import currency
from tokenize import Name
from QuoteCreatorQT.ui_Vendor import Ui_vendorPopup
from QuoteCreatorQT.ui_vendor_window import Ui_Dialog
import QuoteCreatorQT.ui_vendor_NewEdit
from Qc_DataClasses import *
from PyQt6 import QtWidgets, uic,QtGui,QtCore
import sqlite3

class vendor_window(QtWidgets.QDialog,Ui_Dialog):



    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.mainwindow = parent
        self.openWindow = None
        self.setupUi(self)
        self.setWindowTitle("Vendor Manager")
        self.refreshVendorChoices()

        #button setup
        self.make_choice_button.clicked.connect(lambda : self.VendorWindow(self.vendor_list.currentRow()))
        self.cancel_button.clicked.connect(lambda: self.mainwindow.closeOpenWindow())
        self.new_vendor_button.clicked.connect(lambda: self.VendorManageWindow())
        self.edit_vendor_button.clicked.connect(lambda: self.VendorManageWindow(self.vendor_list.currentRow()))
        self.delete_vendor_button.clicked.connect(lambda: self.deleteVendorFromDB(self.vendor_list.currentRow()))

    def refreshVendorChoices(self):
        con = sqlite3.connect("DB.db")
        results = con.execute("Select * FROM Vendors")
        self.vendor_list.clear()
        
        for vendor in results:
            self.vendor_list.addItem(vendor[1])   
        con.close()

    def closeOpenWindow(self):
            self.openWindow.close()
            self.openWindow = None

    def closeEvent(self, event):
        self.mainwindow.closeOpenWindow()
        event.accept()

    def VendorWindow(self,vendorIndex = None):
        if(self.openWindow != None):
            return

        if(vendorIndex == -1):
            self.errorMessage("Please make a Choice")
            return

        con = sqlite3.connect("DB.db")
        query = con.cursor()
        query.execute("Select * FROM Vendors")
        result = query.fetchall()
        realID = result[vendorIndex][0]

        for vendor in self.mainwindow.vendor_Array:
            if(vendor.vendorDBID == realID):
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

        self.openWindow.setWindowTitle("Add Vendor")
        

        self.openWindow.vendor_name_field.setEnabled(False)
        self.openWindow.vendor_name_field.setText(result[vendorIndex][1])

        self.openWindow.vendor_currency_combo.setEnabled(False)
        self.openWindow.vendor_currency_combo.setItemText(0,result[vendorIndex][2])
        self.openWindow.show()

        self.openWindow.vendorPopupBtnBox.accepted.connect(lambda: self.addNewVendorToMain(realID))
        self.openWindow.vendorPopupBtnBox.rejected.connect(lambda: self.closeOpenWindow())
        con.close()

    def addNewVendorToMain(self,vendorIndex):
        
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
        self.closeOpenWindow()
        self.mainwindow.closeOpenWindow()


    def VendorManageWindow(self,vendorIndex=None):
        if(vendorIndex == -1):
            self.errorMessage("Please make a Choice")
            return
    
        self.openWindow = VendorManageDialog(self)
        con = sqlite3.connect("DB.db")
        query = con.cursor()
        
        if(vendorIndex != None):
            query = con.cursor()
            query.execute("Select * FROM Vendors")
            result = query.fetchall()
            realID = result[vendorIndex][0]
            self.openWindow.setWindowTitle("Edit " + result[vendorIndex][1])
            self.openWindow.internal_id_field.setText(str(realID))
            self.openWindow.vendor_name_field.setText(result[vendorIndex][1])
            index = self.openWindow.currency_combo_field.findText(result[vendorIndex][2])
            if index >= 0:
                self.openWindow.currency_combo_field.setCurrentIndex(index)
        else:
            self.openWindow.setWindowTitle("Add Vendor")

        con.close()
        self.openWindow.cancel_button.clicked.connect(lambda: self.closeOpenWindow())
        self.openWindow.ok_button.clicked.connect(lambda: self.VendorToDB(vendorIndex))
        self.openWindow.show()

    def VendorToDB(self,vendorIndex):
        name = self.openWindow.vendor_name_field.text()
        currency = self.openWindow.currency_combo_field.currentText()

        con = sqlite3.connect("DB.db")
        query = con.cursor()
        if(vendorIndex == None):
            query.execute("INSERT INTO Vendors (Name,Currency) VALUES ('{}' , '{}');".format(name,currency))
        else:
            realID = self.getRealID(vendorIndex)
            query.execute("UPDATE Vendors SET name = '{}', Currency = '{}' WHERE ID = {}".format(name,currency,realID))
            
        con.commit()
        self.refreshVendorChoices()
        self.closeOpenWindow()
        con.close()

    def deleteVendorFromDB(self,vendorIndex):
        con = sqlite3.connect("DB.db")
        query = con.cursor()

        realID = self.getRealID(vendorIndex)
        query.execute("DELETE FROM Vendors WHERE ID = {}".format(realID))
        con.commit()
        con.close()
        self.refreshVendorChoices()

    def getRealID(self,vendorIndex):
        con = sqlite3.connect("DB.db")
        query = con.cursor()
        query.execute("Select * FROM Vendors")
        result = query.fetchall()
        realID = result[vendorIndex][0]

        return realID

    def errorMessage(self,string):
        errMsg=QtWidgets.QMessageBox()
        errMsg.setText(string)
        errMsg.setWindowTitle("Error")
        errMsg.exec()

class VendorDialog(QtWidgets.QDialog, Ui_vendorPopup):
        def __init__(self, parent=None):
            QtWidgets.QDialog.__init__(self, parent)
            self.setupUi(self)
            self.mainwindow = parent

        def closeEvent(self, event):
            self.mainwindow.closeOpenWindow()
            event.accept()

class VendorManageDialog(QtWidgets.QDialog,QuoteCreatorQT.ui_vendor_NewEdit.Ui_Dialog):
        def __init__(self, parent=None):
                    QtWidgets.QDialog.__init__(self, parent)
                    self.setupUi(self)
                    self.mainwindow = parent
        
        def closeEvent(self, event):
                self.mainwindow.closeOpenWindow()
                event.accept()