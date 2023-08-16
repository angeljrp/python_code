#here i introduce to the game and ask if he/her wants to play 
print("Hello!, welcome to my anime quiz.")

play = input("Do you want to play? ")

if play == "yes":
        input("Great then let's get started.")
elif play == "no":
        input("Okay bye, to exit press the enter buton.")
        exit()
else:  exit()
#my variable for the score
score = 0
#here is my array for the correct answers from 0-4
correct_answers = ["c", "a" ,"b", "d" ,"c"]
#here i start asking my questions and doing the scoring math afrter each one of them
input("First question:")
print("How many tails does Kurama has")
print("a. 10, b. 13 ,c. 9, d. 7")
question1 = correct_answers[0]
answer1 = input()

if answer1 == question1:
    score = score + 1
else: score = score - 0.5

input("Second question:")
print("To what series does Killua belong")
print("a. Hunter,X,Hunter, b. The Shamang king, c. Demon Slayer, d. Saiki K.")
question2 = correct_answers[1]
answer2 = input()

if answer2 == question2:
    score = score + 1
else: score = score - 0.5

input("Third question:")
print("How many times does Keita rejects Tendo about joining the 'Gamers!' club")
print("a. 1, b. 2, c. 3, d. 5")
question3 = correct_answers[2]
answer3 = input()

if answer3 == question3:
    score = score + 1
else: score = score - 0.5

input("Fourth question:")
print("How is it called the gender of anime that it involves in the MC being taken to another world")
print("a. shounen, b. josei, c. shonen, d. isekai")
question4 = correct_answers[3]
answer4 = input()

if answer4 == question4:
    score = score + 1
else: score = score - 0.5

input("Fifth and final question(for now):")
print("How many different forms of super saiyans does goku have (canon and non-canon)")
print("a. 17, b. 19, c. 21, d. 23")
question5 = correct_answers[4]
answer5 = input()

if answer5 == question5:
    score = score + 1
else: score = score - 0.5

input("You have finished all the questions, It's time to see your score.")
#this is my variable to tell the user the percent of his/her score
score_percent = (score/5)*100
#here i tell the player what was it's score
if score <= 1:
    input(f'You got {score} out of 5 that\'s a {score_percent}')
    input("You need to study more")
elif score == 2:
    input(f'You got {score} out of 5 that\'s a {score_percent}')
    input("If you are dad, then this is a really good score")
elif score > 2 and score <= 4:
    input(f'You got {score} out of 5 that\'s a {score_percent}')
    input("Great job!")
elif score == 5:
    input(f'You got {score} out of 5 that\'s a {score_percent}')
    input("You must be otaku, a cheater or the creator of the quiz")