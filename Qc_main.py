import typing
import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip, Qc_gui
import sys
from PyQt5 import QtWidgets, uic, QtCore
from QuoteCreatorQT.Ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
    
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()