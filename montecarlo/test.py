#!/usr/bin/env python

from mpi4py import MPI
import random
import sys
import time
import socket
import numpy as np


# random.seed(int(time.time()))

def calculate_pi(number_of_points):
    list_points = generate_points(number_of_points)
    in_p = check_points(list_points)
    pi = 4 * (float(in_p) / float(number_of_points))
    return pi


def generate_points(number_of_points):
    res = []
    # change
    for i in range(number_of_points):
        point = (random.random(), random.random())
        res.append(point)
    return res


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
    # print(points_in)
    data[0] = points_in
    # print(data)
    comm.Reduce([data, MPI.LONG_LONG], None, op=MPI.SUM, root=0)
