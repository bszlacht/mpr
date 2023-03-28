import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

columns = ["n", "time"]

dfbig_w = pd.read_csv("resultsares/strongscaling/big", usecols=columns)
dfmedium_w = pd.read_csv("resultsares/strongscaling/medium", usecols=columns)
dfsmall_w = pd.read_csv("resultsares/strongscaling/small", usecols=columns)

dfbig_w = pd.read_csv("resultsares/weakscaling/big", usecols=columns)
dfmedium_w = pd.read_csv("resultsares/weakscaling/medium", usecols=columns)
dfsmall_w = pd.read_csv("resultsares/weakscaling/small", usecols=columns)

dfbig_w = dfbig_w.groupby(['n'], as_index=False).agg({'time': 'mean'})
dfmedium_w = dfmedium_w.groupby(['n'], as_index=False).agg({'time': 'mean'})
dfsmall_w = dfsmall_w.groupby(['n'], as_index=False).agg({'time': 'mean'})

dfbig_w = dfbig_w.groupby(['n'], as_index=False).agg({'time': 'mean'})
dfmedium_w = dfmedium_w.groupby(['n'], as_index=False).agg({'time': 'mean'})
dfsmall_w = dfsmall_w.groupby(['n'], as_index=False).agg({'time': 'mean'})

sp_1_bs = dfbig_w.iloc[0]['time']
sp_1_ms = dfmedium_w.iloc[0]['time']
sp_1_ss = dfsmall_w.iloc[0]['time']

sp_1_bw = dfbig_w.iloc[0]['time']
sp_1_mw = dfmedium_w.iloc[0]['time']
sp_1_sw = dfsmall_w.iloc[0]['time']

plt.scatter(dfbig_w.n, dfbig_w.time, color='r', label='big')
plt.scatter(dfbig_w.n, dfmedium_w.time, color='g', label='medium')
plt.scatter(dfbig_w.n, dfsmall_w.time, color='b', label='small')
plt.xlabel('number of processors')
plt.ylabel('time [s]')
plt.title('Weak scaling time plot on Ares')
plt.legend()
plt.yscale("log")
plt.show()

plt.scatter(dfbig_w.n, dfbig_w.n * sp_1_bs / dfbig_w.time, color='r', label='big')
plt.scatter(dfbig_w.n, dfbig_w.n * sp_1_ms / dfmedium_w.time, color='g', label='medium')
plt.scatter(dfbig_w.n, dfbig_w.n * sp_1_ss / dfsmall_w.time, color='b', label='small')
plt.xlabel('number of processors')
plt.ylabel('speedup')
plt.title('Weak scaling speedup plot on Ares')
plt.legend()
plt.show()

plt.scatter(dfbig_w.n, sp_1_bs / (dfbig_w.time), color='r', label='big')
plt.scatter(dfbig_w.n, sp_1_ms / (dfmedium_w.time), color='g', label='medium')
plt.scatter(dfbig_w.n, sp_1_ss / (dfsmall_w.time), color='b', label='small')
plt.xlabel('number of processors')
plt.ylabel('efficiency')
plt.title('Weak scaling efficiency plot on Ares')
plt.legend()
plt.show()

spbs = dfbig_w.n * sp_1_bs / dfbig_w.time
spms = dfbig_w.n * sp_1_ms / dfmedium_w.time
spss = dfbig_w.n * sp_1_ss / dfsmall_w.time
plt.scatter(dfbig_w.n, (1 / spbs - 1 / dfbig_w.n) / (1 - 1 / dfbig_w.n), color='r', label='big')
plt.scatter(dfbig_w.n, (1 / spms - 1 / dfbig_w.n) / (1 - 1 / dfbig_w.n), color='g', label='medium')
plt.scatter(dfbig_w.n, (1 / spss - 1 / dfbig_w.n) / (1 - 1 / dfbig_w.n), color='b', label='small')
plt.xlabel('number of processors')
plt.ylabel('Serial fraction')
plt.title('Weak scaling serial fraction plot on Ares')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-')
plt.show()
