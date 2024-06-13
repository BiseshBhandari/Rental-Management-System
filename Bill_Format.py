
with open("space_Sample.txt", "w") as file:
    file.write("+"+"-"*78 +"+" +"\n")
    file.write("|\t\t\t\t\t\t\tRentals Spot Rent Bill\t\t\t\t\t\t\t   | \n")
    file.write("|    {:<0}{:<34}{:<0}".format(" Name : Bisesh",""," Date : 2023-04-23 \t   | \n"))
    file.write("|"+"-"*78 +"|" +"\n")
    file.write("| {:<6}| {:<31}| {:<18}| {:<6}| {:<0} |\n".format("Id No", "Name","Brand", "Price", "Quatity"))
    file.write("|"+"-"*78 +"|" +"\n")
    file.write("|\t{:<4}| {:<31}| {:<18}| {:<6}| {:<7} |\n".format("1", "7.1 Surround Sound Speaker set", "JPanda Furnitures", "200","12"))
    file.write("|"+"-"*78 +"|" +"\n")
    file.write("|    {:<5}{:<23}{:<0}".format("Rented for : 12 days","","Returned after : 8 days\t\t   | \n"))
    file.write("|    {:<5}{:<24}{:<0}".format("Total Price : $1200","","fine : 30$\t\t\t\t\t   | \n"))
    file.write("|"+"-"*78 +"|" +"\n")
    file.write("| \t\t\t\t\tIf any delay is occured while returning of item\t\t\t   | \n|")
    file.write("\t\t\t\t\t\t\t     extra fine is charged \t\t\t\t\t\t   | \n")
    file.write("+"+"-"*78 +"+" +"\n")

