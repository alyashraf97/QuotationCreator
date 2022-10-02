from email.quoprimime import quote
import typing
import Qc_main_window, Qc_data_manip, Qc_excel_manip, Qc_pdf_manip
import sys
from PyQt6 import QtWidgets
from QuoteCreatorQT.Ui_main_window import Ui_MainWindow
  
    
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Qc_main_window.MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()