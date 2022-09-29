import Qc_data_manip, Qc_excel_manip, Qc_pdf_manip, Qc_gui
import sys
from PyQt6 import QtWidgets, uic

from QuoteCreatorQT.ui_main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()