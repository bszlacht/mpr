#include <iostream>
#include <cstdlib>
#include <random>
#include <string>
#include <omp.h>
#include <typeinfo>

using namespace std;
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
  int *data = new int[size];
  double divider = atof(didiver_s);
  
  omp_set_num_threads(threads);
  double start = omp_get_wtime();
  // int chunk_size = (int)(size / threads);
  int chunk_size = (int)(size * (divider / 100.0));

#pragma omp parallel default(none) shared(data, size, chunk_size)
  {
    mt19937_64 rng(random_device{}());
    uniform_int_distribution<int> distribution(1, 1000);

#pragma omp for schedule(static, chunk_size)
    // #pragma omp for schedule(dynamic)
    // #pragma omp for schedule(guided)
    // #pragma omp for schedule(runtime)
    // #pragma omp for schedule(auto)
    for (int I = 0; I < size; I++)
      data[I] = distribution(rng);
  }

  FILE *out_file = fopen("results.csv", "a");
  if (out_file == NULL)
  {
    printf("error");
    exit(-1);
  }
  double exec_time = omp_get_wtime() - start;
  fprintf(out_file, "%d,%lld,%f\n", threads, sizeof(int) * size, exec_time);
  return 0;
}
