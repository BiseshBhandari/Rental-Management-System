from tabulate import tabulate

# METHOD TO INSERT  THE TEXT FILE IN THE DICTIONARY
def products_to_dictionary():
    index = 1
    products= {}

    with open("stocks.txt", "r") as f:
        for line in f:
            items = line.strip().split(",")

            products [index] = {
                "name": items[0],
                "brand": items[1],
                "price": items[2],
                "quantity": int(items[3])
            }
            index = index + 1
    return products

# METHOD TO DISPLAY A TABLE OF AVAILABLE ITEMS
def tableDisplay():
    products = products_to_dictionary()
    head = ["Index no","Items", "Brand", "Price", "Quantity"]
    data2 = []
    for index , iteme in products.items():
        data = [index,iteme["name"], iteme["brand"], iteme["price"], iteme["quantity"]]
        data2.append(data)

    table = tabulate(data2, headers=head, tablefmt='fancy_grid')
    print(table)  


# METHOD TO UPDATE THE DICTIONARY
def updateStocks(itemsStock):
    with open("stocks.txt", "w") as f:
        for index, item in itemsStock.items():
            if item['quantity'] <= 0:
                pass
            
            else:
                f.write(f"{item['name']},{item['brand']},{item['price']},{item['quantity']} \n")

