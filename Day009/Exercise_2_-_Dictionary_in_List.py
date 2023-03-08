# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


def add_new_country(country_visited, number_of_visits, cities_visited):
    travel_log.append({"country": country_visited, "visits": number_of_visits, "cities": cities_visited})


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
