/*
 Student: 劉醇浩
 ID: s1040641
 Date: 2016/05/10
 */
#include <stdio.h>
#include <stdlib.h>

int ones(int *num){
    int count = 0;
    for (int i=0; i<4; i++) {
        if (num[i]==1) {
            count++;
        }
    }
    return count;
}

int main(void){
    int f[4][9999][5]={0}, minterms, range[4]={0};
    printf("How many minterms? ");
    scanf("%d", &minterms);
    printf("Enter minterms (separate by space): ");
    for (int i=0; i<minterms; i++) {
        int num;
        scanf("%d", &num);
        for (int j=0; j<4; j++) {
            f[0][i][3-j] = num%2;
            num /= 2;
        }
    }
    range[0] = minterms;
    for (int i=1; i<4; i++) {
        int count=0;
        for (int j=0; j<range[i-1]; j++) {
            for (int k=0; k<range[i-1]; k++) {
                if (ones(&f[i-1][j])+1 == ones(&f[i-1][k])) {
                    int difference = 0;
                    for (int l=0; l<4; l++) {
                        if (f[i-1][j][l] != f[i-1][k][l]) {
                            difference++;
                        }
                    }
                    if (difference>1) {
                        continue;
                    }
                    f[i-1][j][4] = 2;
                    f[i-1][k][4] = 2;
                    for (int l=0; l<4; l++) {
                        if (f[i-1][j][l] != f[i-1][k][l]) {
                            f[i][count][l] = 2;
                        }
                        else{
                            f[i][count][l] = f[i-1][j][l];
                        }
                    }
                    count++;
                }
            }
        }
        range[i] = count;
    }
    int len = 0;//range[0] + range[1] + range[2] + range[3];
    int printable[9999][5];
    for (int i=0; i<4; i++) {
        for (int j=0; j<range[i]; j++) {
            if (f[i][j][4] != 2) {
                for (int k=0; k<4; k++) {
                    printable[len][k] = f[i][j][k];
                }
                len++;
            }
        }
    }
    for (int i=0; i<len; i++) {
        for (int j=0; j<len; j++) {
            if (i==j) {
                continue;
            }
            int repeat = 1;
            for (int k=0; k<5; k++) {
                if (printable[i][k] != printable[j][k]) {
                    repeat = 0;
                }
            }
            if (repeat) {
                printable[j][4] = 2;
            }
        }
    }
    printf("f = ");
    int c = 0;
    for (int i=0; i<len; i++) {
        if (printable[i][4] != 2) {
            if (c!=0) {
                printf(" + ");
            }
            for (int j=0; j<4; j++) {
                if (printable[i][j] == 0) {
                    printf("%c\'", j+65);
                }
                else if (printable[i][j] == 1){
                    printf("%c", j+65);
                }
            }
            c++;
        }
    }
    
    printf("\n");
    system("pause");
    
}

