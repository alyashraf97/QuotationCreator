# Form implementation generated from reading ui file 'f:\Github\QuotationCreator\QuoteCreatorQT\vendor_NewEdit.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(236, 218)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.vendor_name_field = QtWidgets.QLineEdit(Dialog)
        self.vendor_name_field.setObjectName("vendor_name_field")
        self.gridLayout.addWidget(self.vendor_name_field, 0, 1, 1, 2)
        self.ok_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 4, 1, 1, 1)
        self.currency_combo_field = QtWidgets.QComboBox(Dialog)
        self.currency_combo_field.setObjectName("currency_combo_field")
        self.currency_combo_field.addItem("")
        self.currency_combo_field.addItem("")
        self.currency_combo_field.addItem("")
        self.currency_combo_field.addItem("")
        self.currency_combo_field.addItem("")
        self.currency_combo_field.addItem("")
        self.gridLayout.addWidget(self.currency_combo_field, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.internal_id_field = QtWidgets.QLineEdit(Dialog)
        self.internal_id_field.setEnabled(False)
        self.internal_id_field.setObjectName("internal_id_field")
        self.gridLayout.addWidget(self.internal_id_field, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.ok_button.setText(_translate("Dialog", "Ok"))
        self.currency_combo_field.setItemText(0, _translate("Dialog", "EUR"))
        self.currency_combo_field.setItemText(1, _translate("Dialog", "USD"))
        self.currency_combo_field.setItemText(2, _translate("Dialog", "GPB"))
        self.currency_combo_field.setItemText(3, _translate("Dialog", "EGP"))
        self.currency_combo_field.setItemText(4, _translate("Dialog", "CHF"))
        self.currency_combo_field.setItemText(5, _translate("Dialog", "AED"))
        self.label_2.setText(_translate("Dialog", "Currency:"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.label_3.setText(_translate("Dialog", "Internal ID:"))
