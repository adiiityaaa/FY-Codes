#include<stdio.h>

int main() {
 int y;
 printf("Enter the year: \n");
 scanf("%d", &y);
 if(y%4==0 || y%400==0) { printf("Year is a leap year."); }
 else { printf("Year is not a leap year."); }
 return 0;
}
