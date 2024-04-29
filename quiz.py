# Name: Kim Tran
# Student Number:   10657323  

# Import the required modules.
import tkinter
import tkinter.messagebox
import json
import random


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        self.main = tkinter.Tk()
        self.main.title('Quiz')
        self.current_question = 0
        self.score = 0
        self.quiz_questions = []
        self.item = None

        try:            
            f = open('data.txt', 'r')
            self.data = json.load(f)
            f.close()

            if len(self.data) < 5:
                tkinter.messagebox.showerror('Error!', 'Insufficient number of questions!')
                self.main.destroy()
                return
            
            self.quiz_questions = random.sample(self.data, 5)
        except:
            tkinter.messagebox.showerror('Error!', 'Missing/Invalid file!')
            self.main.destroy()
            return

        self.question_label_var = tkinter.StringVar()
        self.question_number_var = tkinter.StringVar()
        
        self.question_number = tkinter.Label(self.main, pady=6, textvariable=self.question_number_var)
        self.question_label = tkinter.Label(self.main, padx=30, pady=4, textvariable=self.question_label_var)
        self.hard_label = tkinter.Label(self.main, text='This is a hard one - good luck!', fg='blue', padx=30, pady=4)
        
        self.bottom = tkinter.Frame(self.main, padx=30, pady=10)
        self.answer_entry = tkinter.Entry(self.bottom, width=40)
        self.submitButton = tkinter.Button(self.bottom, text='Submit Answer', command=self.check_answer)
        
        self.answer_entry.pack(side='left', padx=10)
        self.submitButton.pack(side='left')
        self.question_number.pack()
        self.question_label.pack()
        self.bottom.pack()

        self.show_question()
        
        tkinter.mainloop()


    def show_question(self):
        # This method is responsible for displaying the current question and some other messages in the GUI
        self.item = self.quiz_questions[self.current_question]
        self.question_number_var.set('Question ' + str(self.current_question + 1) + ' of 5:')
        self.question_label_var.set(self.item['question'])

        if self.item['difficulty'] in [4, 5]:
            self.hard_label.pack(before=self.question_label)
        else:
            self.hard_label.pack_forget()
        
        self.answer_entry.delete(0, tkinter.END)
        self.answer_entry.focus_set()


    def check_answer(self):   
        # This method is responsible for checking if the user's answer is correct when the button is clicked.        
        answer = self.answer_entry.get().lower()

        if answer in self.item['answers']:
            self.score = self.score + (self.item['difficulty'] * 2)
            tkinter.messagebox.showinfo('Correct!', 'You are correct!')
        else:
            tkinter.messagebox.showerror('Incorrect!', 'Sorry. That was incorrect!')

        self.current_question += 1
        
        if self.current_question == len(self.quiz_questions):
            tkinter.messagebox.showinfo('Final Score', 'Game over,\nFinal score: ' + str(self.score) + ' \n\nThank you for playing!')
            self.main.destroy()
            return
        
        self.show_question()
                        

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()

# If you have been paid to write this program, please delete this comment.
