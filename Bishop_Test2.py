# Program Name: Bishop_Test2.py
# Course: IT1113/Section W01
# Student Name: Sydney Bishop
# Assignment Number: Test 2
# Due Date: 07/10/2023
# Purpose: Total Stamps Collected in a Year

# create empty list to hold count of stamps for each month
stamp_list = [ ]

# create loop to run program 12 times 
for i in range(12):

    # prompt user for month of the year
    print("Enter the month :")
    month = input( )

    # prompt user for number of stamps collected
    print("Enter the total number of stamps you collected for",month,":")
    stamps = int(input( ))

    stamp_list.append(stamps)

# calculate total number of stamps collected over 12 months
total = sum(stamp_list)
print("You have collected a total of",total,"stamps this year")










