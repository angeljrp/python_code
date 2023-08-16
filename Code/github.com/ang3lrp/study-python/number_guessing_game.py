import random 

def game(level,num1,num2):
    print(f'Level {level}')
    print(num1)
    print(num2)
    play_number = input("Insert your number ")
    n = random.randint(num1,num2)
    print(n)
    if int(play_number) == n:
        input("you leveled up!")
        num2 = num2 +1
        level = level +1
        game(level,num1,num2)
    elif int(play_number) != n:
        print(f'sorry, you missed the actual number is {n}')
        input("You will have to restart")
        game(1,1,1)

print("Hello welcome to my number guessing game, hope you enjoy")
toPlay = input("Would you like to play my game, type (yes) to start: ")
if toPlay == "yes":
    print("In this game tere will be a serius of levels were you will hav eto guess the number the higer level the wider the range of where the number can come, so, be prepared")
    print("you will start with a range of 1-1, then with a range of 1-2, the 1-3, and it keeps going on")
    input("Let's start!")
    game(1,1,1)