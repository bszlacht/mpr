from mpi4py import MPI
import numpy as np
import csv

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# size = comm.Get_size()

maxSize = 100000
N = 1000


def send(size):
    global N

    start_time = MPI.Wtime()
    for i in range(0, N):
        sendBuf = np.empty(size, dtype=np.uint8)
        comm.Send(sendBuf, dest=0, tag=123)
        comm.Recv(sendBuf, source=0, tag=123)
    end_time = (MPI.Wtime() - start_time)/N
    return end_time


def receive(size):
    global N

    for i in range(0, N):
        recvBuf = np.empty(size, dtype=np.uint8)
        comm.Recv(recvBuf, source=1, tag=123)
        comm.Send(recvBuf, dest=1, tag=123)


def test(p_rank):
    global maxSize
    for size in range(1, maxSize, 1000):
        comm.Barrier()
        if p_rank == 0:
            receive(size)
        else:
            time = send(size)
            mbsize = size/(10^6)
            print(str(mbsize/time) + "," + str(size))


test(rank)

# # Define the buffer size
# buf_size = 1024
#
# # Allocate memory for the buffer
# buffer = np.empty(buf_size, dtype='b')
#
# # Attach the buffer to the process
# MPI.Attach_buffer(buffer)
#
# if rank == 0:
#     # Receive the message sent from rank 1
#     msg = comm.Irecv(buffer, source=1, tag=123)
#     msg.Wait()
#     print("Rank 0 received message:", buffer.tobytes())
# else:
#     # Prepare a message to be sent
#     msg = b"Hello from rank " + str(rank).encode()
#     # Send the message using MPI.Bsend()
#     comm.Bsend([msg, MPI.CHAR], dest=0, tag=123)
#
# # Detach the buffer from the process
# MPI.Detach_buffer()
#
# # Free the memory allocated for the buffer
# del buffer
