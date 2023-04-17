# shellcheck disable=SC2034

for num_of_buckets in {100..1000000..100}
do 
./bucketsort 1000000 1 $num_of_buckets
done
