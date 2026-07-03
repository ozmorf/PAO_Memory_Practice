from database import PAO_dict_list
from database import singles
from ascii import *
import random
from rich import print as rprint
from rich import pretty 

def is_odd_length(num_list):
    
    if len(str(num_list)) % 2 != 0:
        return True

def gen_ran_two_digit_num():

    num = []

    for i in range(2):
        ran_num = random.randint(0,9)
        num.append(ran_num)

    num_result = "".join(map(str, num))

    return num_result

def seperate_last_digit(num):
    #check if num is length of 1
    if len(str(num)) <= 1:
        shortened_num = num
        last_digit = num
        return [shortened_num, last_digit]
    
    # NEVER DIVIDE BY ZERO
    last_digit = int(num) % 10
    if num != 0:
        shortened_num = num // 10
    else:
        shortened_num = 0
        last_digit = 0
    return [shortened_num, last_digit]
 
    #add clause to prohibit doing this with an integer of even length?

def gen_ran_num(number):

    number_list = []
   
    for i in range(number):
        ran_digit = random.randint(0,9) 
        number_list.append(ran_digit)
    
    num_result = str(''.join(map(str, number_list)))

    return num_result
   
def gen_main_phrase(num_list):
    #this function generates phrases for odd-number length numbers without the last digit.
    phrase = []
    count = 0

    num_string = str(num_list)
    paired_numbers = []

    for i in range(0, len(str(num_list)), 2):
            paired_numbers.append(num_string[i:i+2])

    for number in paired_numbers:
        phrase.append(PAO_dict_list[int(number)][count])
        count += 1
        if count > 2:
            count = 0

    return phrase

def gen_lonely_word(num):
    #for odd-length numbers, this takes the last digit and returns the "loner" word
    word = singles[num]
    return word

def gen_phrase(num_list):
    phrase = []

    if is_odd_length(num_list):
        main_number, loner = seperate_last_digit(num_list)
        phrase.extend(gen_phrase(main_number))
        phrase.append(gen_lonely_word(loner))
        return phrase
    else:
        phrase.extend(gen_main_phrase(num_list))
        return phrase

def gen_PAO_phrase(num):
    #generates a PAO answer phrase from a single or pair of digits. i.e. 36 => 'match', 'lighting', 'campfire'

    num = int(num)
    PAO_phrase = []
    for word in range(3):
        PAO_phrase.append(PAO_dict_list[num][word])
    
    return PAO_phrase

def format_numbers(number):
    string = str(number)
    return "-".join(string[i:i+2] for i in range(0, len(string), 2))

def collect_user_input():

    user_input = input(f">> ")
    user_answer = [item.strip() for item in user_input.split(",")]

    return user_answer

def give_hint(answer_list):
    ran_index = random.randint(1, len(answer_list)-1)
    return answer_list[ran_index]

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

def display_menu(menu_list):
    
    for item in menu_list:
        rprint(f"[cyan]-{item}[/cyan]")

def get_valid_user_input(user_input, menu_choices):

    count = 0

    #get valid user_menu_input or quit
    while user_input.lower() not in menu_choices:
        print(f"user_input.lower...{user_input.lower()}")
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
    
    return user_input

#check if words are slightly misspelled

# print(gen_ran_two_digit_num())