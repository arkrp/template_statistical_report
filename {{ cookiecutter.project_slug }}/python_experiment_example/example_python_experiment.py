import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(1,10,7)
y = x**2

plt.plot(x,y)
plt.xlabel("example x label")
plt.ylabel("example y label")
plt.title("example plot title")
plt.savefig("example_plot.png")

df = pd.DataFrame({"x":x, "y":y})
df.to_csv("example_data_table.csv")
