# Program Name: Bishop_Lab3.py
# Course: IT1113/Section W01
# Student Name: Sydney Bishop
# Assignment Number: Lab 3
# Due Date: 06/28/2023
# Purpose: Tuition Rate Increase

# create variables
start_year = int(2017)
tuition = int(6450)
tuition_rate = float(0.035)

# create loop to calculate tuition rate increase over 7 years
for year in range(start_year, start_year+8):
    print('The tuition cost for', year, 'is', tuition)
    tuition = tuition + (tuition * tuition_rate)



