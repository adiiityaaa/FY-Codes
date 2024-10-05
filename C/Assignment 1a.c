#include<stdio.h>

int main() {
 int l, b, r, ar, pr; //define all variables for rectangle
 float ac, pc; //define all variables of circle as float as answer can have decimal value
 printf("Enter length and breadth of rectangle:\n");
 scanf("%d %d", &l,&b);
 printf("Enter Radius of Circle\n");
 scanf("%d", &r);
 ac=3.14*r*r; //area of circle
 ar=l*b; //area of rectangle
 pr=2*(l+b); //perimeter of rectangle
 pc=2*3.14*r; //circumference of circle
 printf("Perimeter of Rectangle: %d\nArea of Rectangle: %d\nPerimeter of Circle: %f\nArea of Circle: %f", pr, ar, pc, ac);
 return 0;
}
