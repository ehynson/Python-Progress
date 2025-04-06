# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

name = input("What is your name?: ")
bet = int(input("What is your bid?: $"))

bets = {name: bet}

keep_going = True
while keep_going:
    user_input = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if user_input == "yes":
        name = input("What is your name?: ")
        bet = int(input("What is your bid?: $"))

        bets[name] = bet

    elif user_input == "no":
        keep_going = False

        if bets:
            winner_name = ""
            winner_bet = ""
            highest_bid = -1

            for key in bets:
                if bets[key] > highest_bid:
                    highest_bid = bets[key]
                    winner_name = key
                    winner_bet = bets[key]

                print(f"The winner is {winner_name} with a bid of ${winner_bet}")
