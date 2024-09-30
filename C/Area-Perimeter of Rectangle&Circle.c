#include<stdio.h>

int main() {
 int l, b, r, ar, pr;
 float ac, pc;
 printf("Enter length and breadth of rectangle:\n");
 scanf("%d %d", &l,&b);
 printf("Enter Radius of Circle\n");
 scanf("%d", &r);
 ac=3.14*r*r;
 ar=l*b;
 pr=2*(l+b);
 pc=2*3.14*r;
 printf("Perimeter of Rectangle: %d\nArea of Rectangle: %d\nPerimeter of Circle: %f\nArea of Circle: %f", pr, ar, pc, ac);
 return 0;
}
