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
    double start=-3;
    double stop=2;
    int num=1000;
    double* x = linspace(start, stop, num);
    double* y = (double*)malloc(num * sizeof(double));
    if (y == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < num; i++) {
       y[i] = x[i] * pow(M_E, x[i]);
    }

FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < num; ++i) {
        fprintf(file, "%lf %lf\n", x[i], y[i]);
    }

    fclose(file);
    free(x);
    free(y);
    return 0;
}
