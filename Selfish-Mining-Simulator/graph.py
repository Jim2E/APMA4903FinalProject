import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

alpha = []
gamma = []
rev = []

with open('results.txt') as f:
    lines = f.readlines()

# a = str.split(lines[0])
a = lines[0].split(",")


# print(float(a[2]))

for line in lines:
    a = line.split(",")
    # print("Alpha: ", float(a[0]))
    alpha.append(float(a[0]))
    # print("Gamma: ", float(a[1]))
    gamma.append(float(a[1]))
    # print("Revenue Ratio: ", float(a[5]))
    rev.append(float(a[5]))
    # print()

# print(alpha)
# print(gamma)
# print(rev)
sns.scatterplot(x = alpha, y = rev, hue = gamma )
plt.show()


