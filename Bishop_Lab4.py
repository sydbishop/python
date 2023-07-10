# Program Name: Bishop_Lab4.py
# Course: IT1113/Section W01
# Student Name: Sydney Bishop
# Assignment Number: Lab 4
# Due Date: 07/06/2023
# Purpose: Average Test Scores

# create average function
def calc_average(grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8):
    grade_list = [grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8]
    list_length = len(grade_list)
    return sum(grade_list) /list_length

# create grade determination function
def determine_grade(average):
    if average >= 90:
        return 'A'
    if average >= 80:
        return 'B'
    if average >= 70:
        return 'C'
    if average >= 60:
        return 'D'
    else:
        return 'F'

# create loop to run program 12 times
for i in range(12):

    # create variable for student name
    name = input("Enter the student's first and last name: ")

    # create list of student's test scores
    scores = input("Enter the student's test scores separated by space: ")
    scores_list = scores.split()

    #convert list to integers
    scores_list = [int(x) for x in scores_list]

    # calculate average test score
    list_length = len(scores_list)
    average = calc_average(scores_list[0], scores_list[1], scores_list[2], scores_list[3], scores_list[4], scores_list[5], scores_list[6], scores_list[7])
    print(name, 'scored an average of', average)

    # determine student's letter grade from average
    grade = determine_grade(average)
    print(name, 'earned a(n)', grade, 'in the class.')