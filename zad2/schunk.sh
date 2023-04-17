# shellcheck disable=SC2034

for num_of_buckets in {100..100100..100}
do 
./bucketsort 100000 1 $num_of_buckets
done
