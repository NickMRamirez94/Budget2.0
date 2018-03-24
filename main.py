from item import item
from prettytable import PrettyTable

def menu():
    print
    print "--------------------Menu--------------------"
    print "0. Exit"
    print "1. Enter a new expenditure"
    print "2. Print all expenditures from this month"
    print "--------------------------------------------"
    choice = input("Enter your choice [0-3]:")
    print
    return choice

def addItem(itemList = []):

    #get item information from user
    name = raw_input("Please enter the name of the item: ")
    print
    price = eval(raw_input("Please enter the price of the item: "))
    print
    date = raw_input("Please enter date of the item\n**FORMAT M/D/Y**: ")

    #add item to the list
    itemList.append(item(price, name, date))

def printList(itemList = []):

    #translate itemList into a PrettyTable object
    tab = PrettyTable(['Name', 'Price', 'Purchase Date'])

    for i in range(len(itemList)):
        tab.add_row([itemList[i].name, itemList[i].price, itemList[i].date])

    print tab

def main():

    choice = "-1"

    itemDB = []

    book = item(20, "The Stand", "3/20/18")

    while choice != 0:

        choice = menu()

        if choice == 0:
            print "Bye!"
        elif choice == 1:
            addItem(itemDB)
        elif choice == 2:
            printList(itemDB)
        else:
            print("\nSorry that is not a valid choice.\n")

main()