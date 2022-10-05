from email.quoprimime import quote
import typing
import Qc_main_window, Qc_data_manip, Qc_excel_manip, Qc_pdf_manip
import sys
from PyQt6 import QtWidgets

  
    
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Qc_main_window.MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()