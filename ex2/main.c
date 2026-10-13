#include <stdio.h>

int sum_and_product(int a, int b, int *product){
    *product = a * b;
    return a + b;
}

int main(void){
    int product;

    printf("product = %d, sum = %d\n", product, sum_and_product(3, 4, &product));

    // swapped order (sum first, then product):
    // printf("sum = %d, product = %d\n", sum_and_product(3, 4, &product), product);

    return 0;
}
