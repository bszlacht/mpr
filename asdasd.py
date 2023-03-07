
from mpi4py import MPI
import numpy as np
import csv
# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# size = comm.Get_size()

maxSize = 100000
N = 1000
# Define the buffer size
buf_size = 100000*2

# Allocate memory for the buffer
buffer = np.empty(buf_size, dtype='b')

# Attach the buffer to the process
MPI.Attach_buffer(buffer)
for i in range(0, 1000):
    if rank == 0:
        # Receive the message sent from rank 1
        msg = comm.Irecv(buffer, source=1, tag=123)
        msg.Wait()
        print("Rank 0 received message:", buffer.tobytes())
    else:
        # Prepare a message to be sent
        msg = bytearray(1000)
        # Send the message using MPI.Bsend()
        comm.Bsend([msg, MPI.CHAR], dest=0, tag=123)

# Detach the buffer from the process
MPI.Detach_buffer()

# Free the memory allocated for the buffer
del buffer