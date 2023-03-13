import pandas as pd
from matplotlib import pyplot as plt

columns = ["bandwidth", "bsize"]

# df = pd.read_csv("std_one_node", usecols=columns)
# df1 = pd.read_csv("buf_one_node", usecols=columns)
# plt.plot(df1.bsize, df1.bandwidth, color='r', label='buf_one_node')
# plt.plot(df.bsize, df.bandwidth, color='b', label='std_one_node')
# plt.xlabel('siz e in B')
# plt.ylabel('bandwidth in MB/s')
# plt.title('One node methods comparison')


# df = pd.read_csv("std_two_nodes", usecols=columns)
# plt.plot(df.bsize, df.bandwidth)
# plt.xlabel('size in B')
# plt.ylabel('bandwidth in MB/s')
# plt.title('Standard Send 2:1')

# df = pd.read_csv("buf_two_nodes", usecols=columns)
# plt.plot(df.bsize, df.bandwidth)
# plt.xlabel('size in B')
# plt.ylabel('bandwidth in MB/s')
# plt.title('Buffered Send 2:1')

df = pd.read_csv("std_two_nodes", usecols=columns)
df1 = pd.read_csv("buf_two_nodes", usecols=columns)
plt.plot(df1.bsize, df1.bandwidth, color='r', label='buf_two_nodes')
plt.plot(df.bsize, df.bandwidth, color='b', label='std_one_nodes')
plt.xlabel('siz e in B')
plt.ylabel('bandwidth in MB/s')
plt.title('Two nodes methods comparison')

plt.show()

# plt.savefig('4.png')
