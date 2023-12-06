import pandas as pd
import matplotlib.pyplot as plt

# read the csv file
data = pd.read_csv('Car_Information.csv')

def plot_cylinders_vs_mpg():
    plt.figure(figsize=(8, 6))
    plt.scatter(data['cylinders'], data['mpg'])
    plt.title('Number of cylinders vs MPG')
    plt.xlabel('Number of cylinders (qty)')
    plt.ylabel('MPG (miles per gallon)')
    plt.grid(True)
    plt.savefig('cylinders_vs_mpg.png')  # save the plot as a png

def plot_horsepower_vs_acceleration():
    plt.figure(figsize=(8, 6))
    plt.scatter(data['horsepower'], data['acceleration'])
    plt.title('Horsepower vs acceleration')
    plt.xlabel('Horsepower (hp)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.grid(True)
    plt.savefig('horsepower_vs_acceleration.png')  # save the plot as a png

# call the functions
plot_cylinders_vs_mpg()

plot_horsepower_vs_acceleration()

# group by cylinders and calculate the average MPG for each group
avg_mpg_by_cylinders = data.groupby('cylinders')['mpg'].mean()

# Print the average MPG for each cylinder group
print("OUTPUT Average MPG for each number of cylinders:")
print(avg_mpg_by_cylinders)
