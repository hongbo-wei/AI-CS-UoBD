/*
To compile the code:
    // Linux/MacOS/Windows:
    gcc -o quick-sort quick-sort.c
    // Linux/MacOS:
    make quick-sort
To run the code:
    ./quick-sort
*/

#include <stdio.h>

void quicksort_run(int arr[], int left , int right);
int partition(int arr[], int left , int right);

void quicksort(int arr[], int len){
    quicksort_run(arr, 0, len - 1);
}

void quicksort_run(int arr[], int left , int right) {
    if(left < right){
        int pivotindex = partition(arr, left , right);
        quicksort_run(arr, left, pivotindex - 1);
        quicksort_run(arr, pivotindex + 1, right);
    }
}

int partition(int arr[], int left , int right) {
    int size = right - left + 1;
    int arr_b[size]; // Create temporary array with correct size
    // pivotindex = choosePivot(a, left , right)
    int pivotindex = left; // Choosing the leftmost element as the pivot
    int pivot = arr[left];
    int a_count = left;
    int b_count = 1;
    for ( int i = left; i <= right; i++) {
        if ( i == pivotindex )
            arr_b[0] = arr[i];
        else if (arr[i] < pivot || 
                (arr[i] == pivot && i < pivotindex))
            arr[a_count++] = arr[i];
        else
            arr_b[b_count++] = arr[i];
    }
    for (int i = 0; i < b_count; i++)
        arr[a_count++] = arr_b[i];
    return right - b_count + 1;
}

int main() {
    int arr[] = {4, 5, 2, 7, 8, 1, 3, 6};
    int length = sizeof(arr)/sizeof(arr[0]);
    printf("Length of the array: %d\n",length);
    quicksort(arr, length);
    for (int i = 0; i < length; i++)
        printf("%d ", arr[i]);
    return 0;
}