import pandas as pd

# read the csv file
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Count the different colors of squirrel
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

# make a dictionary to store the data
squirrel_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "No": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrel_count]
}

# convert the dictionary to a panda dataframe
squirrel_dataframe = pd.DataFrame(squirrel_dic)

# export the dataframe to a csv file
squirrel_dataframe.to_csv("squirrel_color_data")
