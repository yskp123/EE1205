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
    double m = 1;
    double k = 1;
    double g = 9.8;
    double start=0;
    double stop=50;
    int num=1000;
    double* t = linspace(start, stop, num);
    double* x = (double*)malloc(num * sizeof(double));
    if (x == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }
    double A = (m*g/2*k);
    double w = pow((4*k)/(5*m),0.5);
    for (int i = 0; i < num; i++) {
       x[i] = A*(1-cos(w*t[i]));
    }

FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < num; ++i) {
        fprintf(file, "%lf %lf\n", t[i], x[i]);
    }

    fclose(file);
    free(t);
    free(x);
    return 0;
}
