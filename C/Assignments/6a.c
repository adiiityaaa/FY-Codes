#include <stdio.h>

int main() {
 int x;
 printf("Enter the day number:\n");
 scanf("%d", &x);
 switch(x) {
  case 1: printf("You chose Monday.");
  break;
  case 2: printf("You chose Tuesday.");
  break;
  case 3: printf("You chose Wednesday.");
  break;
  case 4: printf("You chose Thursday.");
  break;
  case 5: printf("You chose Friday.");
  break;
  case 6: printf("You chose Saturday.");
  break;
  case 7: printf("You chose Sunday.");
  break;
  default: printf("You chose an incorrect value.");
  break;
 }
 return 0;
}
