from ascii import *
from rich import print as rprint
from core_functions import *

from rich.console import Console


def menu():
    menu_choices = ["choose 3", "pick range", "menu", "quit"]

    #welcome sequence
    # display_welcome_sequence()
    # display_menu(menu_choices)

    user_menu_input = input(f"Type your response and hit enter: ")

    count = 0

    #get valid user_menu_input or quit

    """ 
    while user_menu_input.lower() not in menu_choices:
        if count < 2:
            user_menu_input = input("That response is not in my data banks. Please type a valid response: ")
        elif count >= 3 and count < 9:
            user_menu_input = input(f"You appear to be really struggling here...if you want to see the menu again, plz just type, 'menu': ")
        elif count >= 9:
            user_menu_input = print(f"I'm going to play it safe and assume your ability to follow instructions is beyond hope. I'm out.")
            return
    
        count += 1
    
    if count >= 2:
        print(f"You appear to be...oh. You figured it out. Good job, i guess?")
        count = 0
    

    count = 0
    """

    #Execute user's choice

    """ 
    if user_menu_input.lower() == "choose 3":
        answer_three()
    elif user_menu_input.lower() == "pick range":
        pick_range()
    elif user_menu_input.lower() == "menu":
        menu()
    elif user_menu_input.lower() == "quit" or "stop":
        print(f"I'm relieved. I was ready to be done with you too tbh")
        return
    else:
        print("somethine weird must've happened...check your code.")
    """



def answer_three():

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

    reset = input(f"Do you want to quit? [Y/N]: ")

    if reset.lower() == "y":
        console = Console()
        console.clear() 
    else:
        print("well, I'm not equipped at the moment to do that. By anyway.")

def pick_range(num):

    num = int(num)
    #gen ran nums within range based on user's input
    user_num_list = []
    user_list_answer = {}

    # num = int(input(f"Enter a number range you would like to pracice: "))

    for i in range(num, num+9):
        user_num_list.append(i)
    random.shuffle(user_num_list)

    #generate the answer key
    for number in user_num_list:
        PAO_phrase = []
        str_number = str(number)
        triplicated_number = str_number+str_number+str_number 
        user_list_answer[number] = gen_phrase(triplicated_number)


    #loop through each item of the user_num_list, get PAO answer for each item
    for number in user_num_list: 
        rprint(f"Enter the correct PAO phrase for {number}: ")
        user_answer = collect_user_input(number)

        if user_answer[0] == "hint":
            choose_1_or_2 = random.randint(1,2)
            hint = user_list_answer[number][choose_1_or_2]
            rprint(f"[bright_cyan]Hint, huh? Well well, looks like [italic]somebody[/italic] needs to study more.\nHere's the hint for little precious: [yellow]'{hint}'[/yellow][/bright_cyan]")
            new_input = collect_user_input(number)
            user_answer = new_input
            
        elif user_answer[0] in ["stop", "end", "exit", "quit"]:
            rprint(f"[orange]Fine. I'll stop. I thought we...*sniff*...we were on good terms :'([/orange]")
            return

        result = check_answer(user_answer, user_list_answer[number])

        #check if user_answer is correct

        if result:
            rprint(f"[green]Correct![/green]") # add in "_#_ Remaining" after each message
        else:
            rprint(f"[yellow]I'm sorry, that's incorrect. The correct phrase is {user_list_answer[number]}")

        #to add: allow user to type 'hint' for O or A hint.
        #to add: allow user to type 'quit' or 'stop' to end the run 