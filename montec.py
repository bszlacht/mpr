import random
import math
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
n = 10000000


# todo pokazac dokladnosc
# todo pokazac ze ze wzrostem ilosci punktow wzrasta dokladnosc pi

def generate_points(n_local):
    inCount = 0
    for i in range(n_local):
        random.seed(rank * n_local + i)
        x, y = random.random(), random.random()
        d = math.sqrt(pow(x, 2) + pow(y, 2))
        if d < 1:
            inCount += 1
    return inCount


def monte_carlo():
    inCount = generate_points(n // size)
    inCountAll = comm.reduce(inCount, op=MPI.SUM, root=0)
    comm.Barrier()
    if rank == 0:
        pi_estimate = 4 * inCountAll / n
        print("Estimated value of pi:", pi_estimate)

start_time = MPI.Wtime()
monte_carlo()
end_time = (MPI.Wtime() - start_time)
