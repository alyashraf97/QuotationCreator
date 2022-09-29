import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip, Qc_gui
import sys
from PyQt6 import QtWidgets, uic

from QuoteCreatorQT.ui_main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.vendor_add_button.clicked.connect(self.AddVendor)

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
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()