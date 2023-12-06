import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('/Users/aiden/OneDrive/Desktop/CSCI128/CSCI_128_Final_Project/Car_Information.csv')  # Replace 'path_to_your_csv_file.csv' with your file path

# Plotting number of cylinders against gas mileage
plt.figure(figsize=(8, 6))
plt.scatter(data['num-of-cylinders'], data['city-mpg'], alpha=0.7)
plt.title('Number of Cylinders vs Gas Mileage')
plt.xlabel('Number of Cylinders')
plt.ylabel('City MPG')
plt.grid(True)
plt.show()