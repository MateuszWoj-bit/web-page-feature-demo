import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

colors = ['#3ee622', '#0085ca', '#963cbd', '#ff0098', '#ef3340', '#ffd700', '#008578', '#ca9dde', '#fd7e14', '#6cc3d5',
          '#ff69b4', '#00ff00', '#0000ff', '#ffa500', '#800080', '#008000', '#ff4500', '#4b0082', '#6a5acd', '#d2691e',
          '#20b2aa', '#ff1493', '#4682b4', '#32cd32', '#b22222']

plt.figure(figsize=(10, 6))
for i in range(len(x)):
    plt.plot(x[i], y[i], marker='o', color=colors[i], markersize=8)

plt.title('Przykładowy wykres z wykorzystaniem wszystkich kolorów')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.tight_layout()

plt.show()

