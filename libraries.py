# python_libraries
import math
from math import *  # Imports all functions (can cause conflicts)
from random import randint  # Only imports 'randint' from 'random'
import numpy as np  # Shortens 'numpy' to 'np'
import math  # Imports the entire 'math' library
print(math.sqrt(625))  # Uses the sqrt function from math

# import with alias
print(np.array([1, 2, 3]))  # Uses 'np' instead of 'numpy'

# import specific function from a library
print(randint(1, 10))  # No need to write 'random.randint'

# import everything(Not recommended)
print(sqrt(25))  # Works, but can overwrite other functions


print("Square Root:", math.sqrt(16))  # Using math library
print("Power of 2^3:", math.pow(2, 3))  # Using math library
print("Random Number:", randint(1, 100))  # Using random library


# Using the python libraries


# Calculate square root
print(math.sqrt(16))  # Output: 4.0

# Trigonometric functions
print(math.sin(math.pi / 2))  # Output: 1.0

print(math.cos(0))  # Output: 1.0
print(math.tan(math.pi / 4))  # Output: 0.9999999999999999
