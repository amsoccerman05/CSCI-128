import random
import matplotlib.pyplot as plt

seed = input()
random.seed(seed)

n = int(input())

results = [random.randint(1, 6) for _ in range(n)]
counts = [results.count(side) for side in range(1, 7)]

plt.bar(range(1, 7), counts)
plt.savefig("rolls_bar_chart.png")
plt.show()

# passed