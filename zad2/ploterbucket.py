import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["time", "buck_size"]

df = pd.read_csv("results/spraw2/numofbuckets.csv", usecols=columns)
plt.scatter(df.buck_size, df.time, color='r')
plt.xlabel('number of buckets')
plt.ylabel('time[s]')
plt.title('Time plot based on number of buckets')
plt.legend()
plt.show()

columns = ["time","threads"]

df = pd.read_csv("results/spraw2/wholetime.csv", usecols=columns)
plt.scatter(df.threads, df.time, color='r')
plt.xlabel('number of threads')
plt.ylabel('time[s]')
plt.title('Time plot based on number of threads')
plt.legend()
plt.show()
