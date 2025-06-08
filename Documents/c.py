for i in range(3):
    import random
    user_choice = input("enter your choice (rock, paper, or scissors): ")
    outcomes = ["rock", "paper", "scissors"]
    computer_choice = random.choice(outcomes)
    scores = []
    if computer_choice == user_choice:
        continue
    elif computer_choice == "scissors" and user_choice == "rock":
        scores.append("user:1")
    elif computer_choice == "rock" and user_choice == "paper":
        scores.append("user:1")
    elif computer_choice == "rock" and user_choice == "scissors":
        scores.append("computer:1")
    elif computer_choice == "paper" and user_choice == "scissors":
        scores.append("user:1")
    elif computer_choice == "paper" and user_choice == "rock":
        scores.append("computer:1")
    elif computer_choice == "scissors" and user_choice == "paper":
        scores.append("computer:1")
if scores.count("computer:1") > scores.count("user:1"):
    print("computer won!")
if scores.count("computer:1") < scores.count("user:1"):
    print("you won!")