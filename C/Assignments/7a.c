#include <stdio.h>

int main() {
 int x;
 printf("Enter the array size:\n");
 scanf("%d", &x);
 int arr[x];
 printf("Enter array elements: \n");
 for(int i=0; i<x; i++) {
    scanf("%d", &arr[i]);
 }
 int max = arr[0];
 int min = arr[0];
 for(int j=0; j<x; j++) {
   if(arr[j] > max) { max = arr[j]; }
   if(arr[j] < min) { min = arr[j]; }
 }
 printf("Smallest number: %d", min);
 printf("\nGreatest number: %d", max);
 return 0;
}
