from item import item
from prettytable import PrettyTable
from utilityfunctions import menu
from utilityfunctions import welcome
from utilityfunctions import addItem
from utilityfunctions import printList
from utilityfunctions import save
from utilityfunctions import utility

def main():

    month = welcome()

    choice = "-1"

    itemDB = []

    while choice != 0:

        choice = menu()

        if choice == 0:
            print "Bye!"
        elif choice == 1:
            addItem(itemDB)
        elif choice == 2:
            printList(itemDB)
        elif choice == 3:
            utility(itemDB)
        elif choice == 4:
            save(month, itemDB)
        else:
            print("\nSorry that is not a valid choice.\n")

main()