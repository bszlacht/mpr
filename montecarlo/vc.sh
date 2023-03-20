#!/bin/bash -l
chmod +x montec.py
for THREADS in 1 2 3 4 5 6 7 8 9 10 11 12
do
  mpiexec -machinefile ./allnodes -np $THREADS ./montec.py 100000
done
