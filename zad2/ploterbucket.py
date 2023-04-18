import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# columns = ["time", "buck_size"]

# df = pd.read_csv("results/spraw2/numofbuckets.csv", usecols=columns)
# plt.scatter(df.buck_size, df.time, color='r')
# plt.xlabel('number of buckets')
# plt.ylabel('time[s]')
# plt.title('Time plot based on number of buckets')
# plt.legend()
# plt.show()

columns = ["time", "threads"]

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

dfp = pd.read_csv("results/spraw2/sorttime.csv", usecols=columns)
df = dfp.groupby('threads')['time'].agg(['mean', 'std'])

mean_values = df['mean']
std_values = df['std']
plt.errorbar(df.index, mean_values, yerr=std_values, fmt='o', color='r', label='Mean')
plt.xlabel('number of threads')
plt.ylabel('time[s]')
plt.title('Time plot of sorting elements in buckets based on number of threads')
plt.legend()
plt.show()