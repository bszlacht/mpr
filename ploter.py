import pandas as pd
from matplotlib import pyplot as plt

columns = ["bandwidth", "bsize"]

# df = pd.read_csv("std_one_node", usecols=columns)
# plt.plot(df.bsize, df.bandwidth)
# plt.xlabel('siz e in B')
# plt.ylabel('bandwidth in MB/s')
# plt.title('Standard Send 1:2')


# df = pd.read_csv("std_two_nodes", usecols=columns)
# plt.plot(df.bsize, df.bandwidth)
# plt.xlabel('size in B')
# plt.ylabel('bandwidth in MB/s')
# plt.title('Standard Send 2:1')


# df = pd.read_csv("buf_one_node", usecols=columns)
# plt.plot(df.bsize, df.bandwidth)
# plt.xlabel('size in B')
# plt.ylabel('bandwidth in MB/s')
# plt.title('Buffered Send 1:2')

df = pd.read_csv("buf_two_nodes", usecols=columns)
plt.plot(df.bsize, df.bandwidth)
plt.xlabel('size in B')
plt.ylabel('bandwidth in MB/s')
plt.title('Buffered Send 2:1')

plt.show()

# plt.savefig('4.png')
