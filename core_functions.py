from database import PAO_dict_list
from database import singles
from ascii import *
import random
from rich import print as rprint
from rich import pretty 

def is_odd_length(num_list):
    
    if len(str(num_list)) % 2 != 0:
        return True
    # else:
    #     return False

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
    
    # NEVER DIVIDE BY ZEROOOOO!!!!!
    last_digit = int(num) % 10
    if num != 0:
        shortened_num = num // 10
    else:
        shortened_num = 0
        last_digit = 0
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

def gen_ran_num(number):

    number_list = []
   
    for i in range(number):
        ran_digit = random.randint(0,9) 
        number_list.append(ran_digit)

    # 0s will get dropped if first in the sequence
    # while len(number_list) != number:
    #     number_list.append(random.randint(0,9))
    
    num_result = str(''.join(map(str, number_list)))

    return num_result
   
def gen_main_phrase(num_list):
    #this function generates phrases for odd-number length numbers without the last digit.
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
    #for odd-length numbers, this takes the last digit and returns the "loner" word
    word = singles[num]
    return word

# gen_phrase is calling between gen_main_phrase() and itself somewhat redundantly...
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

def gen_PAO_phrase(num):
    #generates a PAO answer phrase from a single or pair of digits. i.e. 36 => 'match', 'lighting', 'campfire'

    num = int(num)
    PAO_phrase = []
    for word in range(3):
        PAO_phrase.append(PAO_dict_list[num][word])
    
    return PAO_phrase

def display_numbers_formatted(num_list):
    #takes numbers like [98, 16, 0] and displays it as 98-16-00, or for odd lengths, 98-16-00-1
    #note: input is a list of numbers, not just a plain integer
    pass
    # for num in num_list:

def gen_shuffled_PAO_phrase(number_of_words):

    #
    
    num = gen_ran_num(number_of_words*2)
    print(f"num: {num}")
    answer = gen_phrase(num)
    # print(f"num_list: {num}\nanswer_key: {answer}")
    return
    num_list = []
    answer_key = {}

    for num in range(number_of_words):
        num_list.append(gen_ran_num(2))

    for item in num_list:
        answer_key[item] = gen_PAO_phrase(item)

    print(f"num_list: {num_list}\nanswer_key: {answer_key}")

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
    # print("\n")

def reset_round():
    None

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