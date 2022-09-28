import tkinter as tk


item_list = {
    "banana":20,
    "apple":50,
    "pear":40,
    "soda":6,
    "ramen":4,
    "orange":15,
    "beef":200,
    "chicken":80
}

def create_quote_excel(item_name, item_quantity):
    return


root=tk.Tk()

item_name = tk.StringVar()
item_quantity = tk.IntVar()

item_name_prompt=tk.Label(text="Product Name:")
item_name_prompt.grid(row=1,column=1)

item_name_box = tk.Entry(textvariable=item_name)
item_name_box.grid(row=1,column=2)

item_quantity_prompt=tk.Label(text="Quantity:")
item_quantity_prompt.grid(row=2,column=1)

item_quantity_box = tk.Entry(textvariable=item_quantity)
item_quantity_box.grid(row=2,column=2)
error_box = tk.Label()
error_box.grid(row=4)

def create_quote():
    if bool(item_name.get() in item_list)==False:
        
        error_box.config(text="error, invalid item")
    elif bool(item_name.get() in item_list)== True:
        
        error_box.config(text="quote created")

create_quote_button = tk.Button(text="Create Quote",command=create_quote)
create_quote_button.grid(row=3, column=2)


root.mainloop()

