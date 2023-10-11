'''
Description: Self-Checkout Counter (Self-Input prices)

Name: Tremendes Roper

Date: 10/06/2023
'''
import math 

# This is for adjustable tax rates just incase the user lives in different areas

def taxPercent(tax):

    return tax / 100

# Step 1: Set up the system to ask the number of items they are purchasing

def selfCheckout():
    
    numItems = int(input("How many items are you scanning? "))
    checkList = []
    counter = 1
    priceList = []
    subtotal = 0.00

    # Step 2: Asking for what the user is purchasing and the price of said item. The loop continues with the number of items they inputted. 
    # The prices of the items are also added into a new variable called "Subtotal." Realistically, there are sales taxes.
    while (counter <= numItems):
        check = input("Enter the item you are checking out: ")
        checkList.append(check)
        price = float((input("Enter the price of the item: ")))
        subtotal += price
        priceList.append(price)
        counter += 1 
    
    # Step 3: Print out the products with the prices.
    print(f"Your order was:")
    # This prints out whatever is in the two lists, then format the price in two decimals places (.2f). The decimal places are adjustable.
    for i in range(numItems):
        print(f"{checkList[i]}: ${priceList[i]:.2f}")

# Step 4: Take the subtotal and multiply this by the sales tax from earlier. After this, add them together.
# The places where "9" are replaceable with other tax percents.
    salesTax =  subtotal * taxPercent(9)
    total = subtotal + salesTax
    total = round(total, 2)
    wholePercent = taxPercent(9) * 100 
    print (f"Your subtotal comes to ${subtotal}. " + f"With {wholePercent:.0f}% sales tax, your total is ${total}.")
    
# Step 5: Ask for payment amount then subtract the total from it
    paymentAmount = float(input("Please insert payment amount: "))
    cashBack = paymentAmount - total
    cashBack = round(cashBack, 2)

# Step 6: Print out the final total for cash back. If the customer does not have sufficient cash, it will print out something else.
    if paymentAmount >= total:
        print(f"I owe you back ${cashBack}.\nThank you for shopping with us! See you soon.")
    else:
        print("You have insufficient funds.")

selfCheckout()