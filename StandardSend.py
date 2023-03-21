from mpi4py import MPI
import numpy as np
import math

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

N = 1000


def send(size):
    global N

    start_time = MPI.Wtime()
    for i in range(0, N):
        sendBuf = np.empty(size, dtype=np.uint8)
        comm.Send(sendBuf, dest=0, tag=123)
        comm.Recv(sendBuf, source=0, tag=123)
    end_time = (MPI.Wtime() - start_time) / N
    return end_time


def receive(size):
    global N

    for i in range(0, N):
        recvBuf = np.empty(size, dtype=np.uint8)
        comm.Recv(recvBuf, source=1, tag=123)
        comm.Send(recvBuf, dest=1, tag=123)


def test(p_rank, size):
    comm.Barrier()
    if p_rank == 0:
        receive(size)
    else:
        time = send(size)
        mbsize = size / math.pow(10, 6)
        v = mbsize / time
        print(v, size)


def test_capacity(p_rank):
    for size in range(0, 1100000, 10000):
        test(p_rank, size)


def test_delay(p_rank):
    size = 1
    test(p_rank, size)


test_delay(rank)
