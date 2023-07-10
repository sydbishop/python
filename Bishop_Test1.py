# Program Name: Bishop_Lab2.py
# Course: IT1113/Section W01
# Student Name: Sydney Bishop
# Assignment Number: Test 1
# Due Date: 06/23/2023
# Purpose: Primary Color Mixer

# create valid input indicator
valid = False

while valid == False:
    # create variable for first color
    color_1 = input("Enter the first primary color to mix: ")
    color_1 = color_1.lower()

    # determine if primary color was entered
    if color_1 == 'red' or color_1 == 'blue' or color_1 == 'yellow':
        print('Color accepted. ')
        valid = True
    else:
        print('ERROR: please enter a primary color. ')


# create valid input indicator
valid = False

while valid == False:
    # create variable for second color
    color_2 = input("Enter the second primary color to mix: ")
    color_2 = color_2.lower()

    # determine if primary color was entered
    if color_2 == 'red' or color_2 == 'blue' or color_2 == 'yellow':
        print('Color accepted. ')
        valid = True
    else:
        print('ERROR: please enter a primary color. ')


# creating purple
if color_1 == 'red' and color_2 == 'blue':
    print('You created purple!')

if color_1 == 'blue' and color_2 == 'red':
    print('You created purple!')

# creating orange
if color_1 == 'red' and color_2 == 'yellow':
    print('You created orange!')

if color_1 == 'yellow' and color_2 == 'red':
    print('You created orange!')

# creating green
if color_1 == 'blue' and color_2 == 'yellow':
    print('You created green!')
    
if color_1 == 'yellow' and color_2 == 'blue':
    print('You created green!')
