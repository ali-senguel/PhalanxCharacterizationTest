import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from tabulate import tabulate


def fn():       # 1.Get file names from directory
    directory = os.getcwdb()
    file_list=os.listdir(r"/home/ali/Documents/Projects/PhalanxCharacterizationTest/Experiment2Force/forcemeasure20220721/sec1b_2")
    return file_list

files = fn()
time = []
for f in files:
    str= f.split(" ")
    time.append(str[2].split(".")[0].replace('-',':'))

time = pd.Series(time)
time = pd.to_datetime(time).dt.strftime('%H:%M:%S')
sorted_time = time.sort_values(ascending=True)
#print(time)
#print(sorted_time)

#df = pd.read_csv("E1_1to100mNw10umps", sep = "\t")
df = pd.read_csv("forcemeasure20220721/sec1b_2force.txt",sep="\t")

distance = df.iloc[:,0]
force = df.iloc[:,1]*1000
day = df.iloc[:,2]
day = pd.to_datetime(day).dt.strftime('%H:%M:%S')

result_df = pd.DataFrame(columns=('time', 'mean_force'))

for ind in sorted_time: 
    ave_force =  force[day == ind].mean()
    data = {'time': ind, 'mean_force': ave_force}
    print(data)


# plt.figure(1)
# plt.plot(distance)
force.plot()
plt.show()

# df["Z/m"] = df["Z/m"].str.replace(',', '.')
# df["time/s"] = df["time/s"].str.replace(',', '.')
# df["force/N"] = df["force/N"].str.replace(',', '.')


# z_mm = df["Z/m"].to_numpy().astype(float)*1000
# time_s = df["time/s"].to_numpy().astype(float)
# force_n = df["force/N"].to_numpy().astype(float)

# #Testing the 
# ind = df["Z/m"].to_numpy().astype(float)*1000

# tresh = 0.1
# min_tresh = tresh*0.999
# max_tresh = tresh*1.001

# print(z_mm[(ind>min_tresh) & (ind<max_tresh)])
# print(force_n[(ind>min_tresh) & (ind<max_tresh)])

# plt.figure(1)
# plt.plot(z_mm)
# plt.figure(2)
# plt.plot(time_s)
# plt.figure(3)
# plt.plot(force_n)
# plt.show()