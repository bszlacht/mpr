#include <iostream>
#include <random>
#include <string>
using namespace std;

int main(int argc, char **argv)
{
    string size_string(argv[1]);
    unsigned long long int size = stoull(size_string);
    int threads = atoi(argv[2]);
    int *data = new int[size];

    FILE *out_file = fopen("results.csv", "w");
    if (out_file == NULL)
    {
        printf("error");
        exit(-1);
    }
    double exec_time = 123.2;
    fprintf(out_file, "%d,%f\n", threads, exec_time);
    return 0;
}
