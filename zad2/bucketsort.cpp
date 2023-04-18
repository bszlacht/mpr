#include <iostream>
#include <cstdlib>
#include <random>
#include <string>
#include <omp.h>
#include <typeinfo>
#include <algorithm>

using namespace std;

/*

        ! wrzucanie elementów do kubełków
        todo sekwencyjny problem zbadac, jak wplywac wielkosc kubelkow na czas problemu, znalezc optimum i uzyc w rownoleglym
        todo wazne, im wiecej kubelkow to mniejsza szansa ze watek sie zatrzyma na locku (wariant 2 algorytmu)
        todo w 3 wariancie kubelki mniejsze
        int thread_id = omp_get_thread_num();
        int thread_count = omp_get_num_threads();

        int start_index = (size / thread_count) * thread_id;
        int end_index = (thread_id == thread_count - 1) ? size : (size / thread_count) * (thread_id + 1);

        int num_buckets = 1000;
        for (int i = start_index; i < end_index; i++)
        {
            int bucket_index = arr[i] / (size / num_buckets);
            bucket_sizes[bucket_index]++;
        }
*/

void bucket_sort(vector<long long> &v, long long number_of_buckets, int threads)
{
    // ściągamy rozmiar tablicy i tworzymy kubełki
    const long long n = v.size();
    vector<vector<double>> buckets(number_of_buckets);

    // double start, end;
    // start = omp_get_wtime();
#pragma omp parallel
    {
        // id i ilość wątków
        int thread_id = omp_get_thread_num();
        long long thread_count = omp_get_num_threads();
        // definiujemy zakresy kubełka
        long long chunk_size = n / thread_count; // 33

        int start = thread_id * chunk_size; // 0 33 66
        int end = (thread_id == thread_count - 1) ? n : (thread_id + 1) * chunk_size; // 33 66 100
        // Umieszczamy elementy we właściwych kubełkach
        int i = start;
        do
        {
            long long bucket_index = (number_of_buckets * v[i]) / n;

            if (v[i] >= start && v[i] < end)
            {
                // cout << thread_id << " wpisal do -> " << bucket_index << "\n";
                buckets[bucket_index].push_back(v[i]);
            }
            i++;
            i = i % n;
        } while (start != i);
// end = omp_get_wtime();
// cout << end - start << "," << threads << endl;

// #pragma omp parallel
//     {
// int thread_id = omp_get_thread_num();
// long long thread_count = omp_get_num_threads();
#pragma omp barrier
#pragma omp for schedule(static)
        for (int i = 0; i < number_of_buckets; i++)
        {
            sort(buckets[i].begin(), buckets[i].end());
        }
        // Łączymy elementy z kubełków w jedną posortowaną tablicę
        int start_idx = 0;
        int bucket_idx = (number_of_buckets / thread_count) * thread_id;
        int range_of_buckets = (number_of_buckets / thread_count);
        for (int i = 0; i < bucket_idx; i++)
        {
            start_idx += buckets[i].size();
        }

        for (int i = bucket_idx; i < bucket_idx + range_of_buckets; i++)
        {
            for (auto &elem : buckets[i])
            {
                v[start_idx++] = elem;
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
    // for (int i = 0; i < arr_size; i++)
    // {
    //     cout << data[i] << endl;
    // }
    // Koniec programu
    return 0;
}