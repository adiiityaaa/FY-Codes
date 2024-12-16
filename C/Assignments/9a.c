#include <stdio.h>

struct Employees {
 char name[50];
 int id;
 char gender[10];
 int salary;
 char post[20];
 int date;
};

int main() {
 int num;
 printf("Enter number of Employees:\n");
 scanf("%d", &num);
 struct Employees employee[num];
 for(int i=0; i<num; i++) {
   printf("\nEnter Details for Employee %d\n", i+1);
   printf("Employee Name:\n");
   scanf("%s", &employee[i].name);
   printf("Employee ID:\n");
   scanf("%d", &employee[i].id);
   printf("Employee Gender:\n");
   scanf("%s", &employee[i].gender);
   printf("Employee Salary:\n");
   scanf("%d", &employee[i].salary);
   printf("Employee Designation:\n");
   scanf("%s", &employee[i].post);
   printf("Employee's Date of Joining:\n");
   scanf("%d", &employee[i].date);
 }
 printf("\nEntered Employee Details are:\n");
 for(int i=0; i<num; i++) {
   printf("\nSr.No Employee Name | Employee ID | Employee Gender | Employee Designation | Employee Salary | Employee's Date of Joining\n");
   printf("-------------------------------------------------------------------------------------------------------------------------");
   printf("\n%d. %s | %d | %s | %s | %d | %d", i+1, employee[i].name, &employee[i].id, employee[i].gender, employee[i].post, employee[i].salary, employee[i].date);
 }
 printf("\n");
 return 0;
}
