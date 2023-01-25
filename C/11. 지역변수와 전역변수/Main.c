#include <stdio.h>

void Sum(int, int);
extern int result;  /*Sum.c 에서 정의된 전역변수를 참조*/

void main()
{
    Sum(7, 10);
    printf("7 + 10 = %d\n", result);   /* 전역변수 result */
}