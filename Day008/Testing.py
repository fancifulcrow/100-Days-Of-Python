def greet(name):
    print(f"Hello, {name}")
    print("How do you do?")
    print("Isn't the weather nice today?")

def greet_again(name, location):
    print(f"Hello, {name}")
    print("How do you do?")
    print(f"WHat is it like in {location}")

my_name = input("What is your name")
my_location = input("Where do you come from?")
greet(my_name)
greet_again(my_name, my_location)
greet_again("Courage", "Nowhere")
greet_again(location="Bikini Bottom", name="Spongebob",)