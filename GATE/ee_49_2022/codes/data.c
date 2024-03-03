#include<stdio.h>
#include <stdlib.h>
#include<math.h>

double* arange(double start, double stop, double step) {

    int num = (stop - start) / step ;
    double* array = (double*)malloc((num+1) * sizeof(double));
    if (array == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i <= num; i++) {
        array[i] = start + i * step;
    }

    return array;
}

int main() {
    double start=0;
    double stop=7;
    int step=1;
    double* n = arange(start, stop, step);
    int num = (int)(stop-start+1)/step;
    double* x = (double*)malloc(num * sizeof(double));
    if (x == NULL) {
        fprintf(stderr, "Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < num; i++) {
       x[i] = 1+2*cos(M_PI/3*n[i])*cos(M_PI/3*n[i]);
    }

FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < num; ++i) {
        fprintf(file, "%lf %lf\n", n[i], x[i]);
    }

    fclose(file);
    free(n);
    free(x);
    return 0;
}
