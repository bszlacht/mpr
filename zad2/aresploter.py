import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["num_of_threads", "time"]

df = pd.read_csv("results/all.csv", usecols=columns)

n = 4
df1 = df.iloc[::n] # cale
df2 = df.iloc[1::n] # buckety
df3 = df.iloc[2::n] # sort
df4 = df.iloc[3::n] # przepisywanie

df1 = df1.groupby('num_of_threads')['time'].mean()
df2 = df2.groupby('num_of_threads')['time'].mean()
df3 = df3.groupby('num_of_threads')['time'].mean()
df4 = df4.groupby('num_of_threads')['time'].mean()

plt.scatter(df1.index, df1.values, color='r')
# plt.scatter(df2.index, df2.values, color='b')
plt.scatter(df3.index, df3.values, color='g')
plt.scatter(df4.index, df4.values, color='#9c1dbf')
plt.xlabel('number of buckets')
plt.ylabel('time[s]')
plt.title('Time plot based on number of buckets')
plt.legend()
plt.show()

# columns = ["time", "threads"]

# df = pd.read_csv("results/spraw2/wholetime.csv", usecols=columns)
# plt.scatter(df.threads, df.time, color='r')
# plt.xlabel('number of threads')
# plt.ylabel('time[s]')
# plt.title('Time plot of whole bucket sort execution based on number of threads')
# plt.legend()
# plt.show()

# dfp = pd.read_csv("results/spraw2/putinbucket.csv", usecols=columns)
# df = dfp.groupby('threads')['time'].agg(['mean', 'std'])

# mean_values = df['mean']
# std_values = df['std']
# plt.errorbar(df.index, mean_values, yerr=std_values, fmt='o', color='r', label='Mean')
# plt.xlabel('number of threads')
# plt.ylabel('time[s]')
# plt.title('Time plot of putting elements into buckets based on number of threads')
# plt.legend()
# plt.show()

# dfp = pd.read_csv("results/spraw2/sorttime.csv", usecols=columns)
# df = dfp.groupby('threads')['time'].agg(['mean', 'std'])

# mean_values = df['mean']
# std_values = df['std']
# plt.errorbar(df.index, mean_values, yerr=std_values, fmt='o', color='r', label='Mean')
# plt.xlabel('number of threads')
# plt.ylabel('time[s]')
# plt.title('Time plot of sorting elements in buckets based on number of threads')
# plt.legend()
# plt.show()

# dfp = pd.read_csv("results/spraw2/writingtime.csv", usecols=columns)
# df = dfp.groupby('threads')['time'].agg(['mean', 'std'])

# mean_values = df['mean']
# std_values = df['std']
# plt.errorbar(df.index, mean_values, yerr=std_values, fmt='o', color='r', label='Mean')
# plt.xlabel('number of threads')
# plt.ylabel('time[s]')
# plt.title('Time plot of writing sorted elements from buckets to array based on number of threads')
# plt.legend()
# plt.show()


# dfp = pd.read_csv("results/spraw2/fixedwholetime.csv", usecols=columns)
# df = dfp.groupby('threads')['time'].agg(['mean', 'std'])

# mean_values = df['mean']
# std_values = df['std']
# plt.errorbar(df.index, mean_values, yerr=std_values, fmt='o', color='r', label='Mean')
# plt.xlabel('number of threads')
# plt.ylabel('time[s]')
# plt.title('Time plot of bucketsort based on number of threads')
# plt.legend()
# plt.show()
