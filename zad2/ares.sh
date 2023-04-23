#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --time=06:00:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr23-cpu


module add gcc/10.3.0

g++ -std=c++11 -fopenmp -o bucketsort bucketsort.cpp

for rep in {1..20..1}
do
    for threads in {1..12..1}
    do
        ./bucketsort 1000000 $threads 1000
    done
done
