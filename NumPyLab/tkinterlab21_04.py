import math
import numpy as np
from matplotlib import pyplot as plt
plt.plot([1, 3, 3, 4, 5, 6, 2], [3, 4, 6, 7, 5, 8, 9])  # plot the graph on canvas
plt.title('Test Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# -------------------------------------------------
# doubts
x = np.arange(0, math.pi, 0.5)
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
y = np.sin(x)
ax.set_xlabel('Angel')
ax.set_ylabel('Sine')
ax.set_xticks([0, 2, 4, 6])
ax.set_xticklabels(['Zero', 'Two', 'Four', 'Six'])
ax.set_yticks([-10])
# ---------------------------------------------
plt.bar([1, 2, 3, 4, 5], [60, 65, 70, 75, 80], label = "compDesign", width=0.5, color='b')

plt.bar([1, 2, 3, 4, 5], [60, 70, 80, 85, 90],
        label="coa",
        width=0.5,
        color='g')
plt.legend
plt.title("Subject Maths")
plt.xlabel("Subject Id")
plt.ylabel("Score Maths")


plt.show()  # print the plotted graph on screen
