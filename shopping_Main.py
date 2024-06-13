import display
import  rent 
import Return

def main_Shopping():
    print('Select the folloing options')
    print('Select 1 To display the items')
    print('Select 2 To start renting process')
    print('Select 3 To start returning process')
    print('Select 4 To exit the program')

    while True:
        try:
            option = int(input("your choice >> \t"))
        except:
            print("Value error, choice must be in number")
            continue
        
        if option == 1:
            display.tableDisplay()
        
        elif option == 2:
            rent.rentItems()
        
        elif option == 3:
            Return.return_items()
        
        elif option == 4:
            print("Thank you for visiting.")
            break
        
        else:
            print("Sorry option not available")

main_Shopping()