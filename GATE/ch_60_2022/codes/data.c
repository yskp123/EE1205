#include<stdio.h>
#include <stdlib.h>
#include<math.h>

double* linspace(double start, double stop, int num) {
    double* array = (double*)malloc(num * sizeof(double));
    if (array == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }

    double step = (stop - start) / (num - 1);
    for (int i = 0; i < num; i++) {
        array[i] = start + i * step;
    }

    return array;
}

int main() {
    double start=0;
    double stop=7;
    int num=1000;
    double* t = linspace(start, stop, num);
    double* y = (double*)malloc(num * sizeof(double));
    if (y == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < num; i++) {
       y[i] = 2+4*pow(M_E,-2*t[i])-6*pow(M_E,-4*t[i]);
    }

FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < num; ++i) {
        fprintf(file, "%lf %lf\n", t[i], y[i]);
    }

    fclose(file);
    free(t);
    free(y);
    return 0;
}
