import random

from art import logo, vs
from game_data import data


def game_loop():
    score = 0
    should_continue = True

    account_a = random.choice(data)

    while should_continue:
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {account_a['name']}, a {account_a['description']} from {account_a['country']}")
        print(vs)
        print(f"Compare B: {account_b['name']}, a {account_b['description']} from {account_b['country']}")

        decision = input("Who has more followers ? Type 'A' or 'B'").lower()

        if account_a['follower_count'] > account_b['follower_count']:
            answer = "a"
        elif account_b['follower_count'] > account_a['follower_count']:
            answer = "b"
            account_a = account_b
        else:
            answer = "equal"

        if decision == answer:
            score += 1
            print(f"You are correct. Your current score is {score}")
        elif answer == "equal":
            score += 1
            print(f"They are equal. Your current score is {score}")
        else:
            print(f"That was incorrect. Your final score is {score}")
            should_continue = False


print(logo)
game_loop()
