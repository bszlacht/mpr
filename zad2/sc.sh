# shellcheck disable=SC2034
for ARR_SIZE in 4095164500 2047582250 1023791125 5511895562
do
    # shellcheck disable=SC2043
    # 1 2 3 4 5 6 7 8 9 10 11
    for THREADS in 12
    do
      ./main ARR_SIZE THREADS
    done
doneasd