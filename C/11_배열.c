#include <stdio.h>
int main() {
    /* �迭 ���� */

    // 1. 10���� int��(4bit)�� ���Ҹ� ������ �迭 ����
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    for (int i = 0; i < 10; i++) {
        // 2. ���Ұ� �޸� �ּҴ� 4bit�� ���̳�
        printf("�迭�� %d ��° ���� : %d,  �޸� �ּ� : %p \n", i + 1, arr[i], &arr[i]);
    }


    /* ��� */
    
    // 1. ����� �� ���� ������ �ٲ��� �ʽ��ϴ�.
    const int a = 3;

    // �� ��ü�� �ٲ� �� ����.
    // a = a + 3;  
    printf("%d \n", a);
    

    /* 2���� �迭 */

    int score[2][3] = {{1, 2, 3}, {4, 5, 6}};
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", score[i][j]);
        }
        printf("\n");
    }
    return 0;
}