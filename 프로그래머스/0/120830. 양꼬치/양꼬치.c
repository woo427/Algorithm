#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, int k) {
    int free = n / 10;
    return (k-free)*2000 + 12000*n;
}