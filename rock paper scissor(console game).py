import random

human = ""
computer = ""
# check if human is the scorer
def scorer():
    # r>s, p>r, s>p
    if (
        (human == "r" and computer == "s")
        or (human == "p" and computer == "r")
        or (human == "s" and computer == "p")
    ):
        return True
    elif human==computer:
        return "tie"
    else:
        return False



print(scorer())

def play(high_score):
    human_score = 0
    computer_score = 0

    while human_score != high_score and computer_score != high_score:
        human = input("'r' for rock, 'p' for paper, 's' for scissor: ")
        computer = random.choice(['r','p','s'])

        if scorer():
            human_score += 1
            print("HUMAN!")
            print(f"computer - {computer}")
            print(f"human = {human_score}, computer = {computer_score}")
        
        elif scorer()=="tie":
            print("tie")
            print(f"computer - {computer}")
        else:
            computer_score += 1
            print(f"COMPUTER!")
            print(f"computer - {computer}")
            print(f"human = {human_score}, computer = {computer_score}")

    if human_score == high_score:
        print("Human won! ")
    else:
        print("Computer won! ")

    print(f"final score: human = {human_score}, computer = {computer_score}")


play(5)
