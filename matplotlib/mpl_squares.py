import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('classic')
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth = 3)

ax.set_title("Square numbers", fontsize = 20)
ax.set_xlabel("Value", fontsize = 12)
ax.set_ylabel("Square of value", fontsize=12)

ax.tick_params(labelsize=14)
plt.show()