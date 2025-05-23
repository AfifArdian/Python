import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# Get Data in Columns
# print(data["condition"])
# print(data.day)

# # Get Data in Row
monday_data = data[data.day == "Monday"]
# print(data[data.temp == data.temp.max()])
print(monday_data.temp[0])

# convert Celsius to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * (9/5) + 32
# print(monday.condition)
# print(monday_temp_F)

# Create data frame from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
