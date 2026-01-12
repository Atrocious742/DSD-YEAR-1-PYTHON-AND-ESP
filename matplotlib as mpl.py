import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")

years = np.array([2020, 2021, 2022, 2023])

porsche_sales = np.array([0.27, 0.30, 0.31, 0.32])   
nissan_sales = np.array([4.0, 3.8, 3.4, 3.6])       

plt.subplot(1, 2, 1)
plt.plot(years, porsche_sales, color="cyan", marker="o", linewidth=2)
plt.xlabel("Year")
plt.ylabel("Cars Sold (millions)")
plt.title("Porsche")

plt.subplot(1, 2, 2)
plt.plot(years, nissan_sales, color="magenta", marker="s", linewidth=2)
plt.xlabel("Year")
plt.ylabel("Cars Sold (millions)")
plt.title("Nissan")

plt.suptitle("Global Car Sales", fontsize=14)
plt.tight_layout()
plt.show()