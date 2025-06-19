import sys
import os

print(sys.path[-1])
# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path (only during runtime)
sys.path.append(parent_dir)
print(sys.path[-1])

from config0 import plus
from folder1.config1 import minus
import folder2.config2 as c2

print(plus(2,3))
print(minus(2,3))
print(c2.mal(2,3))