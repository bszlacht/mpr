#!/bin/bash -l
chmod +x montec.py
for THREADS in 12 11 10 9 8 7 6 5 4 3 2 1
do
  mpiexec -machinefile ./allnodes -np $THREADS ./montec.py 5000000
done
