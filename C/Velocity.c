#include<stdio.h>
#include<math.h>

int main() {
 int a, b, c, d;
 float v;
 printf("Velocity: sqrt(vo2 + 2a(x-x0))\nPlease enter the Vo, A, X and Xo:\n");
 scanf("%d %d %d %d", &a, &b, &c, &d);
 v = sqrt(a*a + 2*b*(c - d));
 printf("Velocity is: %f", v);
 return 0;
}
