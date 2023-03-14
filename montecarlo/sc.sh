#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 6
#SBATCH --time=00:03:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr23-cpu
module add scipy-bundle/2021.10-foss-2021b
chmod +x montec.py
mpiexec -np 6 ./montec.py