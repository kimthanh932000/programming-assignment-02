# Name:  Kim Tran
# Student Number:   10657323  

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 1, 2024.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json




# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
        except:
            continue


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    value = ''
    while value == '':
        value = input(prompt).strip()
    return value


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    f = open('data.txt', 'w')
    json.dump(data_list, f, indent = 2)
    f.close()

def main():
    data = None
    try:
        f = open('data.txt', 'r')
        data = json.load(f)
        f.close()
    except:
        data = []

    print('Welcome to the Quiz Admin Program.')

    while True:
        print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
        choice = input('> ')
            
        if choice == 'a':
            answers = []
            question = input_something('Enter the question: ')

            value = ''
            while value != 'q':
                value = input_something('Enter a valid answer (enter "q" when done): ').lower()
                if value != 'q':
                    answers.append(value)
            
            while True:
                difficulty = input_int('Enter question difficulty (1-5): ')
                if difficulty >= 1 and difficulty <= 5:
                    break
                print('Invalid value. Must be an integer between 1 and 5.')

            question_details = {'question': question, 'answers': answers, 'difficulty': difficulty}
            data.append(question_details)
            save_data(data)
            print('Question added!')
        
        elif choice == 'l':
            if len(data) == 0:
                print('There are no questions saved.')
            else:
                print('Current questions:')
                for idx, details in enumerate(data):
                    print('  ' + str(idx + 1) + ') ' + details['question'])



        elif choice == 's':
            if len(data) == 0:
                print('There are no questions saved.')
            else:
                search_term = input_something('Enter a search term: ')
                count = 0
                for idx, details in enumerate(data):
                    if search_term.lower() in details['question'].lower():
                        print('  ' + str(idx + 1) + ') ' + details['question'])
                        count = count + 1
                if count == 0:
                    print('No results found.')
                


        elif choice == 'v':
            if len(data) == 0:
                print('There are no questions saved.')
            else:
                number = input_int('Question number to view: ')
                count = 0
                for idx, details in enumerate(data):
                    if number == idx + 1:
                        print('\nQuestion: ', details['question'])
                        if (len(details['answers']) == 1):
                            print('Answer:', ', '.join(details['answers']))
                        else:
                            print('Answers:', ', '.join(details['answers']))
                        print('Difficulty:', details['difficulty'])
                        count = count + 1
                        break
                if count == 0:
                    print('Invalid index number.')



        elif choice == 'd':
            if len(data) == 0:
                print('There are no questions saved.')
            else:
                number = input_int('Question number to delete: ')
                count = 0
                for idx, details in enumerate(data):
                    if number == idx + 1:
                        del data[idx]
                        count = count + 1
                        print('Question deleted!')
                        save_data(data)
                        break
                if count == 0:
                    print('Invalid index number.')



        elif choice == 'q':
            print('Goodbye!')
            break



        else:
            print('Invalid choice.')


main()
# If you have been paid to write this program, please delete this comment.
