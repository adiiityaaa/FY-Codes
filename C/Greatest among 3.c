#include<stdio.h>

int main() {
 int a, b, c;
 printf("Enter three numbers: \n");
 scanf("%d %d %d", &a, &b, &c);
 if(a>b && a>c) { printf("%d is the greatest number.", a); }
 else if(a<b && b>c) { printf("%d is the greatest number.", b); }
 else { printf("%d is the greatest number.", c); }
 return 0;
}
