"""
This is a template for quick sort algorithm
Idea: 
step 1 : Pick a pivot to split the array into two parts
step 2 : Quick sort each part
"""

def QuickSort(A, low, high):
    if low < high:
        pivot = Partition(A, low, high)
        QuickSort(A, low, pivot-1)
        QuickSort(A, pivot+1, high)

def Partition(A, low, high):
    pivot = low 
    SwapArray(A, pivot, high)
    for i in xrange(low, high):
        if A[i] <= A[high]:
            SwapArray(A, low, i)
            low += 1
    SwapArray(A,low, high)
    return low
def SwapArray(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp

if __name__=='__main__':
    A = [0, 0, 1, 1, 0, 2, 1, 0]
    QuickSort(A, 0, len(A)-1)
    print A