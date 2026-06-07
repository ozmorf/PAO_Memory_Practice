from ascii import *
from rich import print as rprint
from core_functions import *

def menu():
    menu_choices = ["choose 3", "practice range", "quit"]

    #welcome sequence
    rprint(f"[cyan]{major_PAO}[/cyan]")
    rprint(f"[bold]Welcome to Major PAO Practice! Choose an item from the menu by typing it below: [/bold] ")
    rprint(f"[cyan]{menu_word}")
    
    display_menu(menu_choices)

    user_menu_input = input(f"Type your response and hit enter: ")
    if check_valid_input(user_menu_input, menu_choices):
        print("valid input")
    else:
        print("not valid")


    # if user_menu_input not in menu_choices:
    #     rprint(f"I didn't recognize that input...please try again, or learn how to type.")
    #     user_menu_input = input(f"Let's try this again...choose from the menu below: ")
    #     display_menu
    # elif user_menu_input == "quit":
    #     rprint(f"oh...Okay. Bye, I guess.")
    # else:
    #     rprint(f"Good job, young one. You can follow instructions!")

    #Get user selection, execute function

    #Return to menu, repeat until quit
    
def display_menu(menu):
    
    for item in menu:
        rprint(f"[cyan]-{item}[/cyan]")
    print("\n")

menu()

