int main() {
 int x, c=0;
 printf("Enter the number x:\n");
 scanf("%d", &x);
 for(int i=2; i<x; i++) {
  if(x%i == 0) { c = 1; break; }
  else { continue; }
 }
 if(c == 1) { printf("%d is a composite number.", x); }
 else { printf("%d is a prime number.", x); }
 return 0;
}
