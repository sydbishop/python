# Program Name: Bishop_Test3.py
# Course: IT1113/Section W01
# Student Name: Sydney Bishop
# Assignment Number: Test 3
# Due Date: 07/20/2023
# Purpose: Convert Kilometers to Miles

# create conversion function
def calculate_miles(km):
    miles = km * 0.6214
    miles = round(miles,1)
    return miles

# create loop to run program 15 times
for i in range(15):

    # get kilometer data from user
    distance = float(input("Enter the distance in kilometers: "))

    # convert kilometers to miles
    conversion = calculate_miles(distance)
    print(distance,"kilometers is equal to",conversion,"miles.")

