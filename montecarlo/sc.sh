#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --time=01:00:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr23-cpu

module add scipy-bundle/2021.10-foss-2021b
chmod +x ./montec.py
# shellcheck disable=SC2034
for K in 1 2 3 4 5 .. 20
do
  for SIZE in 10000000000 10000000 1000
  do
    for THREADS in 12 11 10 9 8 7 6 5 4 3 2 1
    do
      mpiexec -np $THREADS ./montec.py $SIZE
    done
  done
done