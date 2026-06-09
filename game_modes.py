from core_functions import *
from ascii import *
from game_logic import *
import random
from rich import print as rprint
from rich.console import Console

# console = Console()
# console.clear()

class GameMode:
    #data: ascii_title, instructions, menu_items
    #behaviors: display menu, get user input, gameplay, clear console
    def __init__(self, ascii_title, instructions, menu_items):
        self.ascii_title = ascii_title
        self.instructions = instructions
        self.menu_items = menu_items

    def display_ascii_title(self):
        rprint(f"[cyan]{self.ascii_title}[/cyan]")
    
    def display_instructions(self):
        rprint(f"[bold white]{self.instructions}[/bold white]")

    def display_menu(self):
        #homework: print number for each display_menu item, and allow user to pick number instead of typing the name of the mode
        for item in self.menu_items:
            rprint(f"[cyan]- {item}[/cyan]")
        rprint("")
    
    def get_user_input(self):
        #need input validation
        return input(">> ").lower()
    
    def display_additional_options(self, user_input):
        pass

    def gameplay(self):
        raise NotImplementedError

    def reset_round(self):
        console = Console()
        console.clear() 
        
    def run(self):
        self.display_ascii_title()
        self.display_instructions()
        self.display_menu()
        user_choice = self.get_user_input()
        self.display_additional_options(user_choice)
        self.gameplay(user_choice)
        self.reset_round()

class display_Menu(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = major_PAO, 
            instructions = "Welcome to Major PAO Practice! Choose an item from the menu by typing it below:\n ", 
            menu_items = ["choose 3", "pick range", "display_menu", "quit"]
            )
    def gameplay(self, user_choice):
        #input validation:
        if validate_user_input(user_choice, self.menu_items):
            if user_choice == "choose 3":
                print(f"answer 3: {answer_three}")
                answer_three()
            elif user_choice == "pick range":
                PickRange()
            elif user_choice == "menu":
                pass
                # menu()
            elif user_choice == "quit" or "stop":
                print(f"I'm relieved. I was ready to be done with you too tbh")
                return
            else:
                print("somethine weird must've happened...check your code.")
        else:
            print(f"Somethine must've happened, this is the else block...")
            # menu()

class PickRange(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = ascii_pick_range,
            instructions = "Pick a range from the following options:\n ",
            menu_items = [i for i in range(0, 91, 10)]
            )
    
    def gameplay(self, choice):
        pick_range(choice)

    def display_additional_options(self, user_choice):

        ascii_nums = [
            range_zeroes_small,
            range_tens_small,
            range_twenties_small,
            range_thirties_small,
            range_forties_small,
            range_fifties_small,
            range_sixties_small,
            range_seventies_small,
            range_eighties_small,
            range_nineties_small,
            ]
        menu_items = [i for i in range(0, 91, 10)]
        
        choice = int(user_choice)
        
        if choice in menu_items:
            index = menu_items.index(choice)
            console = Console()
            console.clear() 
            rprint(f"[cyan]{ascii_nums[index]}[/cyan]")
        else:
            print("You didn't do what you were supposed to...")

        

# display_menu_mode = display_Menu()
# display_menu_mode.run()

pick_range_mode = PickRange()
pick_range_mode.run()
# pick_range_mode = PickRange()


        




