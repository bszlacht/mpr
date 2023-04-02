#include <iostream>
#include <cstdlib>
#include <random>
#include <string>
#include <omp.h>
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

*/
int main(int argc, char **argv)
{
  string size_string(argv[1]);
  unsigned long long int size = stoull(size_string); // string to unsigned long long
  int threads = atoi(argv[2]);                       // string to integer
  int *data = new int[size];                         // create table

  omp_set_num_threads(threads);
  double start = omp_get_wtime();

#pragma omp parallel default(none) shared(data, size)
  {
    mt19937_64 rng(random_device{}());  // ???
    uniform_int_distribution<int> distribution(1, 1000);  // ???
#pragma omp for schedule(static)
    for (int I = 0; I < size; I++)
      data[I] = distribution(rng);  // seed distribution and get random number
  }

  // for (int I = 0; I < 100; I++)
  //   cout << data[I] << " ";
  // cout << "\n";

  cout << "Time: " << omp_get_wtime() - start << "\n";
  return 0;
}
