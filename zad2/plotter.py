import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["threads","arr_size","time"]

df = pd.read_csv("results/default/static.csv", usecols=columns)
df_thread_1 = df[df['threads'] == 1]
df_thread_2 = df[df['threads'] == 2]
df_thread_3 = df[df['threads'] == 3]
df_thread_4 = df[df['threads'] == 4]
#sp_1 = df.iloc[0]['time']
plt.scatter(df_thread_1.arr_size, df_thread_1.time, color='r', label='1 thread')
plt.scatter(df_thread_2.arr_size, df_thread_2.time, color='b', label='2 threads')
plt.scatter(df_thread_3.arr_size, df_thread_3.time, color='g', label='3 threads')
plt.scatter(df_thread_4.arr_size, df_thread_4.time, color='yellow', label='4 threads')

# df = pd.read_csv("montecarlo/results/skalowaniesilnevc", usecols=columns)
# df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
# sp_1 = df.iloc[0]['time']
# plt.scatter(df.n, df.time, color='b', label='strong scaling')
plt.xlabel('size of array [B]')
plt.ylabel('time [s]')
plt.title('Time plot on vCluster for schedule(static)')
plt.legend()
plt.show()

# df = pd.read_csv("montecarlo/results/skalowanieslabevc", usecols=columns)
# df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
# sp_1 = df.iloc[0]['time']
# plt.scatter(df.n, df.n * sp_1 / df.time, color='r', label='weak scaling')
# df = pd.read_csv("montecarlo/results/skalowaniesilnevc", usecols=columns)
# df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
# sp_1 = df.iloc[0]['time']
# plt.scatter(df.n, sp_1 / df.time, color='b', label='strong scaling')
# plt.xlabel('number of processors')
# plt.ylabel('speedup')
# plt.title('Speedup plot on vCluster')
# plt.legend()
# plt.show()



# df = pd.read_csv("montecarlo/results/skalowanieslabevc", usecols=columns)
# df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
# sp_1 = df.iloc[0]['time']
# plt.scatter(df.n, sp_1 / df.time, color='r', label='weak scaling')
# df = pd.read_csv("montecarlo/results/skalowaniesilnevc", usecols=columns)
# df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
# sp_1 = df.iloc[0]['time']
# plt.scatter(df.n, sp_1 / (df.n * df.time), color='b', label='strong scaling')
# plt.xlabel('number of processors')
# plt.ylabel('efficiency [1/s]')
# plt.title('Efficiency plot on vCluster')
# plt.ylim([0, 1.5])
# plt.legend()
# plt.show()


# df = pd.read_csv("montecarlo/results/skalowanieslabevc", usecols=columns)
# df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
# sp_1 = df.iloc[0]['time']
# sp = df.n * sp_1 / df.time
# plt.scatter(df.n, (1 / sp - 1 / df.n) / (1 - 1 / df.n), color='r', label='weak scaling')
# df = pd.read_csv("montecarlo/results/skalowaniesilnevc", usecols=columns)
# df = df.groupby(['n'], as_index=False).agg({'time': 'mean'})
# sp_1 = df.iloc[0]['time']
# sp = sp_1 / df.time
# plt.scatter(df.n, (1 / sp - 1 / df.n) / (1 - 1 / df.n), color='b', label='strong scaling')
# plt.title('Serial fraction plot on vCluster')
# plt.xlabel('number of processors')
# plt.ylabel('serial fraction')
# plt.ylim([-0.5, 0.5])
# plt.axhline(y=0, color='black', linestyle='-')
# plt.show()
