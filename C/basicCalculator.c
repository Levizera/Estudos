#include <stdio.h>
#include <stdlib.h>

int main(){
    
    double num1;
    double num2;
    
    printf("Enter the first Number: ");
    scanf("%lf", &num1);
    printf("Enter the second Number: ");
    scanf("%lf", &num2);
    
    printf("The Result is: %f", num1 + num2);
    
    
    
    return 0;
}