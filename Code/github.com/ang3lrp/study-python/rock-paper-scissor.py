import random
max_score = 0

def game(max_score):
    values = ["rock", "paper", "scissors"]
    pc_choice = random.choice(values)
    player_value = input("Choose: rock, paper or scissors ")

    if pc_choice == player_value:
       print("You choose " + player_value)
       print("the pc chooses " + pc_choice)
       input("It's a tie")
       restart = input("do you want to try again? (yes or no) ")
       if restart == "yes":
          game(max_score)
       else: exit()
    elif pc_choice == "rock" and player_value == "paper" or pc_choice == "paper" and player_value == "scissors" or pc_choice == "scissors" and player_value == "rock":
       print("You choose " + player_value)
       print("the pc chooses " + pc_choice)
       input("You won")
       max_score = max_score + 10
       restart = input("do you want to try again? (yes or no) ")
       if restart == "yes":
          game(max_score)
       else: exit()
    elif pc_choice == "rock" and player_value == "scissors" or pc_choice == "paper" and player_value == "rock" or pc_choice == "scissors" and player_value == "paper":
       print("You choose " + player_value)
       print("the pc chooses " + pc_choice)
       input("You lose")
       print(f'your max score was {max_score}')
       restart = input("do you want to try again? (yes or no) ")
       if restart == "yes":
          game(max_score)
       else: exit()
game(max_score)