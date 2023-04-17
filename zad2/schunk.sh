# shellcheck disable=SC2034

for num_of_buckets in {1000..100000000..1000}
do 
./bucketsort 100000000 1 $num_of_buckets
done
