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

void bubblesort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 1; j < n - i; ++j) {
            if (a[j-1] > a[j]) {
                swap(a, j-1, j);
            }
        }
    }
}

// gcc bubblesort.c -o a && ./a
int main() {
    int arr[6]= {1,10,3,6,4, 7};
    bubblesort(arr, 6);
    assertorder(arr, 6);
    printarr(arr,6);


    int arr1[1]= {1};
    bubblesort(arr1, 1);
    assertorder(arr1, 1);
    printarr(arr1,1);

    int arr2[2]= {2,-12};
    bubblesort(arr2, 2);
    assertorder(arr2, 2);
    printarr(arr2,2);

}
