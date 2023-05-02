
# Import all required modules
from string import ascii_uppercase
import random
import json
question_per_quiz = 7

# Open the file questions.json and save in variable questions
# The file contains the questions for the quiz app
with open("Questions.json","r") as json_object:
    QUESTIONS = json.load(json_object)

# 'prepare_questions' functions randomly reorder
# the questions on every run
def prepare_questions(questions, num_of_questions):
    num_of_questions = min(num_of_questions, len(questions))
    return random.sample(list(questions.items()), num_of_questions)

# binds alphabet to each alternative options(answers) and get user options
def get_answer(question, alternatives):
    print(question)
    labeled_alternative = dict(zip(ascii_uppercase, alternatives)) # binds ascii_letters(A,B..) to each options then convert to dict
    for label, alternative in labeled_alternative.items():
        print(label, alternative)
    
    # checks if user's choice(input) is in the available options
    while (choice := input("\nChoice? ").upper()) not in labeled_alternative:
        print(f"Please answer one of {', '.join(labeled_alternative)}")
    return labeled_alternative[choice]

# displays the questions and compare if user's choice is corrcet
def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternative = random.sample(alternatives, len(alternatives))
    answer = get_answer(question, ordered_alternative)
    if answer  == correct_answer:
        print("\nCorrect!\n")
        return 1
    else:
        print("\nWrong\n")
        return 0

def run ():
    score = 0
    question = prepare_questions(QUESTIONS, question_per_quiz)

    for num, (questions, alternatives) in enumerate(question, start=1):
        print("Question{}".format(num))
        score += ask_question(questions, alternatives)
    print("You got {} out of {}".format(score, num))
    
if __name__ == '__main__':
    run()
        
      
    

