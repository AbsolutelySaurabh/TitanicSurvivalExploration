import numpy as np
import pandas as pd
from IPython.display import display #allows the use of display for DataFrames


in_file = open(r'C:\Users\Saurabh\Desktop\ML_ND\My Projects\Titanic_Survivors_exploration\titanic_data.csv')
# full_data = pd.read_csv(in_file)
#
# #print the first few entries of the RMS dataset
# display(full_data.head())

print in_file.read()
