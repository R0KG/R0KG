import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colour_list = data.value_counts("Primary Fur Color").to_list()
squar_data  = {"Fur Color": ["grey","red","black"],
               "Count": colour_list}
df = pandas.DataFrame(squar_data)
df.to_csv("squarel_data.csv")
