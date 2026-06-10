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
    
    def display_gameplay_menu(self):
        pass


    def reset_round(self):
        console = Console()
        console.clear() 
        # if y_n_menu:
        #     return Menu()
        # else:
        #     print("you said no.")
        #     return
        
    def run(self):
        self.display_ascii_title()
        self.display_instructions()
        self.display_menu()

        user_choice = self.get_user_input()
        next_mode = self.gameplay(user_choice)

        if next_mode:
            print(f"next_mode being triggered: {next_mode}")
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
            menu_items = ["choose 3", "pick range", "menu", "quit"],
            )
    def gameplay(self, user_choice):
        #input validation:
        if get_valid_user_input(user_choice, self.menu_items):
            if user_choice == "choose 3":
                return Choose_3
            elif user_choice == "pick range":
                return PickRange()
            elif user_choice == "menu":
                return Menu()
            elif user_choice == "quit" or "stop":
                #print(f"I'm relieved. I was ready to be done with you too tbh")
                return Goodbye()
            else:
                print("somethine weird must've happened...check your code.")
        else:
            print(f"Somethine must've happened, this is the else block...")
            # menu()

class PickRange(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = ascii_pick_range,
            instructions = "Pick a range from the following options:\n(you can also type 'hint', 'stop', or 'quit' at any time)\n",
            menu_items = [i for i in range(0, 91, 10)]
            )
    
    def gameplay(self, choice):
        # print("before pick range")
        choice = int(choice)

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
        
        if choice in menu_items:
            index = menu_items.index(choice)

            console = Console()
            console.clear() 

            rprint(f"[cyan]{ascii_nums[index]}[/cyan]")
        else:
            print("You didn't do what you were supposed to...")

            # rprint(f"[bold]Hint: you can also type 'hint', or 'stop', or quit.")
        
        pick_range(choice) #focus here...
        print("after pick range")

class Choose_3(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = choose_3, 
            instructions = "Choose 3 instructions here...", 
            menu_items = ["item 1", "item 2", "item 3..."]
            )  
    def gameplay(self, choice):
        answer_three()

class Goodbye(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = goodbye_question, 
            instructions = "Confirm quit? [y/n]", 
            menu_items = ["y", "n", "menu"]
            )
    def gameplay(self, choice):
            
        response = get_valid_user_input(choice, self.menu_items).lower()
        
        if response == 'y':
            return
        else:
            return Menu()

display_menu_mode = Menu()
display_menu_mode.run()

# pick_range_mode = PickRange()
# pick_range_mode.run()

# pick_range_mode = PickRange()


        




