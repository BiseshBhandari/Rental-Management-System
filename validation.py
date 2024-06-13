from display import products_to_dictionary

def askName():
    while True:
        name = input("What is your name? >>\t").strip()  
        if name.isalpha() and len(name) >3:
            return name
            break
        elif name.isdigit():
            print("Name must be in characters")
            continue    
        elif len(name) <3:
            print("Name is too short")
            continue
    
def askItem_No():
    stocks = products_to_dictionary()
    while True:
        try:     
            No = int(input("Item id: >> \t"))
        except:
            print("Invalid id, (enter a number)")
            continue
        if No in stocks.keys():  
            return No
            break
        elif No <= 0:
            print("Option value should be positive !!")
            continue
        else:
            print("Sorry Item_No not available !!")
            continue

def aksQuantity(item_no):
    stocks = products_to_dictionary()
    while True:
        try:
            quantity = int(input("quantity >>\t"))
        except:
            print(
                '''┌───────────────────────────────────────────────────────────────┐
|                    Invalid quantity error                     |
├───────────────────────────────────────────────────────────────┤
|            Sorry the quatity must be in numbers               |
└───────────────────────────────────────────────────────────────┘
                '''
            )
            continue
        if quantity <=0:
            print("Sorry enter a positive value")
            continue
        elif quantity > stocks[item_no]['quantity']:
            print('Sorry Quantity out of stocks')
            continue
        else:
            return quantity
            break
        
def aksQuantityReturn(item_no):
    stocks = products_to_dictionary()
    while True:
        try:
            quantity = int(input("quantity >>\t"))
        except:
            print(
                '''┌───────────────────────────────────────────────────────────────┐
|                    Invalid quantity error                     |
├───────────────────────────────────────────────────────────────┤
|            Sorry the quatity must be in numbers               |
└───────────────────────────────────────────────────────────────┘
                '''
            )
            continue
        if quantity <=0:
            print("Sorry enter a positive value")
            continue
        else:
            return quantity
            break
