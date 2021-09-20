import numpy as np
import matplotlib.pyplot as plt

# Assign filename: file
file = 'seaslug.txt'

# Import file: data ; Tab delimited
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the first element of data
print(data_float[0])

# scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()