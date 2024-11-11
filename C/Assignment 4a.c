#include <stdio.h>
#include <math.h>

int main() {
 int n,r,x,sum,c,y;
 printf("Enter the number: \n");
 scanf("%d", &n);
 x = n;
 y = n;
 sum = 0;
 c = 0;
 while (y > 0) {
  y = y/10;
  c++;
 }
 while (n > 0) {
  r = n%10;
  sum = sum + pow(r, c);
  n = n/10;
 }
 if(sum == x) { printf("%d is an Armstrong number.", x); }
 else { printf("%d is not an Armstrong number.", x); }
 return 0;
}
