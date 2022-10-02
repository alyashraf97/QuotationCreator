





#INTO THE BOWELS OF HELL

'''

vendors =[]
    allQuoteData={}




def get_quote_data(self):
        customer=self.customer_field.text()
        manufacturers=self.manufacturer_field.text()
        request=self.request_field.text()
        paymentTerm=self.payment_term_field.text
        refNo=self.quote_ref_field.text()
        quoteDate=self.quotation_date_entry.text()
        quoteCurrency=self.quote_currency_combo.currentText()
        vatStatus=self.vat_state_combo.currentText()
        targetProfit=float(self.target_profit_field.text())
        offerValidity=int(self.offer_validity_field.text())
        deliveryType=self.delivery_type_field.text()
        
        quoteData = {
            "customer":customer,
            "manufacturers":manufacturers,
            "request":request,
            "paymentTerm":paymentTerm,
            "refNo":refNo,
            "quoteDate":quoteDate,
            "quoteCurrency":quoteCurrency,
            "vatStatus":vatStatus,
            "targetProfit":targetProfit,
            "offerValidity":offerValidity,
            "deliveryType":deliveryType            
        }
        return quoteData
    
    
    def get_vendor_data(self):
        vendorName=self.vendor_name_field.text()        
        vendorComission=float(self.vendor_comission_field.text())
        vendorPackingCost=float(self.packing_cost_field.text())
        vendorShippingCost=float(self.shipping_cost_field.text())
        vendorCustoms=float(self.vendor_comission_field.text())
        vendorCurrency=self.vendor_currency_combo.currentText()
        vendorLeadTime=int(self.vendor_lead_time_field.text())
        
        vendorData={
                "vendorName":vendorName,
                'vendorComission':vendorComission,
                'vendorPackingCost':vendorPackingCost,
                'vendorShippingCost':vendorShippingCost,
                'vendorCustoms':vendorCustoms,
                'vendorCurrency':vendorCurrency,
                'vendorLeadTime':vendorLeadTime,
                }
        return vendorData
        
        
    def refreshVendorlist(self):
        self.vendor_list.clear()

        for vendor in self.vendors:
            self.vendor_list.addItem(vendor.vendorName)    
        
    def addNewVendor(self):
        self.vendors.append(Vendor(self.get_vendor_data()))
        self.vendor_list.addItem("New Vendor")


    def add_item(self):
        pass
    
    def generate_excel(self):
        pass
    
    def generate_pdf(self):
        pass
    
    def save_file(self):
        allQuoteData={}
        return

class Quote:
    def __init__(self, listing_of_all_vendors,qouteData = None):
        self.listing_of_all_vendors=listing_of_all_vendors
        if(qouteData != None):
            self.customer = qouteData["customer"]
            self.manufacturers = qouteData["manufacturers"]
            self.request = qouteData["request"]
            self.paymentTerm = qouteData["paymentTerm"]
            self.refNo = qouteData["refNo"]
            self.quoteDate = qouteData["quoteDate"]
            self.quoteCurrency = qouteData["quoteCurrency"]
            self.vatStatus = qouteData["vatStatus"]
            self.targetProfit = qouteData["targetProfit"]
            self.offerValidity = qouteData["offerValidity"]
            self.deliveryType = qouteData["deliveryType"]
        

    #def __init__(self,listing_of_all_vendors):
        #self.listing_of_all_vendors=listing_of_all_vendors
        #self.final_prices=self.calculate_final_price

        
    def seperate_vendor(self,vendor_name):
        vendor_list_of_unit_prices=self.listing_of_all_vendors[f'{vendor_name}']

        return vendor_list_of_unit_prices


    def get_item_weights(self,list_of_all_item_unit_prices):
        #Returns item weights (vendor by vendor basis)
        #Takes a list of item prices (before markup) and returns a list of weights
        item_weights=[]
        total_sum=sum(list_of_all_item_unit_prices)
        for i in range(len(list_of_all_item_unit_prices)):
            item_weights[i]=list_of_all_item_unit_prices[i]/total_sum
        return item_weights

    def final_vendor_prices(self,list_of_vendor_unit_prices,list_of_vendor_qty, 
                            vendor_packing, vendor_shipping, vendor_customs, 
                            vendor_comission):
        vendor_price_listing={}
        vendor_sum=int()
        list_of_item_total_prices=[]

        #generating a sum of item total prices & a list of item total prices
        for i in range(len(list_of_vendor_unit_prices)):
            vendor_sum+=list_of_vendor_unit_prices[i]*list_of_vendor_qty[i]
            list_of_item_total_prices[i]=(list_of_vendor_unit_prices[i]*(1-vendor_comission))*list_of_vendor_qty[i]

        vendor_final_total=vendor_sum+vendor_customs+vendor_packing+vendor_shipping
        item_weights=self.get_item_weights(list_of_vendor_unit_prices)
        vendor_final_price_list=[vendor_final_total*item_weights[i] for i in range(len(list_of_vendor_unit_prices))]

        vendor_price_listing={
            "totalPrice": vendor_final_total,
            "list_of_vendor_total_prices":vendor_final_price_list
        }    
        
        return vendor_price_listing
        

    def calculate_final_price(self, list_of_vendor_total_prices, target_profit,
                            sales_tax, vat_state):
        cumulative_sum=sum(list_of_vendor_total_prices)
        #for i in range(len(list_of_item_prices)):
            #cumulative_sum+=list_of_item_prices[i]*list_of_item_qty[i]
        
        #final_price=((cumulative_sum/(1-target_profit))*(1+sales_tax))
        if vat_state==True:
            return ((cumulative_sum/(1-target_profit))*(1+sales_tax))
        else:
            return ((cumulative_sum/(1-target_profit))*(1+sales_tax))*1.14

class Vendor:
    def __init__(self,vendorData = None):
        if(vendorData != None):
            self.vendorName = vendorData["vendorName"]
            self.vendorComission = vendorData["vendorComission"]
            self.vendorPackingCost = vendorData["vendorPackingCost"]
            self.vendorShippingCost = vendorData["vendorShippingCost"]
            self.vendorCustoms = vendorData["vendorCustoms"]
            self.vendorCurrency = vendorData["vendorCurrency"]
            self.vendorLeadTime = vendorData["vendorLeadTime"]

        
'''