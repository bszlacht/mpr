#include <iostream>
#include <cstdlib>
#include <random>
#include <string>
#include <omp.h>
#include <typeinfo>
#include <algorithm>

using namespace std;

double times[4];

void bucket_sort(vector<long long> &v, long long number_of_buckets, int threads)
{
    // ściągamy rozmiar tablicy i tworzymy kubełki
    const long long n = v.size();
    vector<vector<long long>> buckets(number_of_buckets);

    double start_time_putting_in_buckets;
    double start_time_sorting_elelements;
    double start_time_writing;

#pragma omp parallel
    {
        // id i ilość wątków
        int thread_id = omp_get_thread_num();
        long long thread_count = omp_get_num_threads();

// *** WRITING INTO BUCKETS ***
#pragma omp master
        {
            start_time_putting_in_buckets = omp_get_wtime();
        }

        // definiujemy zakresy kubełka
        long long thread_offset = n / thread_count;
        long long bucket_lower = thread_id * (number_of_buckets / thread_count);
        long long bucket_upper = (thread_id + 1) * (number_of_buckets / thread_count);

        if (thread_id == thread_count - 1)
            bucket_upper = number_of_buckets;

        // Umieszczamy elementy we właściwych kubełkach iterując przez całą tablicę zaczynają od innego elementu
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

#pragma omp master
        {
            times[1] = omp_get_wtime() - start_time_putting_in_buckets;
        }

        // bariera, ponieważ może być tak, że jakiś wątke skończy pracę szybciej a teraz będziemy sortować buckety więc nie chcemy żeby był wyścig
#pragma omp barrier

// *** SORTING BUCKETS ***
#pragma omp master
        {
            start_time_sorting_elelements = omp_get_wtime();
        }
#pragma omp for schedule(static)
        for (int i = 0; i < number_of_buckets; i++)
        {
            sort(buckets[i].begin(), buckets[i].end());
        }

#pragma omp master
        {
            times[2] = omp_get_wtime() - start_time_sorting_elelements;
        }

// *** WRITING INTO RESULT LIST ***
#pragma omp master
        {
            start_time_writing = omp_get_wtime();
        }
        // Wpisywanie posortowanych bucketów do tablicy
        // Dla każdego wątku będzie różny start = i
        // każdy policzy sobie prefix sum i na jego podstawie powpisuje odpowiednie buckety na odpowiednie miejsca
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
#pragma omp master
        {
            times[3] = omp_get_wtime() - start_time_writing;
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
    double start, end;
    start = omp_get_wtime();
    bucket_sort(data, number_of_buckets, threads);
    end = omp_get_wtime();
    times[0] = end - start;

    // Sprawdzanie czy posortowana
    for (int i = 0; i < arr_size - 1; i++)
    {
        if (data[i + 1] < data[i])
        {
            cout << "ERROR" << endl;
        }
    }
    // for(int i = 0; i < 4; i++) {
    cout << threads << "," << times[1] << endl;
    // }
    // Koniec programu
    return 0;
}