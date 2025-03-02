import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score > 21:
        return "Lose. You went over"
    elif c_score > 21:
        return "You win. Opponent went over."
    elif u_score == 0:
        return "Win with blackjack"
    elif c_score == 0:
        return "Lose. Opponent got blackjack"
    elif u_score > c_score:
        return "You win"
    else:
        return "Opponent win"

def play_game():
    print(logo)
    user_card = []
    computer_card = []
    user_score = -1
    computer_score = -1

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    is_game_over = True

    while is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your card {user_card}, Current score: {user_score}")
        print(f"Computer's first card {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = False
        else:
            user_should_continue = input("Do you add more card? Enter 'y' for yes and 'n' for no: ")

            if user_should_continue == "y":
                user_card.append(deal_card())
            else:
                is_game_over = False

    while computer_score != 0 and computer_score < 17 :
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final card {user_card}, Your final score: {user_score}")
    print(f"Computer final card {computer_card}, Computer final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
    print("\n" * 20)







