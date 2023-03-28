#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --time=06:00:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr23-cpu

module add scipy-bundle/2021.10-foss-2021b
chmod +x ./montecweak.py
# shellcheck disable=SC2034
for SIZE in 2500000000 1581138 1000
do
    # shellcheck disable=SC2043
    for THREADS in 1 2 3 4 5 6 7 8 9 10 11 12
    do
      mpiexec -np $THREADS ./montecweak.py $SIZE
    done
done