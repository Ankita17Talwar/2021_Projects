import  numpy as np

# Initialize random_walk
np.random.seed(123)
random_walk=[0]


for x in range(100):
    # Set step: last element in random_walk
    step=random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(step - 1,0)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)
plt.show()