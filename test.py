from PyQt6 import QtWidgets, uic,QtGui
from QuoteCreatorQT.Ui_main_window import Ui_MainWindow
from Qc_main_window import MainWindow
from QuoteCreatorQT.ui_Vendor import Ui_vendorPopup
import sys

class Dialog(QtWidgets.QDialog, Ui_vendorPopup):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

        
def vendorWindow(vendor = None):
    if(vendor == None):
        window = Dialog()
        window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

main()