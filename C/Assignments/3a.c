#include <stdio.h>

int main() { 
 float a,b,c;
 printf("Enter the three sides of Triangle:\n");
scanf("%f %f %f", &a, &b, &c);
if(a == b && b == c) { printf("The triangle is Equilateral."); }
else if(a == b || b == c || c == a) { printf("The triangle is Isoceles."); }
else { printf("The triangle is Scalene."); }
return 0;
}
