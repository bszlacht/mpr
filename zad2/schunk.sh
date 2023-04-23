# shellcheck disable=SC2034
for rep in {1..100..1}
do
    for threads in {1..4..1}
    do
        ./bucketsort 1000000 $threads 1000
    done
done

