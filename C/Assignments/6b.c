#include <stdio.h>

int main() {
 int x, v, cv=0;
 char str[100];
 printf("Enter the string:\n");
 fgets(str, 100, stdin);
 printf("Select the action:\n1. Number of Characters\n2. Number of Vowels\n3. Character Occurence\n");
 scanf("%d", &x);
 int y = strlen(str-1);
 for(int i=0; i<y; i++) {
    if(str[i] == "a" | str[i] == "e" | str[i] == "i" | str[i] == "o" | str[i] == "u") { cv++; }
 }
 switch(x) {
  case 1: printf("Number of characters in string: %d", y);
  break;
  case 2: printf("You chose Tuesday.");
  break;
  case 3: printf("You chose Wednesday.");
  break;
  default: printf("You chose an incorrect action.");
  break;
 }
 return 0;
}
