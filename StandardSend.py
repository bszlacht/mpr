from mpi4py import MPI
import numpy as np
import csv

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank
# size = comm.Get_size()

maxSize = 10000
N = 100


def send(size):
    global N
    start_time = MPI.Wtime()
    for i in range(0, N):
        sendBuf = np.ones(size, dtype=np.uint8)
        comm.Send(sendBuf, dest=1, tag=123)
        comm.Recv(sendBuf, source=1, tag=MPI.ANY_TAG)
    end_time = (MPI.Wtime() - start_time)/N
    return end_time


def receive(size):
    global N
    for i in range(0, N):
        recvBuf = np.empty(size, dtype=np.uint8)
        comm.Recv(recvBuf, source=0, tag=MPI.ANY_TAG)
        comm.Send(recvBuf, dest=0, tag=123)


def test(p_rank):
    global maxSize

    for size in range(1, maxSize, 100):
        if p_rank == 0:
            time = send(size)
            print(str(size/time) + " <- B/S | standard send | B ->" + str(size))
        else:
            receive(size)


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
