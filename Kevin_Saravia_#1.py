""" Kevin Saravia, PeopleSoft ID: 1478627
    Program #1: Sharing the Bill
    COSC 1306, Fall 2017
    This program computes individual shares of a restaurant bill. """

stringName = "Enter name of friend: "                       #string variables to avoid redundancy and keep things clean
stringBill = "Enter bill for "
comma = ", "
colon = ": "

name1 = input(stringName)                                   #takes input to give every individual a name
name2 = input(stringName)
name3 = input(stringName)
name4 = input(stringName)
name5 = input(stringName)

bill1 = input("\n" + stringBill + name1 + ": ")             #takes input to give every bill an amount for their specific person
bill2 = input(stringBill + name2 + colon)
bill3 = input(stringBill + name3 + colon)
bill4 = input(stringBill + name4 + colon)
bill5 = input(stringBill + name5 + colon)

print("\nName of friends: " + name1 + comma + name2         #prints everyone's names in order
      + comma + name3 + comma + name4 + comma + name5)
print("Individual bills: " + bill1 + comma + bill2          #prints everyone's bills in order
      + comma + bill3 + comma + bill4 + comma + bill5)

tipPercent = input("\nEnter tip percentage: ")              #takes input for the tip percentage
tipPercent = float(tipPercent) * 0.01                       #converts the inputted percentage to a float two decimal places to the left

bill1 = float(bill1)                                        #convert all the inputted bills to floats
bill2 = float(bill2)
bill3 = float(bill3)
bill4 = float(bill4)
bill5 = float(bill5)

billTotal = bill1 + bill2 + bill3 + bill4 + bill5           #adds up all the bills
tip = tipPercent *  billTotal                               #calculates the tip amount from the total bill amount
total = tip + billTotal                                     #adds up the tip amount with the total bill amount
payment = total / 5                                         #divides the overall total by 5 to determine how much each individual is paying

print("\nTotal bill plus tip: $ %.2f" % total)              #prints the total bill amount with only 2 decimal places
print("Each of us must pay $ %.2f" % payment)               #prints how much each person is paying with only 2 decimal places
