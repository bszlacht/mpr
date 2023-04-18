import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


columns = ["time", "threads"]

df = pd.read_csv("results/spraw2/wholetime.csv", usecols=columns)
plt.scatter(df.threads, df.time[0]/df.time, color='r')
plt.xlabel('number of threads')
plt.ylabel('Speedup')
plt.title('Speedup of whole bucket sort execution based on number of threads')
plt.legend()
plt.show()

dfp = pd.read_csv("results/spraw2/putinbucket.csv", usecols=columns)
df = dfp.groupby('threads')['time'].agg(['mean', 'std'])
df.reset_index(inplace=True)
mean_values = df['mean']
speedup_put = mean_values[0] / mean_values
plt.scatter(df.index, speedup_put, color='r')
plt.xlabel('number of threads')
plt.ylabel('Speedup')
plt.title('Speedup of putting elements into buckets based on number of threads')
plt.legend()
plt.show()

dfp = pd.read_csv("results/spraw2/sorttime.csv", usecols=columns)
df = dfp.groupby('threads')['time'].agg(['mean', 'std'])

df.reset_index(inplace=True)
mean_values = df['mean']
speedup_put = mean_values[0] / mean_values
plt.scatter(df.index, speedup_put, color='r')
plt.xlabel('number of threads')
plt.ylabel('Speedup')
plt.title('Speedup of sorting elements in buckets based on number of threads')
plt.legend()
plt.show()

dfp = pd.read_csv("results/spraw2/writingtime.csv", usecols=columns)
df = dfp.groupby('threads')['time'].agg(['mean', 'std'])
df.reset_index(inplace=True)
mean_values = df['mean']
speedup_put = mean_values[0] / mean_values
plt.scatter(df.index, speedup_put, color='r')
plt.xlabel('number of threads')
plt.ylabel('Speedup')
plt.title('Speedup of writing sorted elements from buckets to array based on number of threads')
plt.legend()
plt.show()


dfp = pd.read_csv("results/spraw2/fixedwholetime.csv", usecols=columns)
df = dfp.groupby('threads')['time'].agg(['mean', 'std'])

mean_values = df['mean']
std_values = df['std']
plt.errorbar(df.index, mean_values[0] /
             mean_values, color='r')
plt.xlabel('number of threads')
plt.ylabel('Speedup')
plt.title('Speedup of bucketsort based on number of threads')
plt.legend()
plt.show()
