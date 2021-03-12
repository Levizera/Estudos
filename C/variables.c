#include <stdlib.h>

/*
CHAR é usado para se referir às variáveis que contém caracteres, e os [] são usados para indicar que serão colocados vários caracteres dentro da variável

INT é usado para criar variáveis que contém números

%s é usado para dizer que ali vai ser inserido uma variável

%d é usado para dizer que um número será introduzido ali
*/


int main(){
       
    char nomes[] = "Levi";
    int idade = 17; 
    int segundaIdade = 14;

    printf("O nome dele é %s \n", nomes);
    printf("Ele tem %d anos\n", idade);
    printf("Mas Levi Gostaria de ter %d anos\n", segundaIdade);
    
    return 0;
}