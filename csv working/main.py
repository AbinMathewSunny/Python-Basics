'''read data from the csv file provides and perform actions on it'''

'''
import csv

with open("weather_data.csv") as data_file:
    data=s=csv.reader(data_file)
    temperatures=[]
    for row in data:
        if row[1]!="temp":
           temperatures.append(row[1])
    print(temperatures)
'''

'''read data from the csv file provides and perform actions on it using pandas'''
import pandas
data=pandas.read_csv("weather_data.csv")
print(data["temp"])

'''convert to dict'''
data_dict=data.to_dict()
print(data_dict)

'''convert to list'''
temp_list=data["temp"].to_list()
print(temp_list)

'''mean'''
print(data["temp"].mean())

#get data in columns
print(data["condition"])
print(data.condition)

#get data fromm rows
print(data[data.day == "Monday"])

