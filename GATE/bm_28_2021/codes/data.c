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
    double stop=5;
    int num=1000;
    double* t = linspace(start, stop, num);
    double x[] = {1,2,3};
    double* y1 = (double*)malloc(num * sizeof(double));
    if (y1 == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }
    double* y2 = (double*)malloc(num * sizeof(double));
    if (y1 == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }
    double* y3 = (double*)malloc(num * sizeof(double));
    if (y1 == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < num; i++) {
       y1[i] = sin(x[0]-5*t[i]);
       y2[i] = sin(x[1]-5*t[i]);
       y3[i] = sin(x[2]-5*t[i]);
    }

FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < num; ++i) {
        fprintf(file, "%lf %lf %lf %lf\n", t[i], y1[i], y2[i], y3[i]);
    }

    fclose(file);
    free(t);
    free(y1);
    free(y2);
    free(y3);
    return 0;
}
