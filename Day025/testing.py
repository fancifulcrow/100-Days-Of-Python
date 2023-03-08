# CSV stands for Comma Separated Values

# You could use this to get the data in a csv
with open("weather_data.csv", mode="r") as data_file:
    data = data_file.readlines()
    print(data)

# However Python comes with an inbuilt library called csv that helps with this
import csv

with open("weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)

# This format is easier to work with

# Panda is a powerful data analysis library in python
# This simplifies collecting data so much
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)
print(data["temp"])

# The 2 Primary Data Structures in Panda
print(type(data))
# DataFrame - 2 dimensional  - i.e tables
print(type(data["temp"]))
# Series = 1 dimensional i.e columns

# View documentation for more
# It is extremely well documented

data_dic = data.to_dict()
print(data_dic)

data_temp_list = data["temp"].to_list()
print(data_temp_list)

# average_temp = sum(data_temp_list) / len(data_temp_list)
# print(f"The average temperature is {average_temp}")

# or, more preferably
print(f"Average temperature is {data['temp'].mean()}")
print(f"Maximum temperature is {data['temp'].max()}")

# Getting Data in a column

# treating it like a dictionary
print(data["condition"])
# treating it like an object
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print(f"Row of the hottest day")
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)


def fahrenheit_to_celsius(temperature):
    return (temperature * (9/5)) + 32


monday_temp = int(monday.temp)
print(fahrenheit_to_celsius(monday_temp))

# Create a dataframe from scratch
dict_of_data = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

dataframe_from_dic = pd.DataFrame(dict_of_data)
print(dataframe_from_dic)
dataframe_from_dic.to_csv("new_data.csv")
