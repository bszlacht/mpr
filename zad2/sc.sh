# max = 32761316000B
# shellcheck disable=SC2034
for ARR_SIZE in 100 1000 10000 100000 1000000 10000000 100000000 1000000000
do
    # shellcheck disable=SC2043
    for THREADS in 1 2 3 4
    do
      ./main $ARR_SIZE $THREADS
    done
done