#include <stdio.h>

int occur(char x, char str[], int l) {
 int cc = 0;
 for(int j=0; j<l; j++) {
  if(str[j] == x) { cc++; }
 }
 return cc;
}

int main() {
 int x, vc=0, c, co;
 char str[100];
 printf("Enter the string:\n");
 fgets(str, 100, stdin);
 printf("Select the action:\n1. Number of Characters\n2. Number of Vowels\n3. Character Occurence\n");
 scanf("%d", &x);
 getchar();
 int y = strlen(str)-1;
 for(int i=0; i<y; i++) {
    if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') { vc++; }
 }
 switch(x) {
  case 1: printf("Number of characters in string: %d", y);
  break;
  case 2: printf("Number of Vowels in string: %d", vc);
  break;
  case 3: printf("Enter the character: \n");
    scanf("%c", &c);
    co = occur(c, str, y);
    printf("Number of times %c occurs: %d", c,co);
  break;
  default: printf("You chose an incorrect action.");
  break;
 }
 return 0;
}
