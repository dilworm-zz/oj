#include <stdio.h>
#include <assert.h>

void assertorder(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        assert(a[i] <= a[i+1]);
    }
}

void swap(int a[], int i, int j) {
    int tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
}

void printarr(int a[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%i ", a[i]);
    }
    printf("\n");
}

void insertsort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int j = i -1;
        int tmp = a[i];
        for (; j >=0; j--) { // j 是被比较的位置
            if (tmp < a[j]) {
                a[j+1] = a[j];
            } else {
                break;
            }
        }
        a[j+1] = tmp;
    }
}

// gcc bubblesort.c -o a && ./a
int main() {
    int arr[6]= {1,10,3,6,4, 7};
    insertsort(arr, 6);
    assertorder(arr, 6);
    printarr(arr,6);


    int arr1[1]= {1};
    insertsort(arr1, 1);
    assertorder(arr1, 1);
    printarr(arr1,1);

    int arr2[2]= {2,-12};
    insertsort(arr2, 2);
    assertorder(arr2, 2);
    printarr(arr2,2);

}
