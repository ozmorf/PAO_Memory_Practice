from core_functions import *
import random
from rich import print as rprint

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

def practice_range():

    #gen ran nums within range based on user's input
    user_num_list = []
    user_list_answer = {}

    num = int(input(f"Enter a number range you would like to pracice: "))
    
    for i in range(num, num+9):
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
        result = check_answer(user_answer, user_list_answer[number])

        #check if user_answer is correct

        if result:
            rprint(f"[green]Correct![/green]")
        else:
            rprint(f"[yellow]I'm sorry, that's incorrect. The correct phrase is {user_list_answer[number]}")

        #to add: allow user to type 'hint' for O or A hint. 
        

    
    #prompt user for PAO for each num, check answer
    #User can ask for hint...
    #Loop through all the number
    #user can type 'stop' at any time to exit the practice
    #prompt 'would you like to do this number set again? [Y/N]:' at the end
    #report num of hints given

practice_range()

#Game modes to add:
#Practice a specific range, like 50s, or 10s. User must give correct PAO phrase. User can ask for a hint (output O or A)
#From phrase, give number
#answer 6, or 7, or ... use a timer 



























#menu:
#various modes
#each mode you can return to the menu, and choose a different mode until you quit
#make output pretty instead of brackets and quotes...
#basic mode: generate 3 numbers, and user has to enter in the corresponding correct PAO phrase

"""
#functions to build: Given [num, A, or O], recall the P ✅
#Give a range of numbers, and drill from that range
#Generate random numbers of ___ digits, convert to sentences ✅
#Read from google sheets --> figure out google sheets API
#Generate PAO phrases, and give back the number sequence
#Make a spaced repition algorithm 
#Does Anki have an API? What can it do?
"""
