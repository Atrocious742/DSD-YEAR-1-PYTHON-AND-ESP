import matplotlib.pyplot as plt
import numpy as np

def plot_3d_surface(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none', alpha=0.8, linewidth=0.5, antialiased=True, rstride=1, cstride=1, shade=True)
    plt.show()
# Example usage
x = np.linspace(-20, 40, 100)
y = np.linspace(-20, 40, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
plot_3d_surface(x, y, z)
