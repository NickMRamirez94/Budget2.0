from item import item
from prettytable import PrettyTable

def menu():
    print
    print "--------------------Menu--------------------"
    print "0. Exit"
    print "1. Enter a new expenditure"
    print "2. Print all expenditures from this month"
    print "3. Use utility functions"
    print "4. Save"
    print "--------------------------------------------"
    choice = input("Enter your choice [0-4]:")
    print
    return choice

def welcome():
    print
    print "--------------------Welcome--------------------"
    print "Please enter the month you want to view or edit"
    print "-----------------------------------------------"
    month = raw_input("MONTH: ")
    return month

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

def save(month, itemList = []):
    file = open("BackupData/" + month + ".txt", "w")

    for i in range(len(itemList)):
        file.write("%s %s %s\n" % (itemList[i].name, itemList[i].price, itemList[i].date) )

    file.close()

def sortPrice(itemList = []):
    for i in range(len(itemList)):
        max = i
        for j in range(len(itemList)):
            if itemList[j].price < itemList[max].price:
                max = j

        itemList[i], itemList[max] = itemList[max], itemList[i]

    #translate itemList into a PrettyTable object
    tab = PrettyTable(['Name', 'Price', 'Purchase Date'])

    for i in range(len(itemList)):
        tab.add_row([itemList[i].name, itemList[i].price, itemList[i].date])

    print tab 


def extractMax(itemList = []):
    max = 0
    for i in range(len(itemList)):
        if itemList[i].price > itemList[max].price:
            max = i
    
    tab = PrettyTable(['Name', 'Price', 'Purchase Date'])
    tab.add_row([itemList[max].name, itemList[max].price, itemList[max].date])
    print tab

def extractMin(itemList = []):
    min = 0
    for i in range(len(itemList)):
        if itemList[i].price < itemList[min].price:
            min = i
    
    tab = PrettyTable(['Name', 'Price', 'Purchase Date'])
    tab.add_row([itemList[min].name, itemList[min].price, itemList[min].date])
    print tab

def utility(itemList = []):
    print
    print "--------------------Utility Menu--------------------"
    print "0. Sort by price"
    print "1. Extract max"
    print "2. Extract min"
    print "----------------------------------------------------"
    choice = input("Enter your choice [0-2]:")
    print   

    if choice == 0:
        sortPrice(itemList)
    elif choice == 1:
        extractMax(itemList)
    elif choice == 2:
        extractMin(itemList)
    else:
        print "\nSorry that is not a valid choice.\n"