from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = 'data'
    comm.send(data, dest=1, tag=15)
elif rank == 1:
    data = comm.recv(source=0, tag=15)
