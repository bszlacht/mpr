#!/usr/bin/env python

import random
from mpi4py import MPI
import sys
import numpy as np

# mpi4py global variables
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# number of points to generate
n = np.longlong(sys.argv[1])
# points_for_this_proces = n // size
points_for_this_proces = n

# variable that will hold reduced data
global_data = np.zeros(1, dtype=np.longlong)


def generate_points(n_local):
    inCount = 0
    # random.seed(rank)
    for i in range(n_local):
        x, y = random.random(), random.random()
        d = x * x + y * y
        if d < 1:
            inCount += 1
    return inCount


if rank == 0:
    print("COMM.SIZE = " + str(size) + " n = " + str(n))
    all_points_in = np.zeros_like(global_data)
    comm.Barrier()

    start_time = MPI.Wtime()

    points_in = generate_points(points_for_this_proces)
    global_data[0] = points_in
    comm.Reduce([global_data, MPI.LONG_LONG], [all_points_in, MPI.LONG_LONG], op=MPI.SUM, root=0)
    pi = 4 * all_points_in / (n * size)  # weak
    # pi = 4 * all_points_in / n # strog
    end_time = (MPI.Wtime() - start_time)
    print(end_time)
    print(pi)
else:
    comm.Barrier()
    points_in = generate_points(points_for_this_proces)
    global_data[0] = points_in
    comm.Reduce([global_data, MPI.LONG_LONG], None, op=MPI.SUM, root=0)
