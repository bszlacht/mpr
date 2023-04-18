# shellcheck disable=SC2034

for num_of_buckets in {10..1000..10}
do 
./bucketsort 1000000 4 $num_of_buckets
done

for num_of_buckets in {1000..1000000..1000}
do 
./bucketsort 1000000 4 $num_of_buckets
done
