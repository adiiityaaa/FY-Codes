#include<stdio.h>
#include<math.h> //We import this library to use sqrt() function in velocity formula.

int main() {
 int a, b, c, d;
 float v; //Float is it can have decimal value
 printf("Velocity: sqrt(vo2 + 2a(x-x0))\nPlease enter the Vo, A, X and Xo:\n");
 scanf("%d %d %d %d", &a, &b, &c, &d);
 v = sqrt(a*a + 2*b*(c - d)); //Formula of Velocity in Programming Language Format
 printf("Velocity is: %f", v);
 return 0;
}
