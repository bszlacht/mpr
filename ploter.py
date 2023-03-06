import pandas as pd
from matplotlib import pyplot as plt

columns = ["bandwidth", "bsize"]
df = pd.read_csv("std_one_node", usecols=columns)
plt.plot(df.bsize, df.bandwidth)
plt.xlabel('size in B')
plt.ylabel('bandwidth in B/s')
plt.show()