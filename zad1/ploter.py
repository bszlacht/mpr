import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["n", "time"]

df = pd.read_csv("montecarlo/results/skalowanieslabevc", usecols=columns)
df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
sp_1 = df.iloc[0]['time']
plt.scatter(df.n, df.time, color='r', label='weak scaling')
df = pd.read_csv("montecarlo/results/skalowaniesilnevc", usecols=columns)
df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
sp_1 = df.iloc[0]['time']
plt.scatter(df.n, df.time, color='b', label='strong scaling')
plt.xlabel('number of processors')
plt.ylabel('time[s]')
plt.title('Time plot on vCluster')
plt.legend()
plt.show()

df = pd.read_csv("montecarlo/results/skalowanieslabevc", usecols=columns)
df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
sp_1 = df.iloc[0]['time']
plt.scatter(df.n, df.n * sp_1 / df.time, color='r', label='weak scaling')
df = pd.read_csv("montecarlo/results/skalowaniesilnevc", usecols=columns)
df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
sp_1 = df.iloc[0]['time']
plt.scatter(df.n, sp_1 / df.time, color='b', label='strong scaling')
plt.xlabel('number of processors')
plt.ylabel('speedup')
plt.title('Speedup plot on vCluster')
plt.legend()
plt.show()



df = pd.read_csv("montecarlo/results/skalowanieslabevc", usecols=columns)
df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
sp_1 = df.iloc[0]['time']
plt.scatter(df.n, sp_1 / df.time, color='r', label='weak scaling')
df = pd.read_csv("montecarlo/results/skalowaniesilnevc", usecols=columns)
df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
sp_1 = df.iloc[0]['time']
plt.scatter(df.n, sp_1 / (df.n * df.time), color='b', label='strong scaling')
plt.xlabel('number of processors')
plt.ylabel('efficiency [1/s]')
plt.title('Efficiency plot on vCluster')
plt.ylim([0, 1.5])
plt.legend()
plt.show()


df = pd.read_csv("montecarlo/results/skalowanieslabevc", usecols=columns)
df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
sp_1 = df.iloc[0]['time']
sp = df.n * sp_1 / df.time
plt.scatter(df.n, (1 / sp - 1 / df.n) / (1 - 1 / df.n), color='r', label='weak scaling')
df = pd.read_csv("montecarlo/results/skalowaniesilnevc", usecols=columns)
df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
sp_1 = df.iloc[0]['time']
sp = sp_1 / df.time
plt.scatter(df.n, (1 / sp - 1 / df.n) / (1 - 1 / df.n), color='b', label='strong scaling')
plt.title('Serial fraction plot on vCluster')
plt.xlabel('number of processors')
plt.ylabel('serial fraction')
plt.ylim([-0.5, 0.5])
plt.axhline(y=0, color='black', linestyle='-')
plt.show()
