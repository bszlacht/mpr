import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["threads", "arr_size", "time"]

df = pd.read_csv("results/default/static.csv", usecols=columns)
df_thread_1 = df[df['threads'] == 1]
df_thread_2 = df[df['threads'] == 2]
df_thread_3 = df[df['threads'] == 3]
df_thread_4 = df[df['threads'] == 4]
# sp_1 = df.iloc[0]['time']
plt.scatter(df_thread_1.arr_size, df_thread_1.time,
            color='r', label='1 thread')
plt.scatter(df_thread_2.arr_size, df_thread_2.time,
            color='b', label='2 threads')
plt.scatter(df_thread_3.arr_size, df_thread_3.time,
            color='g', label='3 threads')
plt.scatter(df_thread_4.arr_size, df_thread_4.time,
            color='yellow', label='4 threads')
plt.xlabel('size of array [B]')
plt.ylabel('time [s]')
plt.title('Time plot on vCluster for schedule(static)')
plt.legend()
plt.show()

df = pd.read_csv("results/default/dynamic.csv", usecols=columns)
df_thread_1 = df[df['threads'] == 1]
df_thread_2 = df[df['threads'] == 2]
df_thread_3 = df[df['threads'] == 3]
df_thread_4 = df[df['threads'] == 4]
plt.scatter(df_thread_1.arr_size, df_thread_1.time,
            color='r', label='1 thread')
plt.scatter(df_thread_2.arr_size, df_thread_2.time,
            color='b', label='2 threads')
plt.scatter(df_thread_3.arr_size, df_thread_3.time,
            color='g', label='3 threads')
plt.scatter(df_thread_4.arr_size, df_thread_4.time,
            color='yellow', label='4 threads')
plt.xlabel('size of array [B]')
plt.ylabel('time [s]')
plt.title('Time plot on vCluster for schedule(dynamic)')
plt.legend()
plt.show()


df = pd.read_csv("results/default/guided.csv", usecols=columns)
df_thread_1 = df[df['threads'] == 1]
df_thread_2 = df[df['threads'] == 2]
df_thread_3 = df[df['threads'] == 3]
df_thread_4 = df[df['threads'] == 4]
plt.scatter(df_thread_1.arr_size, df_thread_1.time,
            color='r', label='1 thread')
plt.scatter(df_thread_2.arr_size, df_thread_2.time,
            color='b', label='2 threads')
plt.scatter(df_thread_3.arr_size, df_thread_3.time,
            color='g', label='3 threads')
plt.scatter(df_thread_4.arr_size, df_thread_4.time,
            color='yellow', label='4 threads')
plt.xlabel('size of array [B]')
plt.ylabel('time [s]')
plt.title('Time plot on vCluster for schedule(guided)')
plt.legend()
plt.show()

df = pd.read_csv("results/default/runtime.csv", usecols=columns)
df_thread_1 = df[df['threads'] == 1]
df_thread_2 = df[df['threads'] == 2]
df_thread_3 = df[df['threads'] == 3]
df_thread_4 = df[df['threads'] == 4]
plt.scatter(df_thread_1.arr_size, df_thread_1.time,
            color='r', label='1 thread')
plt.scatter(df_thread_2.arr_size, df_thread_2.time,
            color='b', label='2 threads')
plt.scatter(df_thread_3.arr_size, df_thread_3.time,
            color='g', label='3 threads')
plt.scatter(df_thread_4.arr_size, df_thread_4.time,
            color='yellow', label='4 threads')
plt.xlabel('size of array [B]')
plt.ylabel('time [s]')
plt.title('Time plot on vCluster for schedule(runtime)')
plt.legend()
plt.show()


df = pd.read_csv("results/default/auto.csv", usecols=columns)
df_thread_1 = df[df['threads'] == 1]
df_thread_2 = df[df['threads'] == 2]
df_thread_3 = df[df['threads'] == 3]
df_thread_4 = df[df['threads'] == 4]
plt.scatter(df_thread_1.arr_size, df_thread_1.time,
            color='r', label='1 thread')
plt.scatter(df_thread_2.arr_size, df_thread_2.time,
            color='b', label='2 threads')
plt.scatter(df_thread_3.arr_size, df_thread_3.time,
            color='g', label='3 threads')
plt.scatter(df_thread_4.arr_size, df_thread_4.time,
            color='yellow', label='4 threads')
plt.xlabel('size of array [B]')
plt.ylabel('time [s]')
plt.title('Time plot on vCluster for schedule(auto)')
plt.legend()
plt.show()
