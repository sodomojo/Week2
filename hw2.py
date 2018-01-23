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

sales_tax = float(0.09)
license_fee = float(0.05)
dealer_prep = float(0.03)

sales_price = purchase_price * sales_tax
license_price = purchase_price * license_fee
dealer_price = purchase_price * dealer_prep

full_tax_price = purchase_price * (sales_tax + license_fee + dealer_prep)
total_price = purchase_price + full_tax_price


def user_id():
    acct_id = buyer_last_name[-4:].upper()+"_"+buyer_phone[0]
    return acct_id


print("Hello {} {}. \n".format(buyer_first_name, buyer_last_name))

print("Thank you for your purchase of a {} {}.  The following is a \
breakdown of your total price: \n".format(car_make, car_model))

print("Sales tax: ${} \n".format("%.2f" % sales_price))

print("Licensing Fee: ${} \n".format("%.2f" % license_price))

print("Dealer Prep Fee: ${} \n".format("%.2f" % dealer_price))

print("Total Price: ${} \n".format("%.2f" % total_price))

print("You have been assigned an ID number of {}.  Please refer to this ID number if \
you have any questions \n".format(user_id()))
