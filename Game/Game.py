import os
import time
import pygame
import random

def clear():
    """Clear The Terminal"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Froggy():
    print("The game is being developed.")
    time.sleep(3)
def Twenty_one():

    CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    def deal_initial_cards():
        return random.choices(CARDS, k=2)

    def deal_card():
        return random.choice(CARDS)

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0  # Blackjack
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare_scores(user_score, computer_score):
        if user_score > 21 and computer_score > 21:
            return "\nYou went over. You lose 😤"
        if user_score == computer_score:
            return "\nDraw 🙃"
        elif computer_score == 0:
            return "\nLose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "\nWin with a Blackjack 😎"
        elif user_score > 21:
            return "\nYou went over. You lose 😭"
        elif computer_score > 21:
            return "\nOpponent went over. You win 😁"
        elif user_score > computer_score:
            return "\nYou win 😃"
        else:
            return "\nYou lose 😤"

    def play_game():
        clear()
        print("Starting Game........")
        user_cards = deal_initial_cards()
        computer_cards = deal_initial_cards()

        is_game_over = False
        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            time.sleep(3)

            print(f"\n\nYour cards are : ({", ".join(map(str, user_cards))}). current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                time.sleep(3)
                should_continue = input("\nGit anther card? Y/N : ").upper()
                if should_continue == 'Y':
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare_scores(user_score, computer_score))

        while input("Do you want to play a game of Blackjack? Y/N : ").upper() == 'Y':
            play_game()


    play_game()
    print("Thanks for playing!")


def Snake():
    print("The game is being developed.")
    time.sleep(3)
def main_menu():
    while True:
        clear()
        time.sleep(2)
        print("""Choose a Game To Start......
        
        
1. Froggy
2. Twenty One
3. Snake""")
        choice = input("---------\n").strip().lower()
        if choice in ['1', 'froggy']:
            clear()
            Froggy()
        elif choice in ['2', 'twenty one']:
            clear()
            Twenty_one()
        elif choice in ['3', 'snake']:
            clear()
            Snake()
        else:
            print("Invalid input. Please enter a valid choice...")
            time.sleep(2)

if __name__ == "__main__":
    main_menu()