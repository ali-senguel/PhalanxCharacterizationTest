import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabulate import tabulate

df = pd.read_csv("E1_1to100mNw10umps", sep = "\t")

df["Z/m"] = df["Z/m"].str.replace(',', '.')
df["time/s"] = df["time/s"].str.replace(',', '.')
df["force/N"] = df["force/N"].str.replace(',', '.')


z_mm = df["Z/m"].to_numpy().astype(float)*1000
time_s = df["time/s"].to_numpy().astype(float)
force_n = df["force/N"].to_numpy().astype(float)

#Testing the 
ind = df["Z/m"].to_numpy().astype(float)*1000

tresh = 0.1
min_tresh = tresh*0.999
max_tresh = tresh*1.001

print(z_mm[(ind>min_tresh) & (ind<max_tresh)])
print(force_n[(ind>min_tresh) & (ind<max_tresh)])

plt.figure(1)
plt.plot(z_mm)
plt.figure(2)
plt.plot(time_s)
plt.figure(3)
plt.plot(force_n)
plt.show()