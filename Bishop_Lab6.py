# Program Name: Bishop_Lab6.py
# Course: IT1113/Section W01
# Student Name: Sydney Bishop
# Assignment Number: Lab 6
# Due Date: 07/20/2023
# Purpose: Calculating Rainfall

# create an empty list to store rainfall for each month
rainfall_list = []

# create an empty dictionary to store the data
monthly_rainfall = {}

# create loop to run program 12 times 
for i in range(12):

    # enter the total rainfall for each month
    month = input("Enter the month: ")
    print("Enter the total rainfall for",month,"in inches:")
    rainfall = float(input())

    # store rainfall to list
    rainfall_list.append(rainfall)

    # add row to dictionary to map rainfall to its month
    monthly_rainfall[rainfall] = month

# calculate total rainfall for the year
total = sum(rainfall_list)
print("There was a total of",total,"inches of rainfall this year.")

# calculate average monthly rainfall
list_length = len(rainfall_list)
average = round(total / list_length, 3)
print("The average rainfall for each month was",average,"inches.")

# sort the list from lowest to highest value
rainfall_list.sort()

# print the month with the highest rainfall
print("The lowest rainfall amount was",rainfall_list[0],"inches during the month of",monthly_rainfall[rainfall_list[0]])

# print the month with the lowest rainfall
print("The highest rainfall amount was",rainfall_list[-1],"inches during the month of",monthly_rainfall[rainfall_list[-1]])
