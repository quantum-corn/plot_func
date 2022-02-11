# %% md
# # Plot Functions
# A simple matplotlib and numpy based python code to quickly plot functions
# ### v1.0

# %% imports
import matplotlib.pyplot as plt
import numpy as np

# %% x range
min=0
max=10
div=200

# %% range setup
x=np.linspace(min, max, div)

# %% function creation
f=x**2

# %% plot
fig, ax=plt.subplots()
ax.plot(x, f)

# %% display the plot
plt.show()
