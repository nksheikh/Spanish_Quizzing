## Main program for the Spanish intro quizzing ##
import random

def load_ordinal_numbers_quiz():
    user_input = ""
    while user_input != "quit":
        user_input = input("Random number: " + str(random.randint(0,30)))

load_ordinal_numbers_quiz()