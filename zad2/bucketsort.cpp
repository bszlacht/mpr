#include <iostream>
#include <cstdlib>
#include <random>
#include <string>
#include <omp.h>
#include <typeinfo>
#include <algorithm>

using namespace std;

void bucket_sort(vector<long long> &v, long long number_of_buckets, int threads)
{
    // ściągamy rozmiar tablicy i tworzymy kubełki
    const long long n = v.size();
    vector<vector<long long>> buckets(number_of_buckets);
#pragma omp parallel
    {
        // id i ilość wątków
        int thread_id = omp_get_thread_num();
        long long thread_count = omp_get_num_threads();
        // definiujemy zakresy kubełka
        long long thread_offset = n / thread_count; // 33

        long long bucket_lower = thread_id * (number_of_buckets / thread_count);
        long long bucket_upper = (thread_id + 1) * (number_of_buckets / thread_count);

        if (thread_id == thread_count - 1)
            bucket_upper = number_of_buckets;

        // Umieszczamy elementy we właściwych kubełkach

        for (long long i = thread_offset; i < n; ++i)
        {
            long long bucket_index = (number_of_buckets * v[i]) / n;
            if (bucket_index >= bucket_lower && bucket_index < bucket_upper)
            {
                buckets[bucket_index].push_back(v[i]);
            }
        }
        for (long long i = 0; i < thread_offset; ++i)
        {
            long long bucket_index = (number_of_buckets * v[i]) / n;
            if (bucket_index >= bucket_lower && bucket_index < bucket_upper)
            {
                buckets[bucket_index].push_back(v[i]);
            }
        }

#pragma omp barrier
#pragma omp for schedule(static)
        for (int i = 0; i < number_of_buckets; i++)
        {
            sort(buckets[i].begin(), buckets[i].end());
        }

        int last_bucket = 0;
        int prev_buckets_sizes = 0;
#pragma omp for schedule(static)
        for (int i = 0; i < number_of_buckets; i++)
        {

            for (int j = last_bucket; j < i; j++)
            {
                prev_buckets_sizes += buckets[j].size();
            }
            last_bucket = i;
            int e = prev_buckets_sizes;
            for (int k = 0; k < buckets[i].size(); k++)
            {
                v[e] = buckets[i][k];
                e++;
            }
        }
    }
}

int main(int argc, char **argv)
{

    if (argc != 4)
    {
        printf("invalid number of arguments");
        return 1;
    }
    //  Pobranie parametrów programu
    unsigned long long int arr_size = stoull(argv[1]);
    int threads = atoi(argv[2]);
    int number_of_buckets = atoi(argv[3]);

    // Stworzenie tablicy do posortowania
    vector<long long> data = vector<long long>(arr_size);

    // Ustalenie ilości działających wątków
    omp_set_dynamic(0);
    omp_set_num_threads(threads);

    // Wielkokść chunka tj. jaką porcję w forze dostanie każdy wątek
    // Generator seedujemy osobno dla każdego wątku
#pragma omp parallel default(none) shared(data, arr_size)
    {
        mt19937_64 rng(random_device{}());
        uniform_int_distribution<long long> distribution(1, arr_size - 1);

        // Losowanie liczb do tablicy
#pragma omp for schedule(static)
        for (int I = 0; I < arr_size; I++)
            data[I] = distribution(rng);
    }

    // Wywołanie współbieżnego sortowania

    bucket_sort(data, number_of_buckets, threads);
    // Wypisanie tablicy
    for (int i = 0; i < arr_size - 1; i++)
    {
        if(data[i+1] < data[i]) {
            cout <<"ERROR" <<endl;
        }
    }
    // Koniec programu
    return 0;
}