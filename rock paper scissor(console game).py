# rock paper scissor game
# by: Shoumik Acharya
# Human v/s Computer

import random

# check the scorer
# r for rock, p for paper, s for scissor
def scorer(h, c):
    # r>s, p>r, s>p
    if (h == "r" and c == "s") or (h == "p" and c == "r") or (h == "s" and c == "p"):
        return "h"
    elif h == c:
        return "tie"
    elif (c == "r" and h == "s") or (c == "p" and h == "r") or (c == "s" and h == "p"):
        return "c"


def play(high_score):
    human_score = 0
    computer_score = 0

    while human_score != high_score and computer_score != high_score:
        human = input("'r' for rock, 'p' for paper, 's' for scissor: ")  # Human input
        computer = random.choice(["r", "p", "s"])  # computer input

        if scorer(human, computer) == "h":
            print("YOU!")
            print(f"computer - {computer}")
            human_score += 1
            print(f"your score - {human_score}, computer score - {computer_score}")
            print("\n")

        elif scorer(human, computer) == "c":
            print("COMPUTER!")
            print(f"computer - {computer}")
            computer_score += 1
            print(f"your score - {human_score}, computer score - {computer_score}")
            print("\n")

        elif scorer(human, computer) == "tie":
            print("tie")
            print(f"computer - {computer}")
            print(f"your score - {human_score}, computer score - {computer_score}")
            print("\n")

    if human_score == high_score:
        print("You won!")
    else:
        print("Computer won!")


play(7)
