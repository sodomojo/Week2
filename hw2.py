#!/usr/bin/env python

"""

"""

# Capture buyer inputs and store as separate variables

buyer_first_name, buyer_last_name = input("What is your full name? ").split()
buyer_address = input("What is your address? ")
buyer_phone = input("What is your phone number? (xxx-xxx-xxxx) ").split("-")
car_make, car_model = input("What is the make and model of your car? ").split()
purchase_price = float(input("What is the purchase price of your {} {}? $".format(car_make, car_model)))

print("\n")

# set float values for each of the taxes
sales_tax = float(0.09)
license_fee = float(0.05)
dealer_prep = float(0.03)

# calculate the
sales_price = purchase_price * sales_tax
license_price = purchase_price * license_fee
dealer_price = purchase_price * dealer_prep

full_tax_price = purchase_price * (sales_tax + license_fee + dealer_prep)
total_price = purchase_price + full_tax_price

'''
create a user id function 
will take the last four characters of the user's last name
combine last four characters with area code from user's phone number

'''


def user_id():
    acct_id = buyer_last_name[-4:].upper()+"_"+buyer_phone[0]
    return acct_id


# print purchase receipt for car purchase
print("Hello {} {}. \n".format(buyer_first_name, buyer_last_name))

print("Thank you for your purchase of a {} {}.  The following is a \
breakdown of your total price: \n".format(car_make, car_model))

# each tax should display the hundredth decimal place
print("Sales tax: ${} \n".format("%.2f" % sales_price))

print("Licensing Fee: ${} \n".format("%.2f" % license_price))

print("Dealer Prep Fee: ${} \n".format("%.2f" % dealer_price))

print("Total Price: ${} \n".format("%.2f" % total_price))

# return user id function for ID number
print("You have been assigned an ID number of {}.  Please refer to this ID number if \
you have any questions \n".format(user_id()))
