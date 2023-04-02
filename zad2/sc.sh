# max = 32761316000B, for 1000000000 -> terminate called after throwing an instance of 'std::bad_alloc' what():  std::bad_alloc
# shellcheck disable=SC2034
for ARR_SIZE in `seq 100 10000 100000000`
do
    # shellcheck disable=SC2043
    for THREADS in 1 2 3 4
    do
      ./main $ARR_SIZE $THREADS
    done
done