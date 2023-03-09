from mpi4py import MPI
import numpy as np
import csv

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# size = comm.Get_size()

maxSize = 1000000

N = 1000

size_array = [1, 10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 10000, 12000, 16000, 22000, 40000, 60000, 1000000]


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


def test(p_rank):
    global maxSize
    for size in range(0, 1000000, 10000):
        comm.Barrier()

        buffer = np.empty(maxSize * 4, dtype='b')
        MPI.Attach_buffer(buffer)

        if p_rank == 0:
            receive(size)
        else:
            time = send(size)
            print('size = %d | time = %f' % (size, time))

            mbsize = size / (10 ** 6)
            print(str(mbsize / time) + "," + str(size))

        MPI.Detach_buffer()
        del buffer


test(rank)
