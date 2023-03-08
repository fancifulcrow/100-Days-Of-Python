programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again"}

# Dictionaries take the syntax: {key:value}
# Avoid key errors and name errors

print(programming_dictionary["Bug"])
# Create an empty dictionary
empty_dictionary = {}
# Wipe an existing dictionary
existing_dictionary = {"Hello": "World", "Hi": "whoever you are"}
existing_dictionary = {}
# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# Adding a new item in a dictionary
programming_dictionary["Hello"] = "A casual greeting"
# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

# Nesting a List in a Dictionary
travel_log = {"Germany": ["Hamburg", "Berlin", "Duisburg", "Munich"],
              "France": ["Paris", "Dijon", "Lille"]}
# Nesting a Dictionary in a Dictionary
travel_log2 = {"Germany": {"cities_visited": ["Hamburg", "Berlin", "Duisburg", "Munich"],
                           "total_visits": 12},
               "France": {"cities_visited": ["Paris", "Dijon", "Lille"],
                          "total_visits": 4}}
# Nesting a Dictionary in a List
travel_log_list = [{"country": "Germany",
                    "cities_visited": ["Hamburg", "Berlin", "Duisburg", "Munich"],
                    "total_visits": 12},
                   {"country": "France",
                    "cities_visited": ["Paris", "Dijon", "Lille"],
                    "total_visits": 4}]
# Use lines to make the code readable by the user

print(travel_log_list[0]["cities_visited"][2])
