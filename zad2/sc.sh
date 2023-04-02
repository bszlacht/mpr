# shellcheck disable=SC2034
for ARR_SIZE in 100 1000 10000 100000 1000000 10000000 100000000
do
    # shellcheck disable=SC2043
    for THREADS in 1 2 3 4 5 6 7 8 9 10 11 12
    do
      ./main $ARR_SIZE $THREADS
    done
done