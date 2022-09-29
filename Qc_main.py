from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from QuoteCreatorQT.Ui_untitled import Ui_MainWindow

import imp
import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip, Qc_gui


class App(QtWidgets.QMainWindow,Ui_MainWindow):
    

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.add_vendor_button.clicked.connect(self.AddVendor)

    def AddVendor(self):
        vendorName = self.vendor_name_field.text()
        packing = self.packing_cost_field.text()
        shippingCost = self.shipping_cost_field.text()
        vendorCurrency = self.vendor_currency_combo.currentText()
        vendorLeadTime = self.vendor_lead_time_field.text()
        vendorCustomPercent = self.custome_percent_field.text()

        print(vendorName)
        print(packing)
        print(shippingCost)
        print(vendorCurrency)
        print(vendorLeadTime)
        print(vendorCustomPercent)


def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

