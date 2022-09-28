import openpyxl
import math

#_______________________________________________________________________________
#----------------Class for the vendors------------------------------------------
#_______________________________________________________________________________

class Vendor():
    def __init__(self, vendor_currency, shipping_cost, packaging_cost, clearing_cost,
                 vendor_comission, vendor_leadtime):
        pass
    
class VendorItem(Vendor):
    def __init__(self, vendor_currency, shipping_cost, packaging_cost, 
                 clearing_cost, vendor_comission, vendor_leadtime, item_cost, 
                 item_type, item_description, item_quantity, item_part_number):
        super().__init__(vendor_currency, shipping_cost, packaging_cost, 
                         clearing_cost, vendor_comission, vendor_leadtime)