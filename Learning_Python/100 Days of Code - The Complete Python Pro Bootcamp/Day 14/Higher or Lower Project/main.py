import random
from art import logo
from art import vs
from game_data import data

def take_random_data():
    data_random = random.choice(data)
    return data_random['name'], data_random['follower_count'], data_random['description'], data_random['country']



name1,follower1,description1,country1 = take_random_data()


user_score = 0
computer_score = 0
score = 0

is_game_over = False

print(logo)
while not is_game_over:
    name2, follower2, description2, country2 = take_random_data()
    print(f"Compare A: {name1}, a {description1}, from {country1}.")
    print(vs)
    print(f"Compare B: {name2}, a {description2}, from {country2}.")


    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == 'A':
        user_score = follower1
        computer_score = follower2
    else:
        user_score = follower2
        computer_score = follower1



    if user_score > computer_score:
        score += 1
        name1, follower1, description1, country1 = name2, follower2, description2, country2
        print("\n" * 20)
        print(logo)
        print(f"You're right! Current score {score}")
    elif user_score < computer_score:
        print("\n" * 20)
        print(f"Sorry,That's wrong. Final score {score}")
        is_game_over = True

