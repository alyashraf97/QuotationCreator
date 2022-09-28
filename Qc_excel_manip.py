import openpyxl as xl
import openpyxl_templates
import Qc_data_manip

#_______________________________________________________________________________
#----------------Main Class for the Base Excel Sheet Design---------------------
#_______________________________________________________________________________

class BaseExcellTemplate():
    def __init__(self, categories, sub_categories, currency_conversions):
        self.currency_conversions={}
        pass

#_______________________________________________________________________________
#----------------Class for the Quotation Excel Sheet----------------------------
#_______________________________________________________________________________    
    
class QuotationSheet(BaseExcellTemplate):
    def __init__(self, master, categories, sub_categories, currency_conversions,
                 organization, project, number_of_vendors, vendor_list,
                 quote_currency, vat_status, delivery_term, current_date,
                 reference_code, target_gross_profit, payment_term, validity,
                 currency_risk_factor):
        super().__init__(master, categories, sub_categories, currency_conversions)