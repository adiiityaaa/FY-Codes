#include<stdio.h>

int main() {
 int a, b, c;
 printf("Enter three numbers: \n");
 scanf("%d %d %d", &a, &b, &c);
 if(a>b && a>c) { printf("%d is the greatest number.", a); } //Check if A is greatest
 else if(a<b && b>c) { printf("%d is the greatest number.", b); } //If not check if B is greatest
 else { printf("%d is the greatest number.", c); } //Else C is greatest
 return 0;
}
