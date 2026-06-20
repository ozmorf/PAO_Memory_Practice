from ascii import *
from rich import print as rprint
from core_functions import *
# from rich.console import Console
import random

def answer_three(): #takes argument 'difficulty'
    # easy (6 digits), medium (12-13), hard (14-17), and custom (user chooses up to 20)
    #
    # if difficulty == check_valid_input():
    #     pass

    win = "Ummm, that was correct. Good job, buck-o."
    lose = "Ha! I [italic]knew[/italic] you needed to study more. That is incorrect. \nThe correct phrase is {correct_phrase}"
    three_numbers = gen_ran_num_list(6)

    print(pair_digits(three_numbers))
    print(gen_phrase(three_numbers))
    
    correct_phrase = gen_phrase(three_numbers)
    user_input = collect_user_input(len(str(three_numbers)))

    if check_answer(user_input, correct_phrase):
        rprint(f"[green]Ummm, that was correct. Good job, buck-o.[/green]")
    else:
        rprint(f"[yellow]Ha! I [italic]knew[/italic] you needed to study more. That is incorrect. \nThe correct phrase is {correct_phrase}[/yellow]")



def pick_range(num):

    num = int(num)
    user_num_list = [] #shuffled numbers based on the user's input
    user_list_answer = {} #answer-key based on the shuffled numbers

    #gen ran nums within range of _0 - _9 based on user's input
    for i in range(num, num+9):
        user_num_list.append(i)
    random.shuffle(user_num_list)

    #generate the answer key
    
    for num in user_num_list:
        PAO_phrase = gen_PAO_phrase(num)
        user_list_answer[num] = PAO_phrase

    #loop through each item of the user_num_list, get PAO answer for each item
    for number in user_num_list: 
        rprint(f"Enter the correct PAO phrase for {number}: ")
        user_answer = collect_user_input(number)

        if user_answer[0].lower() == "hint":
            choose_1_or_2 = random.randint(1,2)
            hint = user_list_answer[number][choose_1_or_2]
            rprint(f"[bright_cyan]Hint, huh? Well well, looks like [italic]somebody[/italic] needs to study more.\nHere's the hint for little precious: [yellow]'{hint}'[/yellow][/bright_cyan]")
            user_answer = collect_user_input(number)

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

