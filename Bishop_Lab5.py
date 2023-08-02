# Program Name: Bishop_Lab5.py
# Course: IT1113/Section W01
# Student Name: Sydney Bishop
# Assignment Number: Lab 5 Part 1
# Due Date: 07/16/2023
# Purpose: Country Club - Read and Write Golf Scores

# this program saves a collection of golf scores to golf.txt
def main():

    # open the file to hold the score info
    score_file = open('golf.txt', 'w')

    # get each golfer's data and write it to the file
    for i in range(16):

        # get the data for the golfer
        print('Enter the first name of the player : ')
        first_name = input()

        print('Enter the last name of the player : ')
        last_name = input()

        print('Enter the handicap for',first_name,last_name,':')
        handicap = input()

        print('Enter the score for',first_name,last_name,':')
        score = input()

        # write the data as a record to the file
        score_file.write(first_name + '\n')
        score_file.write(last_name + '\n')
        score_file.write(handicap + '\n')
        score_file.write(score + '\n')

    # close the file
    score_file.close()
    print('Marietta Country Club golf records written to golf.txt')

# call the main function
main()



