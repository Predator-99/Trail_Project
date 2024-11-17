import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from Config import *
from Utility import *

print("hello world")
e = 5
w = 4


def add(x, y):
    return x + y


print(add(e, w))
print(math.sqrt(e))

print (NAME,EMAIL,AGE)

df1 = pd.read_csv(FIRST_DATA)
print(df1.head())

greet(NAME)

mul(4,5)