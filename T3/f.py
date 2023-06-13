import unittest


def add(a,b):
    
    return a + b

if __name__ == '__main__':
   
    a = int(input("n1 = "))
    b = int(input("n2 = "))
    print(add(a,b))


    
    



    
import random



    
def user():
    if __name__ == '__main__':
        while True:
        
            user = str(input("what is your name: "))
            if user.isdigit():
                print("invalid try again!")
            else:
                print(user)
                break
    
user()


def play_round():
    """
    Plays a single round of the game and returns the result.
    """
        
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    print(f"Computer chose: {computer_choice}")
    if user_choice.lower() == computer_choice:
        return "tie"
    elif user_choice.lower() == "rock":
        if computer_choice == "scissors":
            return "user"
        else:
            return "computer"
    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            return "user"
        else:
            return "computer"
    elif user_choice.lower() == "scissors":
        if computer_choice == "paper":
            return "user"
        else:
            return "computer"
    else:
        print("Invalid choice. Please try again.")
        
    if __name__ == '__main__':
        return play_round()

num_rounds = 0
user_wins = 0
computer_wins = 0
play_again = "y"
a = 4

if __name__ == '__main__':
    while play_again.lower() == "y":
        
            num_rounds += 1
            result = play_round()
            if result == "user":
                user_wins += 1
                print("You win!")
            elif result == "computer":
                computer_wins += 1
                print("Computer wins!")
            else:
                print("Tie game.")
            print(f"Rounds played: {num_rounds}")
            print(f"User wins: {user_wins}")
            print(f"Computer wins: {computer_wins}")
            play_again = input("Play another round? (y/n) ")
            
            

