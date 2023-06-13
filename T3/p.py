import random

import unittest
    


# def determine_winner(player1_choice, player2_choice):
#     # if player1_choice == player2_choice:
#     #     return "It is a tie!"
#     # elif (player1_choice == "rock" and player2_choice == "scissors") or \
#     #     (player1_choice == "paper" and player2_choice == "rock") or \
#     #         (player1_choice == "scissors" and player2_choice == "paper"):
                
#     #             return "Player 1 wins!"
    
#     if player1_choice() == player2_choice:
#         return "tie"
#     elif player1_choice() == "rock":
#         if player2_choice == "scissors":
#             return "Player 1 wins!"
#         else:
#             return "computer"
#     elif player1_choice() == "paper":
#         if player2_choice == "rock":
#             return "Player 1 wins!"
#         else:
#             return "computer"
#     elif player1_choice() == "scissors":
#         if player2_choice == "paper":
#             return "Player 1 wins!"
#         else:
#             return "computer"
#     else:
#         print("Invalid choice. Please try again.")        
    
# def determine_winner(player1_choice, player2_choice):
#     if player1_choice == player2_choice:
#         return "It is a tie!"
#     elif (player1_choice == "rock" and player2_choice == "scissors") or \
#         (player1_choice == "paper" and player2_choice == "rock") or \
#             (player1_choice == "scissors" and player2_choice == "paper"):
                
#                 return "Player 1 wins!"            
    


# t = 100
    

    
def play_game():
    choices = ["rock", "paper", "scissors"]
    player1_choice = input("pick: ")
    player2_choice = random.choice(choices)
    
    print(f"Player 1 chose {player1_choice}")
    print(f"Player 2 chose {player2_choice}")
    
    

# if __name__ == '__main__':
    play_game()
    
       
    # if player1_choice.lower() == player2_choice:
    #     return "tie"
    # elif player1_choice.lower() == "rock":
    #     if player2_choice == "scissors":
    #         return "Player 1 wins!"
    #     else:
    #         return "computer"
    # elif player1_choice.lower() == "paper":
    #     if player2_choice == "rock":
    #         return "Player 1 wins!"
    #     else:
    #         return "computer"
    # elif player1_choice.lower() == "scissors":
    #     if player2_choice == "paper":
    #         return "Player 1 wins!"
    #     else:
    #         return "computer"
    # else:
    #     print("Invalid choice. Please try again.")     
    
    # winner = determine_winner(player1_choice, player2_choice)
    # print(winner)
    # if __name__ == '__main__':



    # if player1_choice() == player2_choice:
    #     return "tie"
    # elif player1_choice() == "rock":
    #     if player2_choice == "scissors":
    #         return "Player 1 wins!"
    #     else:
    #         return "computer"
    # elif player1_choice() == "paper":
    #     if player2_choice == "rock":
    #         return "Player 1 wins!"
    #     else:
    #         return "computer"
    # elif player1_choice() == "scissors":
    #     if player2_choice == "paper":
    #         return "Player 1 wins!"
    #     else:
    #         return "computer"
    # else:
    #     print("Invalid choice. Please try again.") 

