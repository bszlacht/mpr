time = 0.000285
size =  990000
mbsize = size / (10 ** 6)
v = mbsize / time
print('size = %d | time = %f' % (size, time))
print('{:.12f},{}'.format(v, size))
