# shellcheck disable=SC2034
count=0
total=20
pstr="[=======================================================================]"

for CHUNK in `seq 5 5 100`
do
    ./main 100000000 4 $CHUNK
    count=$(( $count + 1 ))
    pd=$(( $count * 73 / $total ))
    printf "\r%3d.%1d%% %.${pd}s" $(( $count * 100 / $total )) $(( ($count * 1000 / $total) % 10 )) $pstr
done