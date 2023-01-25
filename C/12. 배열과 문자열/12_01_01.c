#include <stdio.h>

void main()
{
    short student[20];  /* 2byte 정수형 데이터 short를 20개 저장할수 있는 배열 student를 선언
                            short형(2byte) * 20 = 40byte*/
    student[1] = 10;
    printf("%d\n", student[1]);
}