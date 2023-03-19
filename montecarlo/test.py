#!/usr/bin/env python

from mpi4py import MPI
import random
import sys
import socket
import numpy as np


def check_points(number_of_points):
    points_in_circle = 0
    for i in range(number_of_points):
        p = (random.random(), random.random())
        if p[0] * p[0] + p[1] * p[1] < 1:
            points_in_circle += 1
    return points_in_circle


points_num = np.longlong(sys.argv[1])

comm = MPI.COMM_WORLD
number_of_processes = comm.Get_size()
points_to_gen = points_num // number_of_processes

print("my rank is: %d, at node %s" % (comm.rank, socket.gethostname()))

data = np.zeros(1, dtype=np.longlong)

if comm.rank == 0:
    totals = np.zeros_like(data)
    comm.Barrier()

    start = MPI.Wtime()

    points_in = check_points(points_to_gen)
    data[0] = points_in
    comm.Reduce([data, MPI.LONG_LONG], [totals, MPI.LONG_LONG], op=MPI.SUM, root=0)
    pi = 4 * (totals[0] / points_num)
    stop = MPI.Wtime()
    result = stop - start
    print(result)
    print(pi)

else:
    comm.Barrier()
    points_in = check_points(points_to_gen)
    data[0] = points_in
    comm.Reduce([data, MPI.LONG_LONG], None, op=MPI.SUM, root=0)
