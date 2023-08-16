is_alive = True

print("Hello welcome to choose your own adventure game")
play = input("do you wish to play (yes to continue) ")
if play != "yes":
    exit()

questions = ["You are in the jungle and you find yourself in front of an aztec temple. Do you dare to enter? (yes to continue) ",
             "You are in the entrance and the door is in front of you, there is a lever. Do you pull it (yes or no) ",
             "There are two behind number one there is a giant spider and behind the other there is something that looks like a sleeping dragon. Wich one do you choose (1 or 2) "
            ]

correct_answers = ["yes", "no", "2"]

def game(points, i, higher_score):
    question = questions[i]
    correct_answer = correct_answers[i]

    if i == questions.__len__:
        print("you have finished the dungeon")
        input(f'your score was {higher_score}')
        restart = input("want to try again? (yes to restart) ")
        if restart == "yes":
            game(0, 0, higher_score)
        else: exit()

    answer = input(question)

    if answer == correct_answer:
        i = i + 1
        points = points + 20
        if points > higher_score:
            higher_score = points
        else: higher_score = higher_score
        
        game(points, i, higher_score)
    elif answer != correct_answer:
        print("sorry you lost")
        input(f'your highest score was {higher_score}')
        restart = input("want to try again? (yes to restart) ")
        if restart == "yes":
            game(0, 0, higher_score)
        else: exit()

game(0,0,0)