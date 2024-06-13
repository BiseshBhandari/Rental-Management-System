def askRent_Days():
    while True:
        try:
            rent_days = int(input("For How many Days yo want to Rent >>: \t"))
        
        except:
            print("Invalid Days, required numbers")
        
        if rent_days<= 0:
            print("Sorry enter a positive value for days")
            continue
        else:
            return rent_days
            break

def askReturn_Days():
    while True:
        try:
            return_Days = int(input("After How many days did you return the item >>: \t"))
        
        except:
            print("Invalid value, the value should in numbers")
        
        if return_Days <= 0:
            print("Sorry enter a positive value")
            continue
        else:
            return return_Days
            break