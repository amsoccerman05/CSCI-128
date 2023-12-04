import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('height_weight.csv', header=None, names=['Height (in)', 'Weight (lb)'])

heights = df['Height (in)'].tolist()
weights = df['Weight (lb)'].tolist()

plt.figure(figsize=(8, 6))
plt.scatter(heights, weights, alpha=0.5)
plt.title("Height vs. Weight")
plt.xlabel("Height (in)")
plt.ylabel("Weight (lb)")
plt.grid(True)

plt.savefig('height_weight_scatter.png')
plt.show()
