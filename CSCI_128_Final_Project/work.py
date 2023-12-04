import csv
import numpy as np
import matplotlib.pyplot as plt

num_of_cylinders = []
fuel_economy = []

with open('/Users/aiden/OneDrive/Desktop/CSCI128/CSCI_128_Final_Project/Car_Information.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        num_of_cylinders.append(float(row['num_of_cylinders']))
        fuel_economy.append(float(row['fuel_economy']))

num_of_cylinders = np.array(num_of_cylinders)
fuel_economy = np.array(fuel_economy)

mean_num_of_cylinders = np.mean(num_of_cylinders)
mean_fuel_economy = np.mean(fuel_economy)

numerator = np.sum((num_of_cylinders - mean_num_of_cylinders) * (fuel_economy - mean_fuel_economy))
denominator1 = np.sum((num_of_cylinders - mean_num_of_cylinders) ** 2)
denominator2 = np.sum((fuel_economy - mean_fuel_economy) ** 2)
correlation = numerator / np.sqrt(denominator1 * denominator2)

print(f'Correlation between Number of Cylinders and Fuel Economy: {correlation}')

plt.scatter(num_of_cylinders, fuel_economy)
plt.title('Number of Cylinders vs Fuel Economy')
plt.xlabel('Number of Cylinders')
plt.ylabel('Fuel Economy')
plt.show()
