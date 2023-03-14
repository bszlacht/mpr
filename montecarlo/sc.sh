#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 6
#SBATCH --time=01:00:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr23-cpu

module add scipy-bundle/2021.10-foss-2021b
mpiexec -np 6 ./montec.py
