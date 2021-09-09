import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.159, 3.692, 5.263, 6.972]

# Add more Data
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

#add Labels
plt.xlabel('year')
plt.ylabel('pop')
plt.title('Population Projection')

# yticks/xticks(value, label)
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B']  # name of y axis points. list should have same number as first argument
           )


# Display the plot with plt.show()
plt.show()

## Scatter Plot
# plt.scatter(year, pop)
# plt.show()
