from ascii import *
from rich import print as rprint
from core_functions import *
# from rich.console import Console
import random

def convert_numbers(difficulty):
    
    difficult_num = None

    if difficulty == "easy":
        difficulty_num = 4
    elif difficulty == "medium":
        difficulty_num = 6
    elif difficulty == "hard":
        difficulty_num = 12
    elif difficulty == "custom":
        print(f"difficulty set to custom...")
        difficulty_num = 4
    else:
        print(f"difficulty not chosen. Setting digits to length of 4")
        difficulty_num = 4

    num_list = []
    answer_key = {}

    #create random num list and answer key
    for num in range(10):
        num_list.append(gen_ran_num(difficulty_num))

    for item in num_list:
        answer_key[item] = gen_phrase(item)

    #main loop for the mode
    for number in answer_key:
        rprint(f"enter the correct phrase for [cyan]{number}[/cyan]")
        user_answer = collect_user_input()

        if user_answer[0].lower() == "hint":
            rprint(f"Here's your hint: [yellow]{give_hint(answer_key[number])}[/yellow]")
            user_answer = collect_user_input()
        elif user_answer[0].lower() == "menu":
            return "menu"
        elif user_answer[0].lower() == "quit":
            return "quit"


        if check_answer(user_answer, answer_key[number]):
            rprint(f"[green]Correct![/green]")
        else:
            rprint(f"Not quite. The answer is [yellow]{answer_key[number]}[/yellow]\n")
    
    return "done"

def convert_phrases():
    
    for round in range(10):
        # gen_shuffled_PAO_phrase(number_of_words)
        # for i in range(3):
        #     num = gen_ran_two_digit_num()
        pass


def pick_range(num):

    num = int(num)
    user_num_list = [] #shuffled numbers based on the user's input
    user_list_answer = {} #answer-key based on the shuffled numbers

    #gen ran nums within range of _0 - _9 based on user's input
    for i in range(num, num+10):
        user_num_list.append(i)
    random.shuffle(user_num_list)

    #generate the answer key

    for num in user_num_list:
        PAO_phrase = gen_PAO_phrase(num)
        user_list_answer[num] = PAO_phrase

    #loop through each item of the user_num_list, get PAO answer for each item
    for number in user_num_list: 
        rprint(f"Enter the correct PAO phrase for {number}: ")
        user_answer = collect_user_input()

        if user_answer[0].lower() == "hint":
            choose_1_or_2 = random.randint(1,2)
            hint = user_list_answer[number][choose_1_or_2]
            rprint(f"[bright_cyan]Hint, huh? Well well, looks like [italic]somebody[/italic] needs to study more.\nHere's the hint for little precious: [yellow]'{hint}'[/yellow][/bright_cyan]")
            user_answer = collect_user_input()

        elif user_answer[0].lower() == "menu":
            return "menu" 
        
        elif user_answer[0].lower() == "quit":
            return "quit"

        result = check_answer(user_answer, user_list_answer[number])

        #check if user_answer is correct

        if result:
            rprint(f"[green]Correct![/green]") # add in "_#_ Remaining" after each message
        else:
            rprint(f"[yellow]I'm sorry, that's incorrect. The correct phrase is {user_list_answer[number]}")

    return "done"

