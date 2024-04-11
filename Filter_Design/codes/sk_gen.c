#include <stdio.h>
#include <math.h>
#include <complex.h>

#define N 4
#define EPSILON 0.4
#define OMEGA_LP 1
#define PI 3.14159265358979323846

int main() {
    // Calculate B_k coefficient
    double B_k = asinh(1 / EPSILON) / N;

    // Initialize an array to store the poles
    double complex s[2*N];

    // Calculate and store the poles
    for (int k = 0; k < N; ++k) {
    // Calculate A_k coefficient
    double A_k = (2*k+1)* PI/(2*N);
        s[k] = (OMEGA_LP * sin(A_k) * sinh(B_k)) - (I * OMEGA_LP * cos(A_k) * cosh(B_k));
        s[k+N] = -(OMEGA_LP * sin(A_k) * sinh(B_k)) - (I * OMEGA_LP * cos(A_k) * cosh(B_k));
    }

    // Save poles to a .dat file
    FILE *file = fopen("poles.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    fprintf(file, "Real Part, Imaginary Part\n");
    for (int i = 0; i < 2*N; ++i) {
        fprintf(file, "%.4f, %.4f\n", creal(s[i]), cimag(s[i]));
    }
    fclose(file);

    printf("Poles saved to poles.txt file.\n");

    return 0;
}

