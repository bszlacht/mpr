
from mpi4py import MPI
import numpy as np
import csv
# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# size = comm.Get_size()

maxSize = 100
N = 5
# Define the buffer size
buf_size = 100

# Allocate memory for the buffer
buffer = np.empty(buf_size, dtype='b')

# Attach the buffer to the process
MPI.Attach_buffer(buffer)
for i in range(0, N):
    if rank == 0:
        # Receive the message sent from rank 1
        buffer2 = np.empty(buf_size, dtype='b')
        msg = comm.Irecv(buffer2, source=1, tag=123)
        msg.Wait()
        print("Rank 0 received message:", buffer2.tobytes())
    else:
        # Prepare a message to be sent
        msg = b"abcde"
        # Send the message using MPI.Bsend()
        comm.Bsend([msg, MPI.CHAR], dest=0, tag=123)

# Detach the buffer from the process
MPI.Detach_buffer()

# Free the memory allocated for the buffer
del buffer