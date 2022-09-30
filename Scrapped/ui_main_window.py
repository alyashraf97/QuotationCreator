# Form implementation generated from reading ui file 'f:\Github\QuotationCreator\QuoteCreatorQT\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1233, 858)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.quotation_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quotation_groupBox.sizePolicy().hasHeightForWidth())
        self.quotation_groupBox.setSizePolicy(sizePolicy)
        self.quotation_groupBox.setObjectName("quotation_groupBox")
        self.quotation_date_entry = QtWidgets.QDateEdit(self.quotation_groupBox)
        self.quotation_date_entry.setGeometry(QtCore.QRect(120, 140, 91, 27))
        self.quotation_date_entry.setObjectName("quotation_date_entry")
        self.quote_currency_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.quote_currency_label.setGeometry(QtCore.QRect(580, 100, 111, 21))
        self.quote_currency_label.setObjectName("quote_currency_label")
        self.offer_validity_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.offer_validity_label.setGeometry(QtCore.QRect(610, 140, 161, 21))
        self.offer_validity_label.setObjectName("offer_validity_label")
        self.quote_currency_combo = QtWidgets.QComboBox(self.quotation_groupBox)
        self.quote_currency_combo.setGeometry(QtCore.QRect(690, 100, 101, 27))
        self.quote_currency_combo.setObjectName("quote_currency_combo")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.customer_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.customer_label.setGeometry(QtCore.QRect(30, 20, 71, 21))
        self.customer_label.setObjectName("customer_label")
        self.quotation_date_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.quotation_date_label.setGeometry(QtCore.QRect(70, 140, 41, 21))
        self.quotation_date_label.setObjectName("quotation_date_label")
        self.offer_validity_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.offer_validity_field.setGeometry(QtCore.QRect(770, 140, 61, 27))
        self.offer_validity_field.setObjectName("offer_validity_field")
        self.set_date_to_today_button = QtWidgets.QPushButton(self.quotation_groupBox)
        self.set_date_to_today_button.setGeometry(QtCore.QRect(220, 140, 71, 27))
        self.set_date_to_today_button.setObjectName("set_date_to_today_button")
        self.request_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.request_field.setGeometry(QtCore.QRect(110, 60, 441, 27))
        self.request_field.setObjectName("request_field")
        self.request_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.request_label.setGeometry(QtCore.QRect(30, 60, 71, 21))
        self.request_label.setObjectName("request_label")
        self.customer_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.customer_field.setGeometry(QtCore.QRect(110, 20, 441, 27))
        self.customer_field.setObjectName("customer_field")
        self.target_profit_percent_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.target_profit_percent_label.setGeometry(QtCore.QRect(1030, 100, 21, 21))
        self.target_profit_percent_label.setObjectName("target_profit_percent_label")
        self.target_profit_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.target_profit_field.setGeometry(QtCore.QRect(950, 100, 71, 27))
        self.target_profit_field.setObjectName("target_profit_field")
        self.manufacturer_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.manufacturer_label.setGeometry(QtCore.QRect(570, 20, 111, 21))
        self.manufacturer_label.setObjectName("manufacturer_label")
        self.delivery_type_combo = QtWidgets.QComboBox(self.quotation_groupBox)
        self.delivery_type_combo.setGeometry(QtCore.QRect(410, 140, 171, 27))
        self.delivery_type_combo.setObjectName("delivery_type_combo")
        self.delivery_type_combo.addItem("")
        self.delivery_type_combo.addItem("")
        self.delivery_type_combo.addItem("")
        self.delivery_type_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.delivery_type_label.setGeometry(QtCore.QRect(310, 140, 101, 21))
        self.delivery_type_label.setObjectName("delivery_type_label")
        self.manufacturer_label_2 = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.manufacturer_label_2.setGeometry(QtCore.QRect(690, 20, 381, 27))
        self.manufacturer_label_2.setObjectName("manufacturer_label_2")
        self.target_profit_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.target_profit_label.setGeometry(QtCore.QRect(830, 100, 121, 21))
        self.target_profit_label.setObjectName("target_profit_label")
        self.quote_ref_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.quote_ref_field.setGeometry(QtCore.QRect(110, 100, 291, 27))
        self.quote_ref_field.setObjectName("quote_ref_field")
        self.payment_term_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.payment_term_label.setGeometry(QtCore.QRect(580, 60, 101, 21))
        self.payment_term_label.setObjectName("payment_term_label")
        self.quote_ref_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.quote_ref_label.setGeometry(QtCore.QRect(30, 100, 61, 21))
        self.quote_ref_label.setObjectName("quote_ref_label")
        self.payment_term_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.payment_term_field.setGeometry(QtCore.QRect(690, 60, 381, 27))
        self.payment_term_field.setObjectName("payment_term_field")
        self.save_to_file_button = QtWidgets.QPushButton(self.quotation_groupBox)
        self.save_to_file_button.setGeometry(QtCore.QRect(1080, 20, 131, 31))
        self.save_to_file_button.setObjectName("save_to_file_button")
        self.export_to_pdf_button = QtWidgets.QPushButton(self.quotation_groupBox)
        self.export_to_pdf_button.setGeometry(QtCore.QRect(1080, 60, 131, 31))
        self.export_to_pdf_button.setObjectName("export_to_pdf_button")
        self.export_to_excel_button = QtWidgets.QPushButton(self.quotation_groupBox)
        self.export_to_excel_button.setGeometry(QtCore.QRect(1080, 100, 131, 31))
        self.export_to_excel_button.setObjectName("export_to_excel_button")
        self.vat_state_combo = QtWidgets.QComboBox(self.quotation_groupBox)
        self.vat_state_combo.setGeometry(QtCore.QRect(910, 140, 171, 27))
        self.vat_state_combo.setObjectName("vat_state_combo")
        self.vat_state_combo.addItem("")
        self.vat_state_combo.addItem("")
        self.vat_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.vat_label.setGeometry(QtCore.QRect(870, 140, 31, 21))
        self.vat_label.setObjectName("vat_label")
        self.ref_number_generator_button = QtWidgets.QPushButton(self.quotation_groupBox)
        self.ref_number_generator_button.setGeometry(QtCore.QRect(410, 100, 141, 27))
        self.ref_number_generator_button.setObjectName("ref_number_generator_button")
        self.listWidget = QtWidgets.QListWidget(self.quotation_groupBox)
        self.listWidget.setGeometry(QtCore.QRect(30, 220, 241, 571))
        self.listWidget.setObjectName("listWidget")
        self.vendor_name_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.vendor_name_label.setGeometry(QtCore.QRect(300, 220, 91, 21))
        self.vendor_name_label.setObjectName("vendor_name_label")
        self.vendor_lead_time_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.vendor_lead_time_field.setGeometry(QtCore.QRect(440, 280, 161, 27))
        self.vendor_lead_time_field.setObjectName("vendor_lead_time_field")
        self.vendor_shippingcost_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.vendor_shippingcost_label.setGeometry(QtCore.QRect(660, 310, 101, 21))
        self.vendor_shippingcost_label.setObjectName("vendor_shippingcost_label")
        self.vendor_currency_combo = QtWidgets.QComboBox(self.quotation_groupBox)
        self.vendor_currency_combo.setGeometry(QtCore.QRect(390, 250, 101, 27))
        self.vendor_currency_combo.setObjectName("vendor_currency_combo")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.vendor_name_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.vendor_name_field.setGeometry(QtCore.QRect(390, 220, 281, 27))
        self.vendor_name_field.setObjectName("vendor_name_field")
        self.shipping_cost_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.shipping_cost_field.setGeometry(QtCore.QRect(740, 310, 191, 27))
        self.shipping_cost_field.setText("")
        self.shipping_cost_field.setObjectName("shipping_cost_field")
        self.vendor_packingcost_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.vendor_packingcost_label.setGeometry(QtCore.QRect(300, 310, 191, 21))
        self.vendor_packingcost_label.setObjectName("vendor_packingcost_label")
        self.vendor_currency_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.vendor_currency_label.setGeometry(QtCore.QRect(300, 250, 111, 21))
        self.vendor_currency_label.setObjectName("vendor_currency_label")
        self.vendor_customs_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.vendor_customs_label.setGeometry(QtCore.QRect(670, 280, 71, 21))
        self.vendor_customs_label.setObjectName("vendor_customs_label")
        self.custome_percent_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.custome_percent_field.setGeometry(QtCore.QRect(740, 280, 121, 27))
        self.custome_percent_field.setObjectName("custome_percent_field")
        self.packing_cost_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.packing_cost_field.setGeometry(QtCore.QRect(440, 310, 161, 27))
        self.packing_cost_field.setObjectName("packing_cost_field")
        self.vendor_leadtime_label = QtWidgets.QLabel(self.quotation_groupBox)
        self.vendor_leadtime_label.setGeometry(QtCore.QRect(300, 280, 191, 21))
        self.vendor_leadtime_label.setObjectName("vendor_leadtime_label")
        self.label = QtWidgets.QLabel(self.quotation_groupBox)
        self.label.setGeometry(QtCore.QRect(30, 200, 47, 13))
        self.label.setObjectName("label")
        self.vendor_add_button = QtWidgets.QToolButton(self.quotation_groupBox)
        self.vendor_add_button.setGeometry(QtCore.QRect(210, 200, 25, 19))
        self.vendor_add_button.setObjectName("vendor_add_button")
        self.vendor_remove_button = QtWidgets.QToolButton(self.quotation_groupBox)
        self.vendor_remove_button.setGeometry(QtCore.QRect(240, 200, 25, 19))
        self.vendor_remove_button.setObjectName("vendor_remove_button")
        self.label_2 = QtWidgets.QLabel(self.quotation_groupBox)
        self.label_2.setGeometry(QtCore.QRect(300, 340, 47, 13))
        self.label_2.setObjectName("label_2")
        self.target_profit_label_2 = QtWidgets.QLabel(self.quotation_groupBox)
        self.target_profit_label_2.setGeometry(QtCore.QRect(720, 220, 121, 21))
        self.target_profit_label_2.setObjectName("target_profit_label_2")
        self.vendor_comission_field = QtWidgets.QLineEdit(self.quotation_groupBox)
        self.vendor_comission_field.setGeometry(QtCore.QRect(820, 220, 71, 27))
        self.vendor_comission_field.setText("")
        self.vendor_comission_field.setObjectName("vendor_comission_field")
        self.target_profit_percent_label_2 = QtWidgets.QLabel(self.quotation_groupBox)
        self.target_profit_percent_label_2.setGeometry(QtCore.QRect(900, 220, 21, 21))
        self.target_profit_percent_label_2.setObjectName("target_profit_percent_label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.quotation_groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(300, 360, 911, 421))
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.quotation_groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1233, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCurrency_Conversions = QtGui.QAction(MainWindow)
        self.actionCurrency_Conversions.setObjectName("actionCurrency_Conversions")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCurrency_Conversions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quote_currency_label.setText(_translate("MainWindow", "Quote Currency"))
        self.offer_validity_label.setText(_translate("MainWindow", "Offer Vailidity (Months)"))
        self.quote_currency_combo.setItemText(0, _translate("MainWindow", "EUR"))
        self.quote_currency_combo.setItemText(1, _translate("MainWindow", "USD"))
        self.quote_currency_combo.setItemText(2, _translate("MainWindow", "GBP"))
        self.quote_currency_combo.setItemText(3, _translate("MainWindow", "EGP"))
        self.quote_currency_combo.setItemText(4, _translate("MainWindow", "CHF"))
        self.quote_currency_combo.setItemText(5, _translate("MainWindow", "AED"))
        self.customer_label.setText(_translate("MainWindow", "Customer"))
        self.quotation_date_label.setText(_translate("MainWindow", "Date"))
        self.set_date_to_today_button.setText(_translate("MainWindow", "Today"))
        self.request_label.setText(_translate("MainWindow", "Request"))
        self.target_profit_percent_label.setText(_translate("MainWindow", "%"))
        self.manufacturer_label.setText(_translate("MainWindow", "Manufacturer(s)"))
        self.delivery_type_combo.setItemText(0, _translate("MainWindow", "CIF"))
        self.delivery_type_combo.setItemText(1, _translate("MainWindow", "Site Delivery"))
        self.delivery_type_combo.setItemText(2, _translate("MainWindow", "Other"))
        self.delivery_type_label.setText(_translate("MainWindow", "Delivery Type"))
        self.target_profit_label.setText(_translate("MainWindow", "Target PO Profit"))
        self.payment_term_label.setText(_translate("MainWindow", "Payment Term"))
        self.quote_ref_label.setText(_translate("MainWindow", "Ref. No."))
        self.save_to_file_button.setText(_translate("MainWindow", "Save to File"))
        self.export_to_pdf_button.setText(_translate("MainWindow", "Export to PDF"))
        self.export_to_excel_button.setText(_translate("MainWindow", "Export to Excel"))
        self.vat_state_combo.setItemText(0, _translate("MainWindow", "Included"))
        self.vat_state_combo.setItemText(1, _translate("MainWindow", "Not Included"))
        self.vat_label.setText(_translate("MainWindow", "VAT"))
        self.ref_number_generator_button.setText(_translate("MainWindow", "Generate"))
        self.vendor_name_label.setText(_translate("MainWindow", "Vendor Name:"))
        self.vendor_shippingcost_label.setText(_translate("MainWindow", "Shipping Cost"))
        self.vendor_currency_combo.setItemText(0, _translate("MainWindow", "EUR"))
        self.vendor_currency_combo.setItemText(1, _translate("MainWindow", "USD"))
        self.vendor_currency_combo.setItemText(2, _translate("MainWindow", "GBP"))
        self.vendor_currency_combo.setItemText(3, _translate("MainWindow", "EGP"))
        self.vendor_currency_combo.setItemText(4, _translate("MainWindow", "CHF"))
        self.vendor_currency_combo.setItemText(5, _translate("MainWindow", "AED"))
        self.vendor_packingcost_label.setText(_translate("MainWindow", "Packing & Legalization Cost:"))
        self.vendor_currency_label.setText(_translate("MainWindow", "Vendor Currency:"))
        self.vendor_customs_label.setText(_translate("MainWindow", "Customs"))
        self.vendor_leadtime_label.setText(_translate("MainWindow", "Vendor Lead Time (Weeks):"))
        self.label.setText(_translate("MainWindow", "Vendors"))
        self.vendor_add_button.setText(_translate("MainWindow", "+"))
        self.vendor_remove_button.setText(_translate("MainWindow", "-"))
        self.label_2.setText(_translate("MainWindow", "Items"))
        self.target_profit_label_2.setText(_translate("MainWindow", "Vendor Commission:"))
        self.target_profit_percent_label_2.setText(_translate("MainWindow", "%"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Part number"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Qty"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Unit Price"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Total Price"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCurrency_Conversions.setText(_translate("MainWindow", "Currency Conversions"))