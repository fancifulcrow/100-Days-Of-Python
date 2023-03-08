logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________
                       .-------------.
                      /_______________
'''

bid_list = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0;
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid amount of {highest_bid}")


print(logo)
more_bids = True
while more_bids:
    name = input("What is your name?:")
    bid = int(input("How much are you bidding in dolllars: $"))
    bid_list[name] = bid

    should_continue = input("Is there anyone else who wants to bid? 'yes' or 'no'").lower()
    if should_continue == "no":
        more_bids = False
        find_highest_bidder(bid_list)
