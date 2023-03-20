#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --time=06:00:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr23-cpu

module add scipy-bundle/2021.10-foss-2021b
chmod +x ./montec.py
# shellcheck disable=SC2034
for SIZE in 5000000000 10000000 500
do
    for THREADS in 12 11 10 9 8 7 6 5 4 3 2 1
    do
      mpiexec -np $THREADS ./montec.py $SIZE
    done
done