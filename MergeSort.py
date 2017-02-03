"""
This is a template for Merge Sort algorithm
Idea:
Step 1:  Split the array into two parts that is maximally balanced
Step 2:  Sort each part
Step 3:  Merge two parts
"""

def MergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        leftlist = A[:mid]
        rightlist = A[mid:] 
        MergeSort(leftlist)
        MergeSort(rightlist)
    
        #Merge two parts
        i = j = k = 0
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] <= rightlist[j]:
                A[k] = leftlist[i]
                k += 1
                i += 1
            else:
                A[k] = rightlist[j]
                j += 1
                k += 1
        #Merge the remaining part
        while i < len(leftlist):
            A[k] = leftlist[i]
            i += 1
            k += 1
        while j < len(rightlist):
            A[k] = rightlist[j]
            j += 1
            k += 1
if __name__ == '__main__':
    A = [0, 0, 1, 1, 0, 2, 1, 0]
    MergeSort(A)
    print A



