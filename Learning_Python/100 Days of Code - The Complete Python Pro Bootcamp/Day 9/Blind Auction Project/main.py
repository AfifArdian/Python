from art import logo

print(logo)

bid_again = False

bids = {
    }
# cara mencetak nilai tertinggi tanpa menggunakan fungsi max
def find_highest_bidder(biggest_bids):
    winner = ""
    high_value = 0
    for bigger in biggest_bids:
        bid_amount = biggest_bids[bigger]
        if bid_amount > high_value:
            high_value = bid_amount
            winner = bigger
    print(f"The winner is {winner} with a bid of ${high_value}")


while not bid_again:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    price = int(input("what is your bid?: $ "))
    # TODO-2: Save data into dictionary {name: price}

    bids[name] = price

    # TODO-3: Whether if new bids need to be added
    # TODO-4: Compare bids in dictionary

    restart = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()


    if restart == "no":
        bid_again = True
        find_highest_bidder(bids)

    elif restart == "yes":
        print("\n" * 20)

