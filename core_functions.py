from database import PAO_dict_list
from database import singles
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
    number_list = []
    ran_digit_length = random.randint(0,16)
    #loop over list, gen num sequence and phrase
    for i in range(ran_digit_length):
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
    phrase = []

    if is_odd_length(num_list):
        main_number, loner = seperate_last_digit(num_list)
        phrase.extend(gen_phrase(main_number))
        phrase.append(gen_lonely_word(loner))
        return phrase
    else:
        phrase.extend(gen_main_phrase(num_list))
        return phrase
    
def collect_user_input():
    None

def check_answer():
    None
    
def unpack(dict):
    values = list(dict.values())
    print(values)
    for item in values:
        rprint("[green]values[/green]") 

def unpack_phrase(dict):
    a = list(phrase.values())
    print(f"Here's a {a}")
    just_values = a[0]
    P = just_values[0]
    A = just_values[1]
    O = just_values[2]
    rprint(f"[yellow]Phrase: {phrase} \na: {a} \nP: {P} \nA: {A} \nO: {O} [/yellow]")    

ran_num = gen_ran_length()
num_list = gen_ran_num_list(ran_num)
# num_list = 12345

rprint(f"[yellow]Program Starting...[/yellow]")
rprint(f"[blue]Number List:[/blue] {num_list}, [blue]Length:[/blue] {len(str((num_list)))}\n[blue]Phrase:[/blue] {gen_phrase(num_list)}")
