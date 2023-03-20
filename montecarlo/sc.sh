#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --time=06:00:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr23-cpu

module add scipy-bundle/2021.10-foss-2021b
chmod +x ./montec.py
# shellcheck disable=SC2034
for SIZE in 2500000000 3162277 1000
do
    # shellcheck disable=SC2043
    for THREADS in 12
    do
      mpiexec -np $THREADS ./montec.py $SIZE
    done
done