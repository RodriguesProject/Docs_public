"""Gráfico de dispersão (scatter) com Matplotlib."""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([23, 29, 11, 13, 17, 2, 3, 5, 7, 19])

plt.scatter(x, y, color="green", marker="*", s=100, label="Pontos")
plt.legend(loc="upper right")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gráfico de dispersão")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()
