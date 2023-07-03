from os import name, system, path
from time import sleep
import csv
from random import randint

################################################################################
# GLOBAL FUNCTIONS
################################################################################

def clear():
    '''Clears the consol screen. '''

    if name == "nt":
        system("cls")
    else:
        system("clear")


def waitForEnter():
    '''The function used to wait until the user indicates that 
    is ready to proceed by pressing the ENTER key.'''

    input("Press ENTER ...")


def splashScreen():
    '''Showing logo on startup.'''

    clear()

    title = '''\
             ___           ___           ___                    ___                       ___              
            /\  \         /\__\         /\__\                  /\__\                     /\__\             
            \:\  \       /:/  /        /::|  |                /:/ _/_       ___         /:/ _/_            
             \:\  \     /:/  /        /:/:|  |               /:/ /\  \     /\__\       /:/ /\__\           
         ___  \:\  \   /:/  /  ___   /:/|:|  |__            /:/ /::\  \   /:/__/      /:/ /:/ _/_          
        /\  \  \:\__\ /:/__/  /\__\ /:/ |:| /\__\          /:/_/:/\:\__\ /::\  \     /:/_/:/ /\__\         
        \:\  \ /:/  / \:\  \ /:/  / \/__|:|/:/  /          \:\/:/ /:/  / \/\:\  \__  \:\/:/ /:/  /         
         \:\  /:/  /   \:\  /:/  /      |:/:/  /            \::/ /:/  /   ~~\:\/\__\  \::/_/:/  /          
          \:\/:/  /     \:\/:/  /       |::/  /              \/_/:/  /       \::/  /   \:\/:/  /           
           \::/  /       \::/  /        |:/  /                 /:/  /        /:/  /     \::/  /            
            \/__/         \/__/         |/__/                  \/__/         \/__/       \/__/             \n'''
        
    print(title)

################################################################################
# END OF GLOBAL FUNCTIONS
################################################################################


################################################################################
# CLASS TEACHER
################################################################################
class Teacher:

    def __init__(self):
        self.file = ""
        self.numOfQuestionsToAsk = 0
        self.numCorrect = 0
        self.questions = []
        self.answers = []
        
    def loadQuestionsAndAnswers(self):
        '''The function for loading questions and answers, 
        provided that the file has valid content.'''

        if self.file == "":
            print("ERROR! File was not loaded. First use 'Load file' option.")
            sleep(2)
            return False

        with open(self.file, 'r') as csvinput:
            reader = csv.reader(csvinput)
            
            self.questions = [] # clear previously loaded questions
            self.answers = [] # clear previously loaded answers
            for row in reader:

                if len(row) < 2 or len(row) > 2:
                    print("ERROR! Incorrect file format. Read 'Help'.") 
                    sleep(2)
                    return False

                question, answer = row[0], row[1]

                self.questions.append(question)
                self.answers.append(answer)

        numQuestionsAvailable = len(self.questions)
        print(f"Successfully loaded {numQuestionsAvailable} questions.")
        sleep(1)
        return True


    def exam(self):
        '''The function performing the querying process.'''

        self.numCorrect = 0
        self.numOfQuestionsToAsk = int(input("Enter the number of questions to be asked: "))
        numQuestionsAvailable = len(self.questions)

        for iDraw in range(self.numOfQuestionsToAsk):
            clear()
            splashScreen()
            
            iQuestion = randint(0, numQuestionsAvailable-1)
            
            question = self.questions[iQuestion]
            correctAnswer = self.answers[iQuestion]

            print(f"Question {iDraw+1} / {self.numOfQuestionsToAsk}:")
            print(question)
            odp = input("Ans.: ")

            if(odp == correctAnswer):
                print("(^_^) Correct!")
                self.numCorrect += 1
            else:
                print("(T_T) Wrong answer!")
                print(f"The correct answer is: {correctAnswer}")

            sleep(2)

        print("End of the test.")
        

    def presentScore(self):
        '''The function displaying the querying result.'''
        print("Here is your result: ")
        percentCorrect = self.numCorrect/self.numOfQuestionsToAsk*100
        print(f"Correct answers: {self.numCorrect} / {self.numOfQuestionsToAsk} ({percentCorrect} %)")

################################################################################
# END OF CLASS TEACHER
################################################################################


################################################################################
# CLASS MENU
################################################################################
class JustLearnMenu:

    def __init__(self):
        self.teacher = Teacher()
        pass


    def endProgram(self):
        '''The function performing the actions intended at the end of the program.'''
        
        clear()
        splashScreen()
                
        print("Thank you for spending time with JustLearn! :) \n \
            See you soon!")
        sleep(2)
        

    def loadFile(self):
        '''The function prompting the user to provide a file to load'''
        
        odp = input("Enter the file name to load.: ") 

        if not path.exists(odp):
            print("ERROR! No such file!")
            sleep(2)
            return ""
        if not path.isfile(odp):
            print("ERROR! Given object is not a file!")
            sleep(2)
            return ""
        
        loadedFile = odp
        return loadedFile


    def help(self):
        '''The function displaying instructions on how to prepare the file 
        for learning and how to use the program'''
        
        helpLines = [

"""USING THE PROGRAM""",

"""JustLearn! program allows for self-quizzing on user-provided learning material.""",

"""First, use the '1. Load file' option.
The user will be prompted to provide a relative path to the file
containing the learning material (instructions on preparing
such a file will be discussed further).""",

"""If the provided path does not lead to a file, program will return to
the main menu.""",

"""After successfully specifying the file, use the '2. Learn!' option.""",

"""The file's validity will be checked.""",

"""If the file is valid, the user will be asked to enter the number of questions to be randomly selected.""",

"""Then, the user answers a series of questions.""",

"""There is only one correct answer for each question.""",

"""Questions may repeat.""",

"""Letter case in the answer matters.""",

"""After going through the specified number of questions, a summary is displayed: the number and percentage of correct answers.""",

"""Then, program returns to the main menu, and the user can:
- study again using the same file,
- load another file for learning,
- exit the program.""",

"""QUESTION FILES - GUIDELINES""",

"""The user can prepare more than one file for learning.""",

"""Each file must contain two columns of data WITHOUT A HEADER,
separated by a COMMA (CSV format), i.e.:

question1,answer1
question2,answer2
question3,answer3

Example below:
""",

"""
How many moons orbit around the Earth?,1
Who was the first ruler of Poland?,Mieszko I
Provide the formula for the area of a rectangle.,A=ab
""",

"""Important guidelines:
- Each row in the file must contain EXACTLY ONE comma that separates
  the question from the answer.
- There MUST NOT be a space after the comma.
- The number of rows in the file is also the number of possible questions
  from which random selection occurs.
"""


"""
END OF HELP
"""
        ]

        for line in helpLines:
            print(line)
            print()
            waitForEnter()
            clear()
            splashScreen()
    


    def mainMenu(self):
        '''The function displaying and handling the main menu of the program.'''
        
        
        while True:
            try:

                clear()
                splashScreen()

                print(f"[Currently loaded file: {self.teacher.file}]\n")
                print("1. Load file ")
                print("2. Learn! ")
                print("3. Help ")
                print("4. Exit ")

                ans = input("Choose option 1-4: ")

                clear()
                splashScreen()

                if ans not in {"1", "2", "3", "4"}:
                    print("INCORRECT CHOICE! Try again.")
                    sleep(2)
                    continue

                if ans == "1": # Load file
                    self.teacher.file = self.loadFile()
                    
                    if self.teacher.file == "":
                        continue
                    
                if ans == "2": # Learn!
                    if(self.teacher.loadQuestionsAndAnswers()):
                        clear()
                        splashScreen()
                        self.teacher.exam()

                        clear()
                        splashScreen()
                        self.teacher.presentScore()
                        waitForEnter()

                if ans == "3": # Help
                    self.help()

                if ans == "4": # Exit
                    self.endProgram()
                    break
            except:
                print("ERROR! Returning to the main menu ...")
                sleep(2)

################################################################################
# END OF CLASS MENU
################################################################################