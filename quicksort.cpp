#include<iostream>
#include<bits/stdc++.h>

using namespace std;

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int Partition(int arr[], int start, int end)
{
    int pivot = arr[end];
    int i = start;
    
    for(int j = i; j <= end-1 ; j++)
    {
        if (arr[j] < pivot)
        {
            swap(&arr[i], &arr[j]);
            i++;
        }
    }

    swap(&arr[i], &arr[end]);
    return i;
}

void quicksort(int arr[], int start, int end)
{
    if (start<end)
    {
        int index = Partition(arr, start, end);
        quicksort(arr,start, index-1);
        quicksort(arr, index+1, end);
    }
}

int main()
{
    int arr[6] = {5,4,3,2,1,0};
   
    quicksort(arr,0, 5);

    for(int i = 0; i < 6 ; i++)
    {
        cout << arr[i] << " ";
    }
}