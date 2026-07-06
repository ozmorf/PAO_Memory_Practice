from core_functions import *
from ascii import *
from game_logic import *
from constants import *

import random
from rich import print as rprint
from rich.console import Console

class GameMode:
    #data: ascii_title, instructions, menu_items, interactive_loop
    #behaviors: display menu, get user input, gameplay, gameplay_interactive_loop, clear console
    def __init__(self, ascii_title, instructions, menu_items):
        self.ascii_title = ascii_title
        self.instructions = instructions
        self.menu_items = menu_items

    def display_ascii_title(self):
        rprint(f"[bold cyan]{self.ascii_title}[/bold cyan]\n")
    
    def display_instructions(self):
        rprint(f"[bold white]{self.instructions}[/bold white]\n")

    def display_menu(self):
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
     
    def run(self):
        self.display_ascii_title()
        self.display_instructions()      
        self.display_menu()

        user_choice = self.get_user_input()
        next_mode = self.gameplay(user_choice)

        if next_mode:
            self.reset_round()
            Console().clear()
            return next_mode.run()
        else:
            print(f"next_mode not initatied: {next_mode}")
            return

class Menu(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = major_PAO, 
            instructions = "Welcome to Major PAO Practice! Choose an item from the menu by typing it below:\n ", 
            menu_items = ["tutorial", "convert numbers", "convert phrases", "pick range", "quit"]
            )
    def gameplay(self, user_choice):
        Console().clear()
        if get_valid_user_input(user_choice, self.menu_items):
            user_choice = user_choice.lower()
            if user_choice == "convert numbers":
                return Convert_Numbers_Menu()
            elif user_choice == "convert phrases":
                return Convert_Phrases_Menu()
            elif user_choice == "pick range":
                return PickRangeMenu()
            elif user_choice == "menu":
                return Menu()
            elif user_choice == "quit" or "stop":
                print(f"I'm relieved. I was ready to be done with you too tbh")
            else:
                print("somethine weird must've happened...check your code.")
        else:
            print(f"Somethine must've happened, this is the else block...")

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
            menu_items = list(ASCII_MAP.keys())
            )
    
    def gameplay(self, choice):
        choice = int(choice)
        
        if choice in ASCII_MAP:

            console = Console()
            console.clear()

            return PickRangeSession(choice) 
        
        if choice == "menu" or "quit":
            return Menu()

        else:
            print("else block of gameplay in PickRangeMenu...")

class PickRangeSession(GameMode):
    def __init__(self, choice):
        self.choice = choice

        super().__init__(
            ascii_title = ASCII_MAP[choice],
            instructions = "Type your answer below, comma seperated. \nAt anytime, you can select from the following options: \n",
            menu_items = ["hint", "menu"], 
            )
        
    def run(self):
        Console().clear()
        rprint(f"[cyan]{self.ascii_title}[/cyan]")
        super().display_instructions()
        super().display_menu()

        user_input = pick_range(self.choice)

        if user_input == 'menu':
            Console().clear()
            return Menu().run()
        
        elif user_input == 'done': #pick_range() returns 'done' when finished
            return  PlayAgain(lambda: PickRangeMenu().run()).run() 

class Convert_Numbers_Menu(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = ascii_convert_numbers, 
            instructions = "Choose a difficulty from the following options: ", 
            menu_items = ["easy", "medium", "difficult", "menu"]
            )  
        
    def gameplay(self, choice):
        # if choice in get_valid_user_input(choice, self.menu_items):
        if choice == "easy":
            return Convert_Numbers_Session("easy")
        if choice == "medium":
            return Convert_Numbers_Session("medium")
        if choice == "difficult":
            return Convert_Numbers_Session("hard")
        if choice == "custom":
            return Convert_Numbers_Session("custom")
        if choice == "menu":
            return Menu()

class Convert_Numbers_Session(GameMode):
    def __init__(self, difficulty):
        self.difficulty = difficulty

        super().__init__(
            ascii_title =  CONVERT_NUMBERS_MAP[difficulty],
            instructions = "Convert each number into the correct phrase by typing your answer (comma seperated)", 
            menu_items = ["hint", "menu", "quit"]
            )  
        
    def gameplay(self, choice=None):
        convert_numbers(self.difficulty)
        return PlayAgain(lambda: Convert_Numbers_Menu().run())
    
    def run(self):
        self.display_ascii_title()
        self.display_instructions()
        self.display_menu()

        self.gameplay()

        return PlayAgain(lambda: Convert_Numbers_Menu().run()).run()

class Convert_Phrases_Menu(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = ascii_convert_phrases,
            instructions = "Choose a difficulty from the following options",
            menu_items = ["easy", "medium", "hard", "custom"]
            )

    def gameplay(self, difficulty):
        if difficulty == "easy":
            return Convert_Phrases_Session("easy") # convert_phrases("easy")
        elif difficulty == "medium":
            return Convert_Phrases_Session("medium")
        elif difficulty == "hard":
            return Convert_Phrases_Session("hard")
        elif difficulty == "custom":
            return Convert_Phrases_Session("custom")

class Convert_Phrases_Session(GameMode):
    def __init__(self, difficulty):
        self.difficulty = difficulty

        super().__init__(
            ascii_title = CONVERT_PHRASES_MAP[difficulty],
            instructions = "Convert each phrase into the correct number by typing your answer (comma seperated)",
            menu_items = ["menu", "hint", "quit"]
        )
            
    def gameplay(self, choice=None):
        convert_phrases(self.difficulty)
        return PlayAgain(lambda: Convert_Phrases_Menu())
    
    def run(self):
        self.display_ascii_title()
        self.display_instructions()
        self.display_menu()

        self.gameplay()

        return PlayAgain(lambda: Convert_Numbers_Menu().run()).run()

class PlayAgain(GameMode):
    def __init__(self, previous_mode_fn):
        self.previous_mode_fn = previous_mode_fn

        super().__init__(
            ascii_title = play_again, 
            instructions = "Do you want to play again, or return to the menu?\n", 
            menu_items = ["play again", "menu"]
        )

    def gameplay(self, choice):
        if choice.lower() == "play again":
            Console().clear()
            return self.previous_mode_fn()
        elif choice.lower() == "menu":
            Console().clear()
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
Menu().run()
# Convert_Numbers_Session("easy").run()


        




