import Days
import display
import validation
import random

# METHOD THAT GENERATES RETURN BILL WITH FINE IF IT IS CHANRGED
def generate_Return_bill(rented_item,  Cus_name , rentdays, return_days):
    price = 0
    price_with_fine = 0
    invoice_no = random.randint(1,200)
    with open (f"Return_Bill_{invoice_no}.txt", "w") as invoice:
        invoice.write("+"+"-"*78 +"+" +"\n")
        invoice.write("|    {:<0}{:<34}{:<0}".format(f" Name : {Cus_name}",""," Date : 2023-04-23 \t   | \n"))
        invoice.write("|"+"-"*78 +"|" +"\n")
        invoice.write("| {:<6}| {:<31}| {:<18}| {:<6}| {:<0} |\n".format("Id No", "Name","Brand", "Price", "Quatity"))
        for id, value in rented_item.items():
            data = [id,value["name"], value["brand"], value["price"], value["quantity"], value["total"]]
            invoice.write("|\t{:<4}| {:<31}| {:<18}| {:<6}| {:<7} |\n".format(data[0],data[1],data[2],data[3],data[4]))
            price += data[5]
        invoice.write("|"+"-"*78 +"|" +"\n")
        invoice.write("|    {:<5}{:<23}{:<0}".format(f"Rented for : {rentdays} days","",f"Returned after : {return_days} days\t\t   | \n"))
        if return_days > rentdays:
            extras = return_days - rentdays
            fine = extras * 10
            price_with_fine = price + fine
            pass
        invoice.write("|    {:<5}{:<24}{:<0}".format(f"Total Price : ${price}","",f"fine : ${price_with_fine}\t\t\t\t\t   | \n"))
        invoice.write("+"+"-"*78 +"+" +"\n")

# METHOD TO RETURN RENTED ITMES
def return_items():
    stocks = display.products_to_dictionary()
    Return = True
    Return_cart = {}
    print(
"""                                                                      +-------------------------------------+
                                                                       |  Welcome to Item Returning Process  |
                                                                       +-------------------------------------+"""
    )
    name = validation.askName()
    display.tableDisplay()

    while Return:
        no = validation.askItem_No()
        quantity = validation.aksQuantityReturn(no)
            
        if quantity <= stocks[no]['quantity']:
            
            rent_Days = Days.askRent_Days()
            return_days = Days.askReturn_Days()
            print(" ")
            
            price = int(stocks[no]['price'].replace("$",""))
            _price = price // 5
            total_price = _price * quantity
            
            stocks[no]['quantity'] = stocks[no]['quantity'] + quantity
            Return_cart[no] = {
                'name' :  stocks[no]['name'],
                'brand' : stocks[no]['brand'],
                'price' : stocks[no]['price'],
                'quantity': quantity,
                'total': total_price,
                'rentDays': rent_Days,
                'returnDays':return_days
            }
            print(f"{quantity} {stocks[no]['name']} sucessfully added to your cart")
            print(" ")
            Return = False
    
        while True:
            more = input("Do you have any more item left(y/n) >>\t").lower()
            print(" ")
            
            if more == 'y':
                Return = True
                break
            
            elif more == 'n':
                print("Item returned sucessfully and bill generated")
                print(" ")
                display.updateStocks(stocks)
                generate_Return_bill(Return_cart, name, rent_Days, return_days)
                break
            else:
                print("Invalid option, enter(y/n)")