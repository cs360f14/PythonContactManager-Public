#!/usr/bin/python3

################################
# File Name:
# Author:
# Date:
# Class:
# Assignment:
# Purpose:
################################


# Include the ContactData.py file and import all of 
# that file's contents.
from ContactData import *


def displayMenu() :
    """ This function display the menu
    
    """
	print("-1. Quit")
	print(" 0. Display nicely to the screen all the entries")
	print(" 1. Search and show entries only in the given office location")
	print(" 2. Add an entry")
	print(" 3. Delete an entry")
	print(" 4. Search by First name (show all entries)")
	print(" 5. Search by email (show the first entry)")
   	## EXTRA PRACTICE ##
    print(" 6. Write the data to a file")



def main() :
    """ This is the main function
    
    The menu will be displayed, a character will be 
    read from the user and the appropriate function will
    be called to handle that menu item.
    
    If an invalid menu item is provided the menu is displayed
    again
    """
    
	displayMenu()
	choice = int(input(">>> "))
	
	if -1 == choice :
		return



# invoke main()
if __name__=="__main__" :
	main()
