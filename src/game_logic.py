import random

def generate_numbers():
    return random.sample(range(100, 1000), 4)

def check_answer(user_input, correct_numbers):
    #check user input
    user_numbers = [int(x) for x in user_input.split()]
    return sorted(user_numbers) == sorted(correct_numbers)