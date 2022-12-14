# Form implementation generated from reading ui file 'c:\Users\Gebz\Documents\GitHub\QuotationCreator\QuoteCreatorQT\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1142, 631)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.quotation_form_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quotation_form_groupBox.sizePolicy().hasHeightForWidth())
        self.quotation_form_groupBox.setSizePolicy(sizePolicy)
        self.quotation_form_groupBox.setObjectName("quotation_form_groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.quotation_form_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.current_totals_frame = QtWidgets.QFrame(self.quotation_form_groupBox)
        self.current_totals_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.current_totals_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.current_totals_frame.setObjectName("current_totals_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.current_totals_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.total_markup_label = QtWidgets.QLabel(self.current_totals_frame)
        self.total_markup_label.setObjectName("total_markup_label")
        self.gridLayout_6.addWidget(self.total_markup_label, 1, 0, 1, 1)
        self.current_quote_total_number_label = QtWidgets.QLabel(self.current_totals_frame)
        self.current_quote_total_number_label.setObjectName("current_quote_total_number_label")
        self.gridLayout_6.addWidget(self.current_quote_total_number_label, 0, 2, 1, 1)
        self.current_quote_total_label = QtWidgets.QLabel(self.current_totals_frame)
        self.current_quote_total_label.setObjectName("current_quote_total_label")
        self.gridLayout_6.addWidget(self.current_quote_total_label, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.current_totals_frame)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.current_totals_frame)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_6.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.current_totals_frame)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.current_totals_frame)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_6.addWidget(self.lineEdit_3, 0, 5, 1, 1)
        self.current_quote_total_currency_label = QtWidgets.QLabel(self.current_totals_frame)
        self.current_quote_total_currency_label.setObjectName("current_quote_total_currency_label")
        self.gridLayout_6.addWidget(self.current_quote_total_currency_label, 0, 4, 1, 1)
        self.total_markup_percent_label = QtWidgets.QLabel(self.current_totals_frame)
        self.total_markup_percent_label.setObjectName("total_markup_percent_label")
        self.gridLayout_6.addWidget(self.total_markup_percent_label, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.current_totals_frame, 4, 9, 3, 6)
        self.vat_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.vat_label.setObjectName("vat_label")
        self.gridLayout_4.addWidget(self.vat_label, 3, 11, 1, 1)
        self.vat_state_combo = QtWidgets.QComboBox(self.quotation_form_groupBox)
        self.vat_state_combo.setObjectName("vat_state_combo")
        self.vat_state_combo.addItem("")
        self.vat_state_combo.addItem("")
        self.gridLayout_4.addWidget(self.vat_state_combo, 3, 12, 1, 1)
        self.delivery_type_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.delivery_type_label.setObjectName("delivery_type_label")
        self.gridLayout_4.addWidget(self.delivery_type_label, 3, 9, 1, 1)
        self.delivery_type_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.delivery_type_field.setObjectName("delivery_type_field")
        self.gridLayout_4.addWidget(self.delivery_type_field, 3, 10, 1, 1)
        self.manufacturer_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.manufacturer_label.setObjectName("manufacturer_label")
        self.gridLayout_4.addWidget(self.manufacturer_label, 2, 1, 1, 1)
        self.export_to_excel_button = QtWidgets.QPushButton(self.quotation_form_groupBox)
        self.export_to_excel_button.setObjectName("export_to_excel_button")
        self.gridLayout_4.addWidget(self.export_to_excel_button, 2, 14, 1, 1)
        self.request_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.request_label.setObjectName("request_label")
        self.gridLayout_4.addWidget(self.request_label, 3, 1, 1, 1)
        self.save_to_file_button = QtWidgets.QPushButton(self.quotation_form_groupBox)
        self.save_to_file_button.setObjectName("save_to_file_button")
        self.gridLayout_4.addWidget(self.save_to_file_button, 1, 14, 1, 1)
        self.export_to_pdf_button = QtWidgets.QPushButton(self.quotation_form_groupBox)
        self.export_to_pdf_button.setObjectName("export_to_pdf_button")
        self.gridLayout_4.addWidget(self.export_to_pdf_button, 3, 14, 1, 1)
        self.offer_validity_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.offer_validity_field.setObjectName("offer_validity_field")
        self.gridLayout_4.addWidget(self.offer_validity_field, 2, 12, 1, 1)
        self.customer_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_field.sizePolicy().hasHeightForWidth())
        self.customer_field.setSizePolicy(sizePolicy)
        self.customer_field.setMinimumSize(QtCore.QSize(400, 0))
        self.customer_field.setObjectName("customer_field")
        self.gridLayout_4.addWidget(self.customer_field, 1, 3, 1, 2)
        self.customer_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.customer_label.setObjectName("customer_label")
        self.gridLayout_4.addWidget(self.customer_label, 1, 1, 1, 1)
        self.quote_currency_combo = QtWidgets.QComboBox(self.quotation_form_groupBox)
        self.quote_currency_combo.setObjectName("quote_currency_combo")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.quote_currency_combo.addItem("")
        self.gridLayout_4.addWidget(self.quote_currency_combo, 2, 10, 1, 1)
        self.manufacturer_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_field.sizePolicy().hasHeightForWidth())
        self.manufacturer_field.setSizePolicy(sizePolicy)
        self.manufacturer_field.setMinimumSize(QtCore.QSize(400, 0))
        self.manufacturer_field.setObjectName("manufacturer_field")
        self.gridLayout_4.addWidget(self.manufacturer_field, 2, 3, 1, 2)
        self.offer_validity_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.offer_validity_label.setObjectName("offer_validity_label")
        self.gridLayout_4.addWidget(self.offer_validity_label, 2, 11, 1, 1)
        self.payment_term_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.payment_term_label.setObjectName("payment_term_label")
        self.gridLayout_4.addWidget(self.payment_term_label, 4, 1, 1, 1)
        self.request_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.request_field.sizePolicy().hasHeightForWidth())
        self.request_field.setSizePolicy(sizePolicy)
        self.request_field.setMinimumSize(QtCore.QSize(400, 0))
        self.request_field.setObjectName("request_field")
        self.gridLayout_4.addWidget(self.request_field, 3, 3, 1, 2)
        self.quote_currency_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.quote_currency_label.setObjectName("quote_currency_label")
        self.gridLayout_4.addWidget(self.quote_currency_label, 2, 9, 1, 1)
        self.quote_ref_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.quote_ref_field.setObjectName("quote_ref_field")
        self.gridLayout_4.addWidget(self.quote_ref_field, 4, 3, 1, 2)
        self.target_profit_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.target_profit_label.setObjectName("target_profit_label")
        self.gridLayout_4.addWidget(self.target_profit_label, 1, 11, 1, 1)
        self.quote_ref_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.quote_ref_label.setObjectName("quote_ref_label")
        self.gridLayout_4.addWidget(self.quote_ref_label, 5, 1, 1, 1)
        self.quotation_date_entry = QtWidgets.QDateEdit(self.quotation_form_groupBox)
        self.quotation_date_entry.setCalendarPopup(True)
        self.quotation_date_entry.setObjectName("quotation_date_entry")
        self.gridLayout_4.addWidget(self.quotation_date_entry, 1, 10, 1, 1)
        self.target_profit_percent_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.target_profit_percent_label.setObjectName("target_profit_percent_label")
        self.gridLayout_4.addWidget(self.target_profit_percent_label, 1, 13, 1, 1)
        self.target_profit_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.target_profit_field.setObjectName("target_profit_field")
        self.gridLayout_4.addWidget(self.target_profit_field, 1, 12, 1, 1)
        self.quotation_date_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.quotation_date_label.setObjectName("quotation_date_label")
        self.gridLayout_4.addWidget(self.quotation_date_label, 1, 9, 1, 1)
        self.payment_term_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.payment_term_field.setObjectName("payment_term_field")
        self.gridLayout_4.addWidget(self.payment_term_field, 5, 3, 1, 1)
        self.ref_number_generator_button = QtWidgets.QPushButton(self.quotation_form_groupBox)
        self.ref_number_generator_button.setObjectName("ref_number_generator_button")
        self.gridLayout_4.addWidget(self.ref_number_generator_button, 5, 4, 1, 1)
        self.gridLayout.addWidget(self.quotation_form_groupBox, 0, 0, 1, 1)
        self.vendors_and_items_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vendors_and_items_groupBox.sizePolicy().hasHeightForWidth())
        self.vendors_and_items_groupBox.setSizePolicy(sizePolicy)
        self.vendors_and_items_groupBox.setTitle("")
        self.vendors_and_items_groupBox.setObjectName("vendors_and_items_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.vendors_and_items_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.vendors_groupbox = QtWidgets.QGroupBox(self.vendors_and_items_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vendors_groupbox.sizePolicy().hasHeightForWidth())
        self.vendors_groupbox.setSizePolicy(sizePolicy)
        self.vendors_groupbox.setMaximumSize(QtCore.QSize(350, 16777215))
        self.vendors_groupbox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.vendors_groupbox.setObjectName("vendors_groupbox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.vendors_groupbox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vendor_add_window_button = QtWidgets.QPushButton(self.vendors_groupbox)
        self.vendor_add_window_button.setObjectName("vendor_add_window_button")
        self.gridLayout_3.addWidget(self.vendor_add_window_button, 0, 0, 1, 1)
        self.vendor_remove_button = QtWidgets.QPushButton(self.vendors_groupbox)
        self.vendor_remove_button.setObjectName("vendor_remove_button")
        self.gridLayout_3.addWidget(self.vendor_remove_button, 0, 1, 1, 1)
        self.vendor_list = QtWidgets.QListWidget(self.vendors_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vendor_list.sizePolicy().hasHeightForWidth())
        self.vendor_list.setSizePolicy(sizePolicy)
        self.vendor_list.setObjectName("vendor_list")
        item = QtWidgets.QListWidgetItem()
        self.vendor_list.addItem(item)
        self.gridLayout_3.addWidget(self.vendor_list, 1, 0, 1, 2)
        self.gridLayout_2.addWidget(self.vendors_groupbox, 7, 0, 3, 1)
        self.groupBox = QtWidgets.QGroupBox(self.vendors_and_items_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(770, 0))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_7.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_7.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.items_table = QtWidgets.QTableWidget(self.groupBox)
        self.items_table.setWordWrap(False)
        self.items_table.setObjectName("items_table")
        self.items_table.setColumnCount(7)
        self.items_table.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(6, item)
        self.gridLayout_7.addWidget(self.items_table, 2, 0, 4, 3)
        self.gridLayout_2.addWidget(self.groupBox, 7, 1, 3, 1)
        self.gridLayout.addWidget(self.vendors_and_items_groupBox, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1142, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuVendors = QtWidgets.QMenu(self.menubar)
        self.menuVendors.setObjectName("menuVendors")
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
        self.actionNew_Vendor = QtGui.QAction(MainWindow)
        self.actionNew_Vendor.setObjectName("actionNew_Vendor")
        self.actionAdd_Vendor_Spreadsheet = QtGui.QAction(MainWindow)
        self.actionAdd_Vendor_Spreadsheet.setObjectName("actionAdd_Vendor_Spreadsheet")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCurrency_Conversions)
        self.menuVendors.addAction(self.actionNew_Vendor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuVendors.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quotation_form_groupBox.setTitle(_translate("MainWindow", "Quotation Details"))
        self.total_markup_label.setText(_translate("MainWindow", "Total Markup"))
        self.current_quote_total_number_label.setText(_translate("MainWindow", "Total"))
        self.current_quote_total_label.setText(_translate("MainWindow", "Current Quote Total"))
        self.current_quote_total_currency_label.setText(_translate("MainWindow", "Currency"))
        self.total_markup_percent_label.setText(_translate("MainWindow", "%"))
        self.vat_label.setText(_translate("MainWindow", "VAT"))
        self.vat_state_combo.setItemText(0, _translate("MainWindow", "Included"))
        self.vat_state_combo.setItemText(1, _translate("MainWindow", "Not Included"))
        self.delivery_type_label.setText(_translate("MainWindow", "Delivery Type"))
        self.manufacturer_label.setText(_translate("MainWindow", "Manufacturer(s)"))
        self.export_to_excel_button.setText(_translate("MainWindow", "Export to Excel"))
        self.request_label.setText(_translate("MainWindow", "Request"))
        self.save_to_file_button.setText(_translate("MainWindow", "Save to File"))
        self.export_to_pdf_button.setText(_translate("MainWindow", "Export to PDF"))
        self.customer_label.setText(_translate("MainWindow", "Customer"))
        self.quote_currency_combo.setItemText(0, _translate("MainWindow", "EUR"))
        self.quote_currency_combo.setItemText(1, _translate("MainWindow", "USD"))
        self.quote_currency_combo.setItemText(2, _translate("MainWindow", "GBP"))
        self.quote_currency_combo.setItemText(3, _translate("MainWindow", "EGP"))
        self.quote_currency_combo.setItemText(4, _translate("MainWindow", "CHF"))
        self.quote_currency_combo.setItemText(5, _translate("MainWindow", "AED"))
        self.offer_validity_label.setText(_translate("MainWindow", "Validity (Months)"))
        self.payment_term_label.setText(_translate("MainWindow", "Payment Term"))
        self.quote_currency_label.setText(_translate("MainWindow", "Quote Currency"))
        self.target_profit_label.setText(_translate("MainWindow", "Target PO Profit"))
        self.quote_ref_label.setText(_translate("MainWindow", "Ref. No."))
        self.target_profit_percent_label.setText(_translate("MainWindow", "%"))
        self.quotation_date_label.setText(_translate("MainWindow", "Date"))
        self.ref_number_generator_button.setText(_translate("MainWindow", "Generate"))
        self.vendors_groupbox.setTitle(_translate("MainWindow", "Vendors"))
        self.vendor_add_window_button.setText(_translate("MainWindow", "Add"))
        self.vendor_remove_button.setText(_translate("MainWindow", "Remove"))
        __sortingEnabled = self.vendor_list.isSortingEnabled()
        self.vendor_list.setSortingEnabled(False)
        item = self.vendor_list.item(0)
        item.setText(_translate("MainWindow", "Universal Advanced Solutions"))
        self.vendor_list.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "Items"))
        self.pushButton_3.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove"))
        self.items_table.setSortingEnabled(False)
        item = self.items_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.items_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.items_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.items_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.items_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.items_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.items_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.items_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.items_table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.items_table.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.items_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.items_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.items_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Part number"))
        item = self.items_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Qty"))
        item = self.items_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Description"))
        item = self.items_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Unit Price"))
        item = self.items_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Total"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuVendors.setTitle(_translate("MainWindow", "Vendors"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCurrency_Conversions.setText(_translate("MainWindow", "Currency Conversions"))
        self.actionNew_Vendor.setText(_translate("MainWindow", "New Vendor"))
        self.actionAdd_Vendor_Spreadsheet.setText(_translate("MainWindow", "Add Vendor Spreadsheet"))
