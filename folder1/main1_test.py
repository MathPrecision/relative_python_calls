import os
print(os.getcwd())
os.chdir(os.path.join(os.getcwd(), '..'))
print(os.getcwd())

from config0 import plus
from folder1.config1 import minus
import folder2.config2 as c2

print(plus(2,3))
print(minus(2,3))
print(c2.mal(2,3))