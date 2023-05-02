import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["N","RAND","DIST","SORT","REDIST","TOTAL"]

df = pd.read_csv("results/times.csv", usecols=columns)

plt.scatter(df.N, df.TOTAL, color='r', label='WHOLE BUCKETSORT')
plt.scatter(df.N, df.REDIST, color='b', label='INSERTING INTO BUCKETS')
plt.scatter(df.N, df.SORT, color='g', label='SORTING BUCKETS')
plt.scatter(df.N, df.DIST, color='#9c1dbf', label='WRITING TO RESULT')
plt.xlabel('number of threads')
plt.ylabel('time[s]')
plt.title('Time plot based on number of threads')
plt.legend()
plt.show()



df = pd.read_csv("results/speedup.csv", usecols=columns)


plt.scatter(df.N, df.TOTAL, color='r', label='WHOLE BUCKETSORT')
plt.scatter(df.N, df.REDIST, color='b', label='INSERTING INTO BUCKETS')
plt.scatter(df.N, df.SORT, color='g', label='SORTING BUCKETS')
plt.scatter(df.N, df.DIST, color='#9c1dbf', label='WRITING TO RESULT')
plt.xlabel('number of threads')
plt.ylabel('time[s]')
plt.title('Speedup plot based on number of threads')
plt.legend()
plt.show()
