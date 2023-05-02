import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["num_of_threads", "time"]

df = pd.read_csv("results/all.csv", usecols=columns)

n = 4
df1 = df.iloc[::n]  # cale
df2 = pd.read_csv("results/buckets.csv", usecols=columns)
df3 = df.iloc[2::n]  # sort
df4 = df.iloc[3::n]  # przepisywanie

df1 = df1.groupby('num_of_threads')['time'].mean()
df2 = df2.groupby('num_of_threads')['time'].mean()
df3 = df3.groupby('num_of_threads')['time'].mean()
df4 = df4.groupby('num_of_threads')['time'].mean()

plt.scatter(df1.index, df1.values, color='r', label='WHOLE BUCKETSORT')
plt.scatter(df2.index, df2.values, color='b', label='INSERTING INTO BUCKETS')
plt.scatter(df3.index, df3.values, color='g', label='SORTING BUCKETS')
plt.scatter(df4.index, df4.values, color='#9c1dbf', label='WRITING TO RESULT')
plt.xlabel('number of threads')
plt.ylabel('time[s]')
plt.title('Time plot based on number of threads')
plt.legend()
plt.show()


speedup1 = df1.values[0] / df1.values
speedup2 = df2.values[0] / df2.values
speedup3 = df3.values[0] / df3.values
speedup4 = df4.values[0] / df4.values

plt.scatter(df1.index, speedup1, color='r', label='WHOLE BUCKETSORT')
plt.scatter(df2.index, speedup2, color='b', label='INSERTING INTO BUCKETS')
plt.scatter(df3.index, speedup3, color='g', label='SORTING BUCKETS')
plt.scatter(df4.index, speedup4, color='#9c1dbf', label='WRITING TO RESULT')
plt.xlabel('number of threads')
plt.ylabel('time[s]')
plt.title('Speedup plot based on number of threads')
plt.legend()
plt.show()


columns = ["number"]

df = pd.read_csv("results/dist.csv", usecols=columns)
dict = {}
for index, row in df.iterrows():
    if row["number"] in dict.keys():
        dict[row["number"]] += 1
    else:
        dict[row["number"]] = 0

x_values = []
y_values = []

for key in dict:
    print(key)
    x_values.append(key)
    y_values.append(dict[key])

print(dict)
plt.bar(x_values, y_values, color ='maroon')
plt.xlabel('integer')
plt.ylabel('number of occurances')
plt.title('Distribution of integers')
plt.legend()
plt.show()

dict = {}
for index, row in df.iterrows():
    if int(row["number"] / 10) in dict.keys():
        dict[int(row["number"] / 10)] += 1
    else:
        dict[int(row["number"] / 10)] = 0

x_values = []
y_values = []

for key in dict:
    x_values.append(key)
    y_values.append(dict[key])

print(dict)
plt.bar(x_values, y_values, color ='maroon')
plt.xlabel('buckets index')
plt.ylabel('number of integers in a bucket')
plt.title('Distribution of integers in buckets')
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
