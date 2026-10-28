import csv
import pandas
'''with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != 'temp':

            temperatures.append(row[1])
    print(temperatures)'''
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)
temp_list = data['temp'].to_list()
print(len(temp_list))
sum1 = sum(temp_list)/len(temp_list)
print(data['temp'].max())
