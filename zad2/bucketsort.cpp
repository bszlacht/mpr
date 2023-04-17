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

void bucket_sort(vector<int> &v)
{
    const int n = v.size();
    vector<double> buckets[4];

#pragma omp parallel
    {

        int thread_id = omp_get_thread_num();
        int thread_count = omp_get_num_threads();

        int chunk_size = n / thread_count;
        int start = thread_id * chunk_size;
        int end = (thread_id == thread_count - 1) ? n : (thread_id + 1) * chunk_size;

        // Umieszczamy elementy we właściwych kubełkach
        int i = start + 1;
        while (start != i) {
            int bucket_index = 4 * v[i] / 1000;

            if (bucket_index == thread_id)
            {
                buckets[bucket_index].push_back(v[i]);
            }
            i++;
            i = i % n;
        }
        // for (int i = 0; i < n; i++)
        // {
        //     int bucket_index = 4 * v[i] / 1000;

        //     if (bucket_index == thread_id)
        //     {
        //         buckets[bucket_index].push_back(v[i]);
        //     }
                
        // }

        // Sortujemy elementy w każdym kubełku
        #pragma omp for
        for (auto &bucket : buckets)
        {
            sort(bucket.begin(), bucket.end());
        }

        // Łączymy elementy z kubełków w jedną posortowaną tablicę
        int i = 0;
        for (auto &bucket : buckets)
        {
            for (auto &element : bucket)
            {
                v[i++] = element;
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

    string size_string = argv[1];
    char *s_threads = argv[2];
    char *didiver_s = argv[3];
    unsigned long long int size = stoull(size_string);
    int threads = atoi(s_threads);
    vector<int> data = vector<int>(size);
    double divider = atof(didiver_s);

    omp_set_num_threads(threads);
    double start = omp_get_wtime();

    int chunk_size = (int)(size * (divider / 100.0));

#pragma omp parallel default(none) shared(data, size, chunk_size)
    {
        mt19937_64 rng(random_device{}()); // todo czy to jest uniform distribution???
        uniform_int_distribution<int> distribution(1, 1000);

#pragma omp for schedule(static, chunk_size)
        for (int I = 0; I < size; I++)
            data[I] = distribution(rng);
    }

    double exec_time = omp_get_wtime() - start;

    bucket_sort(data);
    for (int i = 0; i < size; i++)
    {
        cout << data[i] << endl;
    }
    return 0;
}
