# python_libraries
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
