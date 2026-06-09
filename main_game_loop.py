from ascii import *
from rich import print as rprint
from core_functions import *
from game_modes import *
import builtins

def menu():
    menu_choices = ["choose 3", "pick range", "menu", "quit"]

    #welcome sequence
    # display_welcome_sequence()
    # display_menu(menu_choices)

    user_menu_input = input(f"Type your response and hit enter: ")

    count = 0

    #get valid user_menu_input or quit
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

    #Execute user's choice
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
    

    #Get user selection, execute function

    #Return to menu, repeat until quit

menu()

