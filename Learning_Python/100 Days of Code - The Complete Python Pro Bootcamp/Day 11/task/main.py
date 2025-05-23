import random

from art import logo

def deal_card():
    """" Return a random card from a deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """" Take a list of cards and return the score calculated from the cards """
    if sum(cards) == 21 and len(cards) == 2 :
        return 0

    if sum(cards) > 21  and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, com_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == com_score:
        return "draw"
    elif com_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win, with a Blackjack"
    elif u_score > 21:
        return "you went over 21, you lose"
    elif com_score > 21:
        return "Opponent went over 21, you win"
    elif u_score > com_score:
        return "You win"
    else:
        return "You lose"



def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card : {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]} score {computer_score}")


        if user_cards == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input("want to draw another card, 'y' or 'n' ").lower()
            if draw_card == 'y' :
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

        print(f"Your final hand : {user_cards}, final score: {user_score}")
        print(f"Computer's final hand:: {computer_cards} final score {computer_score}")
        print(compare(user_score, computer_score))


        should_continue = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

        if should_continue == "n":
            is_game_over = True
        elif should_continue == "y":
            print("\n" * 20)
            print(logo)
            blackjack()

blackjack()
