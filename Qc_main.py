from email.quoprimime import quote
import typing
import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip
import sys
from PyQt6 import QtWidgets
from QuoteCreatorQT.Ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
    #self.vendors=[]
    
    
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()