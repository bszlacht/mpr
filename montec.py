import random
import math
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# todo startuj generator z roznego poczatkowego ziarna
# todo pokazac dokladnosc
# todo pokazac ze ze wzrostem ilosci punktow wzrasta dokladnosc pi
def generate_points(n):
    inCount = 0
    for i in range(0, n):
        x, y = random.random(), random.random()
        d = math.sqrt(pow(x, 2) + pow(y, 2))
        if d < 1:
            inCount += 1
    return inCount


def monte_carlo(rank):

    n = 1000
    inCount = generate_points(n)
    res = 4 * inCount/n
    print(res)


monte_carlo(rank)