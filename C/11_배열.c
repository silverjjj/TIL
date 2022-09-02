#include <stdio.h>
int main() {
    /* 배열 기초 */

    // 1. 10개의 int형(4bit)의 원소를 가지는 배열 생성
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    for (int i = 0; i < 10; i++) {
        // 2. 원소간 메모리 주소는 4bit씩 차이남
        printf("배열의 %d 번째 원소 : %d,  메모리 주소 : %p \n", i + 1, arr[i], &arr[i]);
    }


    /* 상수 */
    
    // 1. 상수는 그 값이 영원히 바뀌지 않습니다.
    const int a = 3;

    // 값 자체를 바꿀 수 없다.
    // a = a + 3;  
    printf("%d \n", a);
    

    /* 2차원 배열 */

    int score[2][3] = {{1, 2, 3}, {4, 5, 6}};
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", score[i][j]);
        }
        printf("\n");
    }
    return 0;
}