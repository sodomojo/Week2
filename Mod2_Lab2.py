#!/usr/bin/env python

'''
Assign a random number between 50 and 100 to a variable called test_num (read page 50-52 in your text)
If test_num is divisible by three, print "fizz"
If test_num is divisible by five, print "buzz"
if test_num is divisible by both three and five, print "fizzbuzz!"

'''

test_num = int(input("Enter a number (> 0): "))

if test_num % 3 == 0 and test_num % 5 == 0:
    print ("fizzbuzz")

elif test_num % 3 == 0:
    print ("fizz")

elif test_num % 5 == 0:
    print("buzz")

else:
    pass

