import csv

def addGtinNumber():
    while True:
        try:
            gtinNumb = int(input("Please enter the GTIN-8 number of your product: "))
            print()
            break
        except ValueError:
            print("Oops! That is not a valid GTIN-8 number sorry, please try again: ")
    return(gtinNumb)

def addProduct():
    while True:
        try:
            product = str(input("Please enter the product to go along side the GTIN-8 number entered previously: "))
            print()
            break
        except ValueError:
            print("Oops! That is not a valid product, please try again: ")
    

def addQuantity():
    while True:   
        try:
            quantity = str(input("Please enter the quantity of the product entered previously: "))
            print()
            break
        except ValueError:
            print("Oops! That is not a valid quantity, please try again: ")

            return (quantity )
            
def addPrice(quantity):
    while True:
        try:
            price = input("Please enter the price of the product you wish to purchase: ")
            int(price)
            print()
            break
        except ValueError:
            print("Oops! Thats not a valid price, please try again: ")

    
    pricexQuantity = (price * quantity)
    print("The total price for the product is then", pricexQuantity)
    

myList = []

myList.append(addGtinNumber())
print(myList)

myList.append(addProduct())
print(myList)

addQuantity()

addPrice()

totalPrice()


print(myList)


    
    
        
                           
       



        
