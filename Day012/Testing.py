# Scope
# Local and Global Scope
# There is no Block Scope in Python

# Global Scope
enemies = 1


def increase_enemies():
    # Local Scope
    enemies = 2
    print(f"enemies inside function: {enemies}")


# Output is 2
increase_enemies()
# Output is 1
print(f"enemies outside function: {enemies}")
# Generally, it is a bad idea to give your local variables and global variables the same name


player_health = 10


def drink_potion():
    # Use the 'global' keyword if you want to modify a global variable however avoid doing this as much as you can
    # global player_health
    # You can also use the 'return' keyword to easily modify the global variable without 'global' keyword
    return player_health + 1


player_health = drink_potion()
print(player_health)

game_level = 3


def create_opponents():
    opponents = ["Skeleton", "Alien", "Zombie"]
    if game_level > 5:
        new_opponent = opponents[0]
    # Despite new_opponent being declared in the if-block, it can still be called within the function
    print(new_opponent)


# Global Constants
# The naming convention for global constants is to use capital letters and underscores to separate words
PI = 3.14
URL = "www.udemy.com"
TWITTER_HANDLE = "@yu_angela"

