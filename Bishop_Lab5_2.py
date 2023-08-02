# Program Name: Bishop_Lab5_2.py
# Course: IT1113/Section W01
# Student Name: Sydney Bishop
# Assignment Number: Lab 5 Part 2
# Due Date: 07/16/2023
# Purpose: Country Club - Read and Write Golf Scores

# this program reads the golf data in golf.txt 
# and displays the score for each golfer
def main():
    # open golf.txt for reading
    score_file = open('golf.txt', 'r')

    # read the first line from golf.txt
    # i.e. the first name of the first golfer
    first_name = score_file.readline()

    # if a field was read, continue processing
    while first_name != '':
        # read the last name field
        last_name = score_file.readline()

        # read the handicap field
        handicap = score_file.readline() 

        # read the score field
        score = score_file.readline()

        # strip the newlines from the fields
        first_name = first_name.rstrip('\n')
        last_name = last_name.rstrip('\n')
        handicap = handicap.rstrip('\n')
        score = score.rstrip('\n')

        # display the golfer's record
        print('First name:',first_name)
        print('Last name:',last_name)
        print('Handicap:',handicap)
        print('Golf Score:',score)

        # determine the result of the golfer's score
        score = int(score)
        if score == 80:
            print('Made Par')
        if score > 80:
            print('Over Par')
        if score < 80:
            print('Under Par')
        
        # print an empty line for spacer
        print()
        
        # read the first name of the next record
        first_name = score_file.readline()

    # close the file
    score_file.close()

# call the main function
main()


    

