#include <stdio.h>

void Test()
{
    static int data = 0;    /*data 변수 앞에 static 키워드를 사용 */
    printf("%d, ", data++);
}

void main()
{
    int i;
    for(i=0; i<5; i++) Test();
}