# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# ZShen,08.30.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ZShen,08.30.2020, add code in class product
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    # TODO: Add Code to the Product class
    product_name = ''
    product_price = ''

    def __init__(self, product_name: str, product_price: float):

        self.__product_name = str(product_name)
        self.__product_price = float(product_price)


    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        if str(value).isnmeric() == False:
            self.__product_name = value
        else:
            raise Exception('Name cannot be numbers')

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if float(value).isnmeric() == True:
            self.__product_price = value
        else:
            raise Exception('Please enter numbers only')

    def __str__(self):
        return self.product_name + ',' + str(self.product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ZShen,08.30.2020, add code to complete class Fileprocessor
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):

        file = open(file_name, 'r')
        for line in file:
            product, price = line.split(",")
            row = product, price
            lstOfProductObjects.append(row)
        file.close()
        return lstOfProductObjects, 'Success'

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, lstOfProductObjects):

        file = open(file_name, 'w')
        for row in lstOfProductObjects:
            file.write(row[0].strip() + ',' + row[1].strip() + '\n')
        file.close()

        return lstOfProductObjects, 'Success'


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    @staticmethod
    def __doc__():
        return 'Product and Price list'
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_Tasks():
        print('''
            Menu of Options
            1) Show current data
            2) Add a new Task 
            3) Save Data to File         
            ''')
        print()

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()
        return choice
    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_Tasks_in_list(lstOfProductObjects):
        print("******* The current Tasks ToDo are: *******")
        for row in lstOfProductObjects:
            print(row[0].strip() + " (" + row[1].strip() + ")")
        print("*******************************************")
        print()
        return lstOfProductObjects
    # TODO: Add code to get product data from user
    @staticmethod
    def input_product_name_and_product_price():
        # TODO: Add Code Here!
        product_name = input('Enter product name: ')
        product_price = input('Enter product price: ')
        return str(product_name), str(product_price)


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program

FileProcessor.read_data_from_file(strFileName)
while True:
    print(IO.__doc__())
    IO.print_menu_Tasks()
    strChoice = IO.input_menu_choice()

    if strChoice.strip() == '1':
        IO.print_current_Tasks_in_list(lstOfProductObjects)
        continue
    elif strChoice.strip() == '2':
        product, price = IO.input_product_name_and_product_price()
        obj = Product(product, price)
        row = (obj.product_name, str(obj.product_price))
        lstOfProductObjects.append(row)
        continue
    elif strChoice.strip() == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print('Data saved, Exit the program')
        break

# Main Body of Script  ---------------------------------------------------- #
