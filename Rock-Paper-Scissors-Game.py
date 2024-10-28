import random

print("Rock-Paper-Scissors-Game")
list = ["rock","paper","scis"]

pc_score = 0
your_score = 0



while True:
    choice_of_pc = random.choice(list)
    your_choice = input ("Choose one of the rock paper scis : ")
    print(f"choice of pc : {choice_of_pc}")
 

    if your_choice == choice_of_pc:
        print("draw")

    if your_choice == "rock":
        if choice_of_pc == "scis":
            print("You Won.")
            your_score += 1
            print(f"your score: {your_score}    pc score: {pc_score} ")
        elif choice_of_pc == "paper":
            print("You Lose.")
            pc_score += 1
            print(f"your score: {your_score}    pc score: {pc_score}")

    if your_choice == "paper":
        if choice_of_pc == "rock":
            print("You Won.")
            your_score += 1
            print(f"your score: {your_score}    pc score: {pc_score}")
        elif choice_of_pc == "scis":
            print("You Lose.")
            pc_score += 1
            print(f"your score: {your_score}    pc score: {pc_score}") 

    if your_choice == "scis":
        if choice_of_pc == "paper":
            print("You Won.")
            your_score += 1
            print(f"your score: {your_score}    pc score: {pc_score}")
        elif choice_of_pc == "rock":
            print("You Lose.")
            pc_score += 1
            print(f"your score: {your_score}    pc score: {pc_score}")

    if your_score == 3 or pc_score == 3:
        break

if your_score > pc_score:
    print("YOU WON")

else:
    print("YOU LOSE")