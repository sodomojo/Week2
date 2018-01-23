#!/usr/bin/env python

'''
Create variables to store user input for:
    User name
    User phone number
    Favorite cheese
    Average monthly amount spent on their favorite cheese


Combine the phone number and username variables to create an account ID
Use the replace() method to replace the first letter of your User ID with a Z and store that value as the final user ID

Feel free to add as much snark as you want.
Make sure your script runs, and upload the python script here.

'''
# Create variables to store user input:

userName = input("What is your name? ")
userPhone = input("What is your phone number? (xxx-xxx-xxxx) ")
userCheese = input("What is your favorite cheese? ")

# Store the amount spent on cheese as a float cast to an int
monthCheese = float(input("How much do you typically spend on cheese per month? $"))
monthCheese = int(monthCheese)

# Calculate the daily amount this user spends on cheese and store this value as a variable
avgMonth = monthCheese / 30

# Split the user's phone number based on "-"
splPhone = userPhone.split("-")

# Use the string slicing method to store the first three letters of the user's name as a variable and replace the first letter with a "Z"
splName = userName[0:3]
userAcct = splName.replace(splName[0], "Z")

acctId = splPhone[2]+userAcct

# Print out a string telling the user what their account ID is, and letting them know what their daily cheese spending habits look like.
print("Your user account is {} and you spend a total of ${} per day on cheese.  That's weird.".format(acctId, float("%.2f" % avgMonth)))