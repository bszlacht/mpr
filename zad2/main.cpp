#include <iostream>
#include <cstdlib>
#include <random>
#include <string>
#include <omp.h>
#include <typeinfo>

using namespace std;

// g++ 1.cpp -o 1 -std=c++11 -fopenmp
/*
Wykresy:
  1. Przyspieszenie(rozmiar)
  2. CzasWykonania(rozmiar)
Wykresy dla różnych:
  -> ustawien 'schedule' min. 5 różnych, parametr chunk
  -> wielkosci problemu = wielkosc zaalokowanej tablicy (trzeba dodac jaki to % max mozliwosci sprzetu)
  -> wnioski opisujaca klauzule 'schedule'

32761316kB = 32761316000B
więc 8190329000B to max jaki moze byc size
*/
int main(int argc, char **argv)
{
  if (argc != 3)
  {
    printf("invalid number of arguments");
    return 1;
  }

  string size_string = argv[1];
  char *s_threads = argv[2];

  unsigned long long int size = stoull(size_string);
  int threads = atoi(s_threads);
  int *data = new int[size];

  omp_set_num_threads(threads);
  double start = omp_get_wtime();

#pragma omp parallel default(none) shared(data, size)
  {
    mt19937_64 rng(random_device{}());                   // ???
    uniform_int_distribution<int> distribution(1, 1000); // ???
#pragma omp for schedule(static)
    for (int I = 0; I < size; I++)
      data[I] = distribution(rng);
  }

  // for (int I = 0; I < 100; I++)
  //   cout << data[I] << " ";
  // cout << "\n";

  FILE *out_file = fopen("results.csv", "a");
  if (out_file == NULL)
  {
    printf("error");
    exit(-1);
  }
  double exec_time = omp_get_wtime() - start;
  fprintf(out_file, "%d,%f\n", threads, exec_time);
  return 0;
}
