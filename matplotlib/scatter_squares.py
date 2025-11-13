import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('classic')
fig, ax = plt.subplots()

ax.scatter(x_values,y_values, c='green', s=10)

ax.set_title("Square numbers", fontsize = 20)
ax.set_xlabel("Value", fontsize = 12)
ax.set_ylabel("Square of value", fontsize=12)

ax.axis([0,1100, 0, 1_100_000])
plt.show()