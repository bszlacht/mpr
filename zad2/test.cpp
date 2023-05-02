#include <iostream>
#include <cstdlib>
#include <random>
#include <string>
#include <omp.h>
#include <typeinfo>
#include <algorithm>

using namespace std;


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

    for (int i = 0; i < arr_size; i++)
            cout << data[i] << endl;
    // Koniec programu
    return 0;
}