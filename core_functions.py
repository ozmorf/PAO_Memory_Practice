from database import PAO_dict_list
from database import singles
from ascii import *
import random
from rich import print as rprint
from rich import pretty 

# pretty.install()

def gen_ran_length():

    #is this even useful? Will see...
    length = random.randint(1,12)
    return length

def is_odd_length(num_list):
    
    if len(str(num_list)) % 2 != 0:
        return True
    else:
        return False

def seperate_last_digit(num):
    last_digit = int(num) % 10
    shortened_num = num // 10
    return [shortened_num, last_digit]
    
    #add clause to prohibit doing this with an integer of even length?

def pair_digits(num): 
    # is this even used? I think this code is duplicated in gen_phrase() or gen_main_phrase()...
    paired_digits = []
    num_string = str(num)

    for i in range(0, len(num_string), 2):
        paired_digits.append(int(num_string[i:i+2]))

    return paired_digits
    # return [int(num_string[i:i+2]) for i in range (0, len(num), 2)]

def gen_ran_num_list(number):

    if number == None:
        number = random.randint(0,16)
    else:
        number_list = []
        #loop over list, gen num sequence and phrase
        for i in range(number):
            ran_digit = random.randint(0,9) #add a catch if this number isn't in the proper range, or to check how many items are in the data source
            number_list.append(ran_digit)
    
    number = int(''.join(map(str, number_list)))

    return number
   
def gen_main_phrase(num_list):

    phrase = []
    count = 0

    num_string = str(num_list)
    paired_numbers = []

    for i in range(0, len(str(num_list)), 2):
            #digit pair is actually the index...we want the digits from the integer instead.
            paired_numbers.append(num_string[i:i+2])

    for number in paired_numbers:
        phrase.append(PAO_dict_list[int(number)][count])
        count += 1
        if count > 2:
            count = 0

    return phrase

def gen_lonely_word(num):
    word = singles[num]
    return word

# gen_phrase is calling between gen_main_phrase() and itself someewhat redundantly...
def gen_phrase(num_list):
    #add a "catch" if the input is a list instead of int
    phrase = []

    if is_odd_length(num_list):
        main_number, loner = seperate_last_digit(num_list)
        phrase.extend(gen_phrase(main_number))
        phrase.append(gen_lonely_word(loner))
        return phrase
    else:
        phrase.extend(gen_main_phrase(num_list))
        return phrase

def collect_user_input(number):

    user_input = input(f"Your response (comma seperated): ")
    #user_answer = user_input.split(",")
    user_answer = [item.strip() for item in user_input.split(",")]

    return user_answer

    #seperate user answer by commas, and store each item in a list

def check_valid_input(user_input, valid_choices):
    if user_input in valid_choices:
        return True


def check_answer(user_input, answer):

    user_input_lowercase = []
    answer_lowercase = [] #To do: the database should already be lowercase. Homework: do it...without Chat GPT's help. 

    for item in user_input:
        user_input_lowercase.append(item.lower())
    for item in answer:
       answer_lowercase.append(item.lower()) 
      
    return user_input_lowercase == answer_lowercase

def display_welcome_sequence():
    rprint(f"[cyan]{major_PAO}[/cyan]")
    rprint(f"[bold]Welcome to Major PAO Practice! Choose an item from the menu by typing it below: [/bold] ")
    rprint(f"[cyan]{menu_word}")

def display_menu(menu):
    
    for item in menu:
        rprint(f"[cyan]-{item}[/cyan]")
    print("\n")