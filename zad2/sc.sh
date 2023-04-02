# max = 32761316000B, for 1000000000 -> terminate called after throwing an instance of 'std::bad_alloc' what():  std::bad_alloc
# shellcheck disable=SC2034
count=0
total=100
pstr="[=======================================================================]"

for ARR_SIZE in `seq 100 1000000 100000000`
do
    # shellcheck disable=SC2043
    for THREADS in 1 2 3 4
    do
      #./main $ARR_SIZE $THREADS
      sleep 0.5 # this is work
      count=$(( $count + 1 ))
      pd=$(( $count * 73 / $total ))
      printf "\r%3d.%1d%% %.${pd}s" $(( $count * 100 / $total )) $(( ($count * 1000 / $total) % 10 )) $pstr
    done
done