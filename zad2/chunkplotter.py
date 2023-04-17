import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["procent", "time"]

df = pd.read_csv("results/chunks/static.csv", usecols=columns)
# sp_1 = df.iloc[0]['time']
plt.scatter(df.procent, df.time,
            color='r')
plt.axvline(x=25, color='b', label='best chunk size', ls='--')
plt.xlabel('chunk equal percentage of the whole array')
plt.ylabel('time [s]')
plt.title('Time plot on vCluster for schedule(static, array percent)')
plt.legend()
plt.show()

df = pd.read_csv("results/chunks/dynamic.csv", usecols=columns)
# sp_1 = df.iloc[0]['time']
plt.scatter(df.procent, df.time,
            color='r')
plt.axvline(x=25, color='b', label='best chunk size', ls='--')
plt.xlabel('chunk equal percentage of the whole array')
plt.ylabel('time [s]')
plt.title('Time plot on vCluster for schedule(dynamic, array percent)')
plt.legend()
plt.show()
