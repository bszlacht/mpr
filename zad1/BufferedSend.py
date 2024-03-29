import math

from mpi4py import MPI
import numpy as np

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

maxSize = 1000000

N = 1000


def send(size):
    global N

    start_time = MPI.Wtime()
    for i in range(0, N):
        sendBuf = np.empty(size, dtype=np.uint8)
        comm.Bsend(sendBuf, dest=0, tag=123)
        comm.Recv(sendBuf, source=0, tag=123)
    end_time = (MPI.Wtime() - start_time) / N
    return end_time


def receive(size):
    global N

    for i in range(0, N):
        recvBuf = np.empty(size, dtype=np.uint8)
        comm.Recv(recvBuf, source=1, tag=123)
        comm.Bsend(recvBuf, dest=1, tag=123)


def test(maxSizeLocal, p_rank, size):
    comm.Barrier()
    buffer = np.empty(maxSizeLocal * 4, dtype='b')
    MPI.Attach_buffer(buffer)
    if p_rank == 0:
        receive(size)
    else:
        time = send(size)
        mbsize = size / math.pow(10, 6)
        v = mbsize / time
        print(v, size)
    MPI.Detach_buffer()
    del buffer


def test_capacity(p_rank):
    global maxSize
    for size in range(0, 1000000, 10000):
        test(maxSize, p_rank, size)


def test_delay(p_rank):
    global maxSize
    size = 1
    test(maxSize, p_rank, size)


test_delay(rank)
