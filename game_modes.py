from core_functions import *
from ascii import *
from game_logic import *
from constants import ASCII_MAP

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
        rprint(f"[cyan]{self.ascii_title}[/cyan]\n")
    
    def display_instructions(self):
        rprint(f"[bold white]{self.instructions}[/bold white]")

    def display_menu(self):
        #homework: print number for each display_menu item, and allow user to pick number instead of typing the name of the mode
        for item in self.menu_items:
            rprint(f"[cyan]- {item}[/cyan]")
        rprint("")
    
    def get_user_input(self):

        user_input = input(">> ")
        count = 0

        while user_input not in str(self.menu_items):
                
            if count < 2:
                user_input = input("That response is not in my data banks. Please type a valid response: ")
            elif count >= 3 and count < 9:
                user_input = input(f"You appear to be really struggling here...if you want to see the menu again, plz just type, 'menu': ")
            elif count >= 9:
                user_input = print(f"I'm going to play it safe and assume your ability to follow instructions is beyond hope. I'm out.")
                return False
        
            count += 1


        if count >= 2:
            print(f"You appear to be...oh. You figured it out. Good job, i guess?")

        return user_input             

    def gameplay(self, user_choice):
        raise NotImplementedError

    def reset_round(self):
        Console().clear()
        # console = Console()
        # console.clear() 
        
    def run(self):
        self.display_ascii_title()
        self.display_instructions()
        self.display_menu()

        user_choice = self.get_user_input()
        next_mode = self.gameplay(user_choice)

        if next_mode:
            self.reset_round()
            next_mode.run()
        else:
            print(f"Next mode else block. {next_mode}")
            pass # self.clear_console()

        self.gameplay(user_choice)
        self.reset_round()

class Menu(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = major_PAO, 
            instructions = "Welcome to Major PAO Practice! Choose an item from the menu by typing it below:\n ", 
            menu_items = ["tutorial", "choose 3", "pick range", "quit"]
            )
    def gameplay(self, user_choice):
        if get_valid_user_input(user_choice, self.menu_items):
            if user_choice == "choose 3":
                return Choose_3
            elif user_choice == "pick range":
                return PickRangeMenu()
            elif user_choice == "menu":
                return Menu()
            elif user_choice == "quit" or "stop":
                print(f"I'm relieved. I was ready to be done with you too tbh")
                # return Goodbye()
            else:
                print("somethine weird must've happened...check your code.")
        else:
            print(f"Somethine must've happened, this is the else block...")
            # menu()

class Tutorial(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = ascii_tutorial, 
            instructions = "What in the world is Major PAO? Why do people learn this memory system?", 
            menu_items = ["menu item placeholder..."],
            )
    def gameplay():
        print(you_win)

class PickRangeMenu(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = ascii_pick_range,
            instructions = "Pick a range from the following options:\n(you can also type 'hint', 'stop', or 'quit' at any time)\n",
            menu_items = list(ASCII_MAP.keys()) #[i for i in range(0, 91, 10)]
            )
    
    def gameplay(self, choice):
        
        choice = int(choice)

        # ascii_nums = [
        #     range_zeroes_small,
        #     range_tens_small,
        #     range_twenties_small,
        #     range_thirties_small,
        #     range_forties_small,
        #     range_fifties_small,
        #     range_sixties_small,
        #     range_seventies_small,
        #     range_eighties_small,
        #     range_nineties_small,
        #     ]
        # menu_items = [i for i in range(0, 91, 10)]
        
        if choice in ASCII_MAP:

            console = Console()
            console.clear()

            return PickRangeSession(choice) 

            # index = menu_items.index(choice)
            # range_session_ascii_title = ascii_nums[index]
            # rprint(f"[cyan]{ascii_nums[index]}[/cyan]")

        else:
            print("else block of gameplay in PickRangeMenu...")


class PickRangeSession(GameMode):
    def __init__(self, choice):
        self.choice = choice

        super().__init__(
            ascii_title = ASCII_MAP[choice],
            instructions = "Type your answer below, comma seperated. \nAt anytime, you can choose the following: \n",
            menu_items = ["hint", "quit"]
            )
        
    def run(self):
        Console().clear()
        rprint(f"[cyan]{self.ascii_title}[/cyan]")
        super().display_instructions()
        super().display_menu()
        pick_range(self.choice)
        PlayAgain().run()

class Choose_3(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = choose_3, 
            instructions = "Choose 3 instructions here...", 
            menu_items = ["item 1", "item 2", "item 3..."]
            )  
    def gameplay(self, choice):
        answer_three()

class PlayAgain(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = play_again, 
            instructions = "You can play again or go back to the menu?", 
            menu_items = ["play again", "menu"]
        )

    def gameplay(self, choice):
        print("gameplay of PlayAgain reached")
        if choice.lower() == "play again":
            print("you chose play again")
        elif choice.lower() == "menu":
            return Menu()

class Goodbye(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = goodbye_question, 
            instructions = "Confirm quit? [y/n]", 
            menu_items = ["quit", "menu (go back to menu)"]
            )
    def gameplay(self, choice):
            
        response = get_valid_user_input(choice, self.menu_items).lower()
        
        if response == 'y':
            return
        else:
            return Menu()
Console().clear()
display_menu_mode = Menu()
display_menu_mode.run()

# pick_range_mode = PickRangeMenu()
# pick_range_mode.run()

# pick_range_mode = PickRangeMenu()


        




