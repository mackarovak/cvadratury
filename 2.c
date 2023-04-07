#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void Taylor(int b, long n, double epsilon, double an, double sum, double sum1,
            int i, double* xvalues, double* yvalues, int col, int kol);
double Fx(double epsilon, double x);
double Integral(double t);
double CentralRectangle(double x, int n);
double LeftRectangle(double x, int n);
double Trapecia(double x, int n);
double epsilon = pow(10, -6);

int main() {
    double an = 0, sum = 0, sum1 = 0;
    int i = 0;
    int col = 10;
    long n = 0;
    double a = 0, b = 2;
    double yvalues[100];
    double xvalues[100];
    printf("Task1.\n");
    for (int kol = 11; kol < 12; kol++) {
        // printf("%d\n", kol);
        Taylor(b, n, epsilon, an, sum, sum1, i, xvalues, yvalues, col, kol);
    }
    printf("\n\n");
    printf("Task2.\n");
    return 0;
}

double Fx(double epsilon, double x) {
    double sum = 0;
    int n = 0;
    double an = x;
    double q = 0;
    while (fabs(an) > epsilon) {
        sum += an;
        q = -(x * x * (2 * n + 1)) / ((n + 1) * (2 * n + 3));
        an *= q;
        n++;
    }
    sum *= 2 / sqrt(M_PI);
    return sum;
}

double Integral(double t) { return exp(-t * t) * 2 / sqrt(M_PI); }

double LeftRectangle(double x, int n) {
    double s1 = 0, s = 0;
    double c = 0.0;
    n = 1;
    double h;
    do {
        s = s1;
        n *= 1048576;
        h = (x - c) / n;
        s1 = 0;
        for (double temp = 0; temp < x; temp += h) {
            s1 += h * (Integral(temp + h));
        }
        // printf("%d\n", n);
    } while (abs(s1 - s) > epsilon);
    { return s1; }
}

double CentralRectangle(double x, int n) {
    double s1 = 0, s = 0;
    double c = 0.0;
    n = 1;
    double h;
    do {
        s = s1;
        n *= 2048;
        //printf("%d\n", n);
        h = (x - c) / n;
        s1 = 0;
        for (double temp = 0; temp < x; temp += h) {
            s1 += h * (Integral(temp + h / 2));
        }
    } while (abs(s1 - s) > epsilon);
    { return s1; }
}

double Trapecia(double x, int n) {
    double s1 = 0, s = 0;
    double c = 0.0;
    n = 1;
    double h;
    do {
        s = s1;
        n *= 1024;
        //printf("%d\n", n);
        h = (x - c) / n;
        s1 = 0;
        for (double temp = 0; temp < x; temp += h) {
            s1 += h * ((Integral(temp + h) + Integral(temp)) / 2);
        }
    } while (abs(s1 - s) > epsilon);
    { return s1; }
}

double Simpson(double x, int n) {
    double s1 = 0, s = 0;
    double c = 0.0;
    n = 1;
    double h;
    do {
        s = s1;
        n *= 16;
        //printf("%d\n", n);
        h = (x - c) / n;
        s1 = 0;
        for (double temp = 0; temp < x; temp += h) {
            s1 += h / 6 *
                  (Integral(temp) + 4 * Integral(temp + h / 2) +
                   Integral(temp + h));
        }
    } while (abs(s1 - s) > epsilon);
    { return s1; }
}

double Gauss(double x, int n) {
    double s1 = 0, s = 0;
    double c = 0.0;
    n = 1;
    double h;
    do {
        s = s1;
        n *= 32;
        //printf("%d\n", n);
        h = (x - c) / n;
        s1 = 0;
        for (double temp = 0; temp < x; temp += h) {
            s1 += h / 2 *
                  (Integral(temp + (h / 2) * (1 - 1 / sqrt(3))) +
                   Integral(temp + h / 2 * (1 + 1 / sqrt(3))));
        }
    } while (abs(s1 - s) > epsilon);
    { return s1; }
}

void Taylor(int b, long n, double epsilon, double an, double sum, double sum1,
            int i, double* xvalues, double* yvalues, int col, int kol) {
    int a = 0;
    double max = -100;
    // int n=1;
    double h = (double)(b - a) / (kol - 1);
    double h1 = (double)(b - a) / 10;
    int o = 1;
    for (int top = 0; top < kol; top++) {
        double xi = a + top * h;
        xvalues[top] = xi;
        // printf("%lf\n", xvalues[top]);
    }
    // printf("%d ", kol);
    // printf(" x    f(x)\n");
    for (i = 0; i < kol; i += 1) {
        double x = a + i * h;
        yvalues[i] = Fx(epsilon, x);
        // printf("%.10lf\n", yvalues[i]);
    }
    for (int i = 0; i * h <= b; i++) {
        printf("%lf %.7lf %.7lf %.10lf\n", i*h, Fx(epsilon, i*h), Simpson(i*h, n), fabs(Simpson(i * h, n) - Fx(epsilon, i * h)));
        //printf("%.7lf\n", CentralRectangle(i*h, n));
    }
    return;
}
