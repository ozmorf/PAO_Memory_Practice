from core_functions import *
import random
from rich import print as rprint
from ascii import *
from main_game_loop import *
from rich.console import Console

# console = Console()
# console.clear()

class GameMode:
    def __init__(self, ascii_title, instructions, menu):
        self.ascii_title = ascii_title
        self.instructions = instructions
        self.menu = menu

    def display_ascii_title(self):
        rprint(f"[cyan]{self.ascii_title}[/cyan]")
    
    def display_instructions(self):
        rprint(f"[bold white]{self.instructions}[/bold white]")

    def display_menu(self):
        for item in self.menu:
            rprint(f"[cyan]- {item}[/cyan]")

    def gameplay(self):
        pass

    def reset_round(self):
        pass
    
    def run(self):
        self.display_ascii_title()
        self.display_instructions()
        self.display_menu()

mode_menu = GameMode(
    ascii_title = menu_word,
    instructions = "Type your response and hit enter: ",
    menu = ["choose 3", "pick range", "menu", "quit"]
)

class Menu(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = "", 
            instructions = display_welcome_sequence(), 
            menu = ["choose 3", "pick range", "menu", "quit"]
            )
        def gameplay(self):
            menu()

class PracticeRange(GameMode):
    def __init__(self):
        super().__init__(
            ascii_title = ascii_pick_range,
            instructions = "Play to win!!",
            menu = ['item1', 'item2']
            )
    
    def gameplay(self):
        print("PracticeRange Running")

menu_mode = Menu()
menu_mode.run()
pick_range_mode = PracticeRange()





# sample_mode.run()
# mode_menu.run()

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
        
def pick_range():

    #gen ran nums within range based on user's input
    user_num_list = []
    user_list_answer = {}

    num = int(input(f"Enter a number range you would like to pracice: "))

    for i in builtins.range(num, num+9):
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



