import random
import json

QUESTIONS_FILE = open('questions.json')

def main():
    playing = True

    while playing != False:
        print("I have a general knowledge quiz for you !")
        playing = input("Are you interested ? ")
        if playing.lower() == "yes":
            play()
            playing = False
        elif playing.lower() == "no":
            playing = False
        else:
            print("You have to type either yes or no.")

def play():
    correct = 0
    name = input("What's your name, player ? ")
    list = json.load(QUESTIONS_FILE)
    questions_list = list['questions']
    number_questions = len(list['questions'])

    print(f"Hello {name} ! Welcome to our quiz game !")
    print(f"Today, for you, we have {number_questions} questions for you !")

    for i in range(len(questions_list)):
        question = random.choice(questions_list)
        answer = input(question['question'])
        if answer.lower() == question['answer'].lower():
            print("Correct !")
            correct += 1
        else:
            print(f"Wrong ! The right answer was : {question['answer']}")
        questions_list.remove(question)
    
    print(f"You had {correct} right answers, out of {number_questions} possible ones.")

main()