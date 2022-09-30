# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gebz/Documents/GitHub/QuotationCreator/QuoteCreatorQT/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1266, 739)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vendors_and_items_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vendors_and_items_groupBox.sizePolicy().hasHeightForWidth())
        self.vendors_and_items_groupBox.setSizePolicy(sizePolicy)
        self.vendors_and_items_groupBox.setObjectName("vendors_and_items_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.vendors_and_items_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.items_label = QtWidgets.QLabel(self.vendors_and_items_groupBox)
        self.items_label.setObjectName("items_label")
        self.gridLayout_2.addWidget(self.items_label, 9, 1, 1, 1)
        self.vendor_entry_form_groupBox = QtWidgets.QGroupBox(self.vendors_and_items_groupBox)
        self.vendor_entry_form_groupBox.setObjectName("vendor_entry_form_groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.vendor_entry_form_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vendor_name_field = QtWidgets.QLineEdit(self.vendor_entry_form_groupBox)
        self.vendor_name_field.setObjectName("vendor_name_field")
        self.gridLayout_3.addWidget(self.vendor_name_field, 0, 1, 1, 5)
        self.packing_cost_field = QtWidgets.QLineEdit(self.vendor_entry_form_groupBox)
        self.packing_cost_field.setObjectName("packing_cost_field")
        self.gridLayout_3.addWidget(self.packing_cost_field, 1, 1, 1, 1)
        self.target_profit_percent_label_2 = QtWidgets.QLabel(self.vendor_entry_form_groupBox)
        self.target_profit_percent_label_2.setObjectName("target_profit_percent_label_2")
        self.gridLayout_3.addWidget(self.target_profit_percent_label_2, 1, 11, 1, 1)
        self.vendor_comission_percent = QtWidgets.QLabel(self.vendor_entry_form_groupBox)
        self.vendor_comission_percent.setObjectName("vendor_comission_percent")
        self.gridLayout_3.addWidget(self.vendor_comission_percent, 0, 11, 1, 1)
        self.vendor_customs_label = QtWidgets.QLabel(self.vendor_entry_form_groupBox)
        self.vendor_customs_label.setObjectName("vendor_customs_label")
        self.gridLayout_3.addWidget(self.vendor_customs_label, 1, 6, 1, 1)
        self.vendor_shippingcost_label = QtWidgets.QLabel(self.vendor_entry_form_groupBox)
        self.vendor_shippingcost_label.setObjectName("vendor_shippingcost_label")
        self.gridLayout_3.addWidget(self.vendor_shippingcost_label, 1, 4, 1, 1)
        self.vendor_leadtime_label = QtWidgets.QLabel(self.vendor_entry_form_groupBox)
        self.vendor_leadtime_label.setObjectName("vendor_leadtime_label")
        self.gridLayout_3.addWidget(self.vendor_leadtime_label, 3, 0, 1, 1)
        self.target_profit_label_2 = QtWidgets.QLabel(self.vendor_entry_form_groupBox)
        self.target_profit_label_2.setObjectName("target_profit_label_2")
        self.gridLayout_3.addWidget(self.target_profit_label_2, 0, 6, 1, 1)
        self.vendor_add_button = QtWidgets.QToolButton(self.vendor_entry_form_groupBox)
        self.vendor_add_button.setObjectName("vendor_add_button")
        self.gridLayout_3.addWidget(self.vendor_add_button, 3, 9, 1, 2)
        self.vendor_currency_label = QtWidgets.QLabel(self.vendor_entry_form_groupBox)
        self.vendor_currency_label.setObjectName("vendor_currency_label")
        self.gridLayout_3.addWidget(self.vendor_currency_label, 3, 4, 1, 1)
        self.vendor_currency_combo = QtWidgets.QComboBox(self.vendor_entry_form_groupBox)
        self.vendor_currency_combo.setObjectName("vendor_currency_combo")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.vendor_currency_combo.addItem("")
        self.gridLayout_3.addWidget(self.vendor_currency_combo, 3, 5, 1, 1)
        self.customs_percent_field = QtWidgets.QLineEdit(self.vendor_entry_form_groupBox)
        self.customs_percent_field.setObjectName("customs_percent_field")
        self.gridLayout_3.addWidget(self.customs_percent_field, 1, 9, 1, 1)
        self.vendor_name_label = QtWidgets.QLabel(self.vendor_entry_form_groupBox)
        self.vendor_name_label.setObjectName("vendor_name_label")
        self.gridLayout_3.addWidget(self.vendor_name_label, 0, 0, 1, 1)
        self.vendor_comission_field = QtWidgets.QLineEdit(self.vendor_entry_form_groupBox)
        self.vendor_comission_field.setText("")
        self.vendor_comission_field.setObjectName("vendor_comission_field")
        self.gridLayout_3.addWidget(self.vendor_comission_field, 0, 9, 1, 1)
        self.shipping_cost_field = QtWidgets.QLineEdit(self.vendor_entry_form_groupBox)
        self.shipping_cost_field.setText("")
        self.shipping_cost_field.setObjectName("shipping_cost_field")
        self.gridLayout_3.addWidget(self.shipping_cost_field, 1, 5, 1, 1)
        self.vendor_packingcost_label = QtWidgets.QLabel(self.vendor_entry_form_groupBox)
        self.vendor_packingcost_label.setObjectName("vendor_packingcost_label")
        self.gridLayout_3.addWidget(self.vendor_packingcost_label, 1, 0, 1, 1)
        self.vendor_lead_time_field = QtWidgets.QLineEdit(self.vendor_entry_form_groupBox)
        self.vendor_lead_time_field.setObjectName("vendor_lead_time_field")
        self.gridLayout_3.addWidget(self.vendor_lead_time_field, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.vendor_entry_form_groupBox, 7, 1, 2, 13)
        self.vendors_groupbox = QtWidgets.QGroupBox(self.vendors_and_items_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vendors_groupbox.sizePolicy().hasHeightForWidth())
        self.vendors_groupbox.setSizePolicy(sizePolicy)
        self.vendors_groupbox.setTitle("")
        self.vendors_groupbox.setObjectName("vendors_groupbox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.vendors_groupbox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.vendors_label = QtWidgets.QLabel(self.vendors_groupbox)
        self.vendors_label.setObjectName("vendors_label")
        self.gridLayout_5.addWidget(self.vendors_label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.vendors_groupbox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 0, 2, 1, 1)
        self.edit_selected_vendor_button = QtWidgets.QPushButton(self.vendors_groupbox)
        self.edit_selected_vendor_button.setObjectName("edit_selected_vendor_button")
        self.gridLayout_5.addWidget(self.edit_selected_vendor_button, 0, 3, 1, 1)
        self.vendor_list = QtWidgets.QListWidget(self.vendors_groupbox)
        self.vendor_list.setObjectName("vendor_list")
        item = QtWidgets.QListWidgetItem()
        self.vendor_list.addItem(item)
        self.gridLayout_5.addWidget(self.vendor_list, 1, 0, 1, 5)
        self.remove_selected_vendor_button = QtWidgets.QToolButton(self.vendors_groupbox)
        self.remove_selected_vendor_button.setObjectName("remove_selected_vendor_button")
        self.gridLayout_5.addWidget(self.remove_selected_vendor_button, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.vendors_groupbox, 7, 0, 4, 1)
        self.items_table = QtWidgets.QTableWidget(self.vendors_and_items_groupBox)
        self.items_table.setWordWrap(False)
        self.items_table.setObjectName("items_table")
        self.items_table.setColumnCount(8)
        self.items_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(0, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(7, item)
        self.gridLayout_2.addWidget(self.items_table, 10, 1, 1, 14)
        self.gridLayout.addWidget(self.vendors_and_items_groupBox, 1, 0, 1, 1)
        self.quotation_form_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.quotation_form_groupBox.setObjectName("quotation_form_groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.quotation_form_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.request_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.request_label.setObjectName("request_label")
        self.gridLayout_4.addWidget(self.request_label, 3, 1, 1, 1)
        self.customer_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.customer_label.setObjectName("customer_label")
        self.gridLayout_4.addWidget(self.customer_label, 1, 1, 1, 1)
        self.customer_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_field.sizePolicy().hasHeightForWidth())
        self.customer_field.setSizePolicy(sizePolicy)
        self.customer_field.setMinimumSize(QtCore.QSize(400, 0))
        self.customer_field.setObjectName("customer_field")
        self.gridLayout_4.addWidget(self.customer_field, 1, 3, 1, 2)
        self.export_to_excel_button = QtWidgets.QPushButton(self.quotation_form_groupBox)
        self.export_to_excel_button.setObjectName("export_to_excel_button")
        self.gridLayout_4.addWidget(self.export_to_excel_button, 2, 14, 1, 1)
        self.offer_validity_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.offer_validity_label.setObjectName("offer_validity_label")
        self.gridLayout_4.addWidget(self.offer_validity_label, 2, 11, 1, 1)
        self.vat_state_combo = QtWidgets.QComboBox(self.quotation_form_groupBox)
        self.vat_state_combo.setObjectName("vat_state_combo")
        self.vat_state_combo.addItem("")
        self.vat_state_combo.addItem("")
        self.gridLayout_4.addWidget(self.vat_state_combo, 3, 10, 1, 1)
        self.delivery_type_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.delivery_type_label.setObjectName("delivery_type_label")
        self.gridLayout_4.addWidget(self.delivery_type_label, 3, 11, 1, 1)
        self.target_profit_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.target_profit_label.setObjectName("target_profit_label")
        self.gridLayout_4.addWidget(self.target_profit_label, 1, 11, 1, 1)
        self.request_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.request_field.sizePolicy().hasHeightForWidth())
        self.request_field.setSizePolicy(sizePolicy)
        self.request_field.setMinimumSize(QtCore.QSize(400, 0))
        self.request_field.setObjectName("request_field")
        self.gridLayout_4.addWidget(self.request_field, 3, 3, 1, 2)
        self.vat_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.vat_label.setObjectName("vat_label")
        self.gridLayout_4.addWidget(self.vat_label, 3, 9, 1, 1)
        self.save_to_file_button = QtWidgets.QPushButton(self.quotation_form_groupBox)
        self.save_to_file_button.setObjectName("save_to_file_button")
        self.gridLayout_4.addWidget(self.save_to_file_button, 1, 14, 1, 1)
        self.export_to_pdf_button = QtWidgets.QPushButton(self.quotation_form_groupBox)
        self.export_to_pdf_button.setObjectName("export_to_pdf_button")
        self.gridLayout_4.addWidget(self.export_to_pdf_button, 3, 14, 1, 1)
        self.delivery_type_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.delivery_type_field.setObjectName("delivery_type_field")
        self.gridLayout_4.addWidget(self.delivery_type_field, 3, 12, 1, 1)
        self.offer_validity_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.offer_validity_field.setObjectName("offer_validity_field")
        self.gridLayout_4.addWidget(self.offer_validity_field, 2, 12, 1, 1)
        self.manufacturer_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.manufacturer_label.setObjectName("manufacturer_label")
        self.gridLayout_4.addWidget(self.manufacturer_label, 2, 1, 1, 1)
        self.target_profit_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.target_profit_field.setObjectName("target_profit_field")
        self.gridLayout_4.addWidget(self.target_profit_field, 1, 12, 1, 1)
        self.target_profit_percent_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.target_profit_percent_label.setObjectName("target_profit_percent_label")
        self.gridLayout_4.addWidget(self.target_profit_percent_label, 1, 13, 1, 1)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_field.sizePolicy().hasHeightForWidth())
        self.manufacturer_field.setSizePolicy(sizePolicy)
        self.manufacturer_field.setMinimumSize(QtCore.QSize(400, 0))
        self.manufacturer_field.setObjectName("manufacturer_field")
        self.gridLayout_4.addWidget(self.manufacturer_field, 2, 3, 1, 2)
        self.quote_currency_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.quote_currency_label.setObjectName("quote_currency_label")
        self.gridLayout_4.addWidget(self.quote_currency_label, 2, 9, 1, 1)
        self.payment_term_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.payment_term_label.setObjectName("payment_term_label")
        self.gridLayout_4.addWidget(self.payment_term_label, 4, 1, 1, 1)
        self.quote_ref_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.quote_ref_label.setObjectName("quote_ref_label")
        self.gridLayout_4.addWidget(self.quote_ref_label, 5, 1, 1, 1)
        self.payment_term_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.payment_term_field.setObjectName("payment_term_field")
        self.gridLayout_4.addWidget(self.payment_term_field, 5, 3, 1, 1)
        self.ref_number_generator_button = QtWidgets.QPushButton(self.quotation_form_groupBox)
        self.ref_number_generator_button.setObjectName("ref_number_generator_button")
        self.gridLayout_4.addWidget(self.ref_number_generator_button, 5, 4, 1, 1)
        self.quote_ref_field = QtWidgets.QLineEdit(self.quotation_form_groupBox)
        self.quote_ref_field.setObjectName("quote_ref_field")
        self.gridLayout_4.addWidget(self.quote_ref_field, 4, 3, 1, 2)
        self.quotation_date_label = QtWidgets.QLabel(self.quotation_form_groupBox)
        self.quotation_date_label.setObjectName("quotation_date_label")
        self.gridLayout_4.addWidget(self.quotation_date_label, 1, 9, 1, 1)
        self.quotation_date_entry = QtWidgets.QDateEdit(self.quotation_form_groupBox)
        self.quotation_date_entry.setObjectName("quotation_date_entry")
        self.gridLayout_4.addWidget(self.quotation_date_entry, 1, 10, 1, 1)
        self.current_totals_frame = QtWidgets.QFrame(self.quotation_form_groupBox)
        self.current_totals_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.current_totals_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.current_totals_frame.setObjectName("current_totals_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.current_totals_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.current_quote_total_label = QtWidgets.QLabel(self.current_totals_frame)
        self.current_quote_total_label.setObjectName("current_quote_total_label")
        self.gridLayout_6.addWidget(self.current_quote_total_label, 0, 0, 1, 1)
        self.current_quote_total_number_label = QtWidgets.QLabel(self.current_totals_frame)
        self.current_quote_total_number_label.setObjectName("current_quote_total_number_label")
        self.gridLayout_6.addWidget(self.current_quote_total_number_label, 0, 1, 1, 1)
        self.current_quote_total_currency_label = QtWidgets.QLabel(self.current_totals_frame)
        self.current_quote_total_currency_label.setObjectName("current_quote_total_currency_label")
        self.gridLayout_6.addWidget(self.current_quote_total_currency_label, 0, 2, 1, 1)
        self.total_markup_label = QtWidgets.QLabel(self.current_totals_frame)
        self.total_markup_label.setObjectName("total_markup_label")
        self.gridLayout_6.addWidget(self.total_markup_label, 1, 0, 1, 1)
        self.total_markup_number_label = QtWidgets.QLabel(self.current_totals_frame)
        self.total_markup_number_label.setObjectName("total_markup_number_label")
        self.gridLayout_6.addWidget(self.total_markup_number_label, 1, 1, 1, 1)
        self.total_markup_percent_label = QtWidgets.QLabel(self.current_totals_frame)
        self.total_markup_percent_label.setObjectName("total_markup_percent_label")
        self.gridLayout_6.addWidget(self.total_markup_percent_label, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.current_totals_frame, 4, 9, 2, 6)
        self.gridLayout.addWidget(self.quotation_form_groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1266, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCurrency_Conversions = QtWidgets.QAction(MainWindow)
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
        self.items_label.setText(_translate("MainWindow", "Items"))
        self.vendor_entry_form_groupBox.setTitle(_translate("MainWindow", "       Vendor Details"))
        self.target_profit_percent_label_2.setText(_translate("MainWindow", "%"))
        self.vendor_comission_percent.setText(_translate("MainWindow", "%"))
        self.vendor_customs_label.setText(_translate("MainWindow", "Customs"))
        self.vendor_shippingcost_label.setText(_translate("MainWindow", "Shipping Cost"))
        self.vendor_leadtime_label.setText(_translate("MainWindow", "Vendor Lead Time (Weeks):"))
        self.target_profit_label_2.setText(_translate("MainWindow", "Vendor Commission:"))
        self.vendor_add_button.setText(_translate("MainWindow", "Add Vendor"))
        self.vendor_currency_label.setText(_translate("MainWindow", "Vendor Currency:"))
        self.vendor_currency_combo.setItemText(0, _translate("MainWindow", "EUR"))
        self.vendor_currency_combo.setItemText(1, _translate("MainWindow", "USD"))
        self.vendor_currency_combo.setItemText(2, _translate("MainWindow", "GBP"))
        self.vendor_currency_combo.setItemText(3, _translate("MainWindow", "EGP"))
        self.vendor_currency_combo.setItemText(4, _translate("MainWindow", "CHF"))
        self.vendor_currency_combo.setItemText(5, _translate("MainWindow", "AED"))
        self.vendor_name_label.setText(_translate("MainWindow", "Vendor Name:"))
        self.vendor_packingcost_label.setText(_translate("MainWindow", "Packing & Legalization Cost:"))
        self.vendors_label.setText(_translate("MainWindow", "Vendors"))
        self.pushButton.setText(_translate("MainWindow", "Add Item"))
        self.edit_selected_vendor_button.setText(_translate("MainWindow", "edit"))
        __sortingEnabled = self.vendor_list.isSortingEnabled()
        self.vendor_list.setSortingEnabled(False)
        item = self.vendor_list.item(0)
        item.setText(_translate("MainWindow", "Rohde & Schwarz"))
        self.vendor_list.setSortingEnabled(__sortingEnabled)
        self.remove_selected_vendor_button.setText(_translate("MainWindow", "remove"))
        self.items_table.setSortingEnabled(False)
        item = self.items_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.items_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.items_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.items_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.items_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Part number"))
        item = self.items_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Qty"))
        item = self.items_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        item = self.items_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Unit Price"))
        item = self.items_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Total Price"))
        self.quotation_form_groupBox.setTitle(_translate("MainWindow", "Quotation Details"))
        self.request_label.setText(_translate("MainWindow", "Request"))
        self.customer_label.setText(_translate("MainWindow", "Customer"))
        self.export_to_excel_button.setText(_translate("MainWindow", "Export to Excel"))
        self.offer_validity_label.setText(_translate("MainWindow", "Offer Vailidity (Months)"))
        self.vat_state_combo.setItemText(0, _translate("MainWindow", "Included"))
        self.vat_state_combo.setItemText(1, _translate("MainWindow", "Not Included"))
        self.delivery_type_label.setText(_translate("MainWindow", "Delivery Type"))
        self.target_profit_label.setText(_translate("MainWindow", "Target PO Profit"))
        self.vat_label.setText(_translate("MainWindow", "VAT"))
        self.save_to_file_button.setText(_translate("MainWindow", "Save to File"))
        self.export_to_pdf_button.setText(_translate("MainWindow", "Export to PDF"))
        self.manufacturer_label.setText(_translate("MainWindow", "Manufacturer(s)"))
        self.target_profit_percent_label.setText(_translate("MainWindow", "%"))
        self.quote_currency_combo.setItemText(0, _translate("MainWindow", "EUR"))
        self.quote_currency_combo.setItemText(1, _translate("MainWindow", "USD"))
        self.quote_currency_combo.setItemText(2, _translate("MainWindow", "GBP"))
        self.quote_currency_combo.setItemText(3, _translate("MainWindow", "EGP"))
        self.quote_currency_combo.setItemText(4, _translate("MainWindow", "CHF"))
        self.quote_currency_combo.setItemText(5, _translate("MainWindow", "AED"))
        self.quote_currency_label.setText(_translate("MainWindow", "Quote Currency"))
        self.payment_term_label.setText(_translate("MainWindow", "Payment Term"))
        self.quote_ref_label.setText(_translate("MainWindow", "Ref. No."))
        self.ref_number_generator_button.setText(_translate("MainWindow", "Generate"))
        self.quotation_date_label.setText(_translate("MainWindow", "Date"))
        self.current_quote_total_label.setText(_translate("MainWindow", "Current Quote Total"))
        self.current_quote_total_number_label.setText(_translate("MainWindow", "Total"))
        self.current_quote_total_currency_label.setText(_translate("MainWindow", "Currency"))
        self.total_markup_label.setText(_translate("MainWindow", "Total Markup"))
        self.total_markup_number_label.setText(_translate("MainWindow", "Markup"))
        self.total_markup_percent_label.setText(_translate("MainWindow", "%"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCurrency_Conversions.setText(_translate("MainWindow", "Currency Conversions"))
