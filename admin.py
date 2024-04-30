# Name:  Kim Tran
# Student Number:   10657323  

# Import the json module to allow us to read and write data in JSON format.
import json

# This function repeatedly prompts for input until an integer is entered (an integer of 1 or more).
def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
        except ValueError:
            pass

# This function repeatedly prompts for input until something other than whitespace is entered.
def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value != '':
            return value

# This function opens "data.txt" in write mode and writes the data to it in JSON format.
def save_data(data_list):
    f = open('data.txt', 'w')
    json.dump(data_list, f, indent = 2)
    f.close()

# This function adds new question to the list.
def add_question(data):
    question = input_something('Enter the question: ')
    answers = []
    
    while True:
        value = input_something('Enter a valid answer (enter "q" when done): ').lower()
        if value == 'q':
            break
        answers.append(value)

    while True:
        difficulty = input_int('Enter question difficulty (1-5): ')
        if  1 <= difficulty <= 5:
            break
        print('Invalid value. Must be an integer between 1 and 5.')
        
    data.append({'question': question, 'answers': answers, 'difficulty': difficulty})
    save_data(data)
    print('Question added!')

# This function list all current questions.
def list_questions(data):
    if not data:
        print('No questions saved.')
        return

    print('Current questions:')
    for idx, details in enumerate(data):
        print('  ' + str(idx + 1) + ') ' + details['question'])

# This function prints questions that contain the search term.
def search_question(data):
    if not data:
        print('No questions saved.')
        return
    
    search_term = input_something('Enter a search term: ')
    count = 0
    
    for idx, details in enumerate(data):
        if search_term.lower() in details['question'].lower():
            print('  ' + str(idx + 1) + ') ' + details['question'])
            count = count + 1
            
    if count == 0:
        print('No results found.')

# This function prints details of a specific question.
def view_question(data):
    if not data:
        print('No questions saved.')
        return
    
    index = input_int('Question number to view: ')

    if 1 <= index <= len(data):
        item = data[index - 1]
        print('\nQuestion: ', item['question'])
        if (len(item['answers']) > 1):
            print('Answers:', ', '.join(item['answers']))
        else:
            print('Answer:', ', '.join(item['answers']))
        print('Difficulty:', item['difficulty'])
        return
    
    print('Invalid index number.')

# This function deletes a specific question.
def delete_question(data):
    if not data:
        print('No questions saved.')
        return
    
    index = input_int('Question number to delete: ')

    if 1 <= index <= len(data):
        del data[index - 1]
        save_data(data)
        print('Question deleted!')
        return

    print('Invalid index number.')

# Main program
def main():
    data = None
    try:
        f = open('data.txt', 'r')
        data = json.load(f)
        f.close()
    except:
        data = []

    print('Welcome to the Quiz Admin Program.')

    options = {
        'a': add_question,
        'l': list_questions,
        's': search_question,
        'v': view_question,
        'd': delete_question
    }

    while True:
        print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
        choice = input('> ')
        if choice in options:
            options[choice](data)
        elif choice == 'q':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')

main()
# If you have been paid to write this program, please delete this comment.
