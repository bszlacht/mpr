import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["n", "time"]

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

# df = pd.read_csv("std_two_nodes", usecols=columns)
# df1 = pd.read_csv("buf_two_nodes", usecols=columns)
# plt.scatter(df1.bsize, df1.bandwidth, color='r', label='buf_two_nodes')
# plt.scatter(df.bsize, df.bandwidth, color='b', label='std_two_nodes')
# plt.xlabel('size in B')
# plt.ylabel('bandwidth in MB/s')
# plt.title('Two nodes methods comparison')
# plt.show()
#
# df = pd.read_csv("std_one_node", usecols=columns)
# df1 = pd.read_csv("buf_one_node", usecols=columns)
# plt.scatter(df1.bsize, df1.bandwidth, color='r', label='buf_one_node')
# plt.scatter(df.bsize, df.bandwidth, color='b', label='std_one_node')
# plt.xlabel('size in B')
# plt.ylabel('bandwidth in MB/s')
# plt.title('One node methods comparison')
#
# plt.show()

# plt.savefig('4.png')
# X = ['One Node', 'Two Nodes']
# Send = [1 / (0.1197414639716798 * 10 ** 3), 1 / (0.008171778041448212 * 10 ** 3)]
# Bsend = [1 / (0.06692255161630022 * 10 ** 3), 1 / (0.006422658058825691 * 10 ** 3)]
#
# X_axis = np.arange(len(X))
#
# plt.bar(X_axis - 0.2, Send, 0.4, label='Standard Send', color='b')
# plt.bar(X_axis + 0.2, Bsend, 0.4, label='Buffered Send', color='r')
#
# plt.xticks(X_axis, X)
# plt.xlabel("Nodes")
# plt.ylabel("Delay [ms]")
# plt.title("Delay in ms for 1B message size")
# plt.legend()
# plt.show()

df = pd.read_csv("montecarlo/results/skalowanieslabevc", usecols=columns)
plt.scatter(df.n, df.time)
plt.xlabel('number of processors')
plt.ylabel('time [s]')
plt.title('Time plot on vCluster')
plt.show()