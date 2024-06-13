import validation
import display
import random
import Days

def generate_Rent_bill(rented_item,  Cus_name, price):
    price = 0
    invoice_no = random.randint(1,200)
    with open (f"Rent_Bill_{invoice_no}.txt", "w") as invoice:
        invoice.write('-'*60)
        invoice.write(f"Customer Name: {Cus_name} \n")
        for id, value in rented_item.items():
            data = [id,value["name"], value["brand"], value["price"], value["quantity"], value["total"]]
            invoice.write(f"id: {data[0]} \t name: {data[1]} \t brand: {data[2]} \t price: {data[3]} \t quantity: {data[4]} \n")
            price += data[5]
        invoice.write(f"Total Price: {price}")


def rentItems():
    rented_cart = {}
    stocks = display.products_to_dictionary()
    rent = True
    print(
                                                                    """+-----------------------------------+
                                                                       |  Welcome to Item Renting Process  |
                                                                       +-----------------------------------+"""
    )
    name = validation.askName()
    display.tableDisplay()

    while rent:
        no = validation.askItem_No()
        quantity = validation.aksQuantity(no)
            
        if quantity <= stocks[no]['quantity']:
            
            rent_Days = Days.askRent_Days()
            print(" ")
            
            price = int(stocks[no]['price'].replace("$",""))
            _price = price // 5
            total_price = _price * quantity
            
            stocks[no]['quantity'] = stocks[no]['quantity'] - quantity
            rented_cart[no] = {
                'name' :  stocks[no]['name'],
                'brand' : stocks[no]['brand'],
                'price' : stocks[no]['price'],
                'quantity': quantity,
                'total': total_price
            }
            print(f"{quantity} {stocks[no]['name']} sucessfully added to your cart")
            print(" ")
            rent = False
    
        while True:
            more = input("Do you want to rent More(y/n) >>\t").lower()
            print(" ")
            
            if more == 'y':
                rent = True
                break
            
            elif more == 'n':
                print("Item rented sucessfully and bill generated")
                print(" ")
                display.updateStocks(stocks)
                generate_Rent_bill(rented_cart, name, total_price)
                break