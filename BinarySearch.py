def bsearch(array, target):
            start = 0
            end = len(array) - 1
            while start <= end:
                mid = (start+end)//2
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    end = mid-1
                else:
                    start = mid + 1
            return start
array = [1,2,3,4,5,6,7,8]
target = 0
print(bsearch(array, target))

def bsearch2insert(array, target):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start + end)//2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    else:
        if array[mid] < target:#You moved search to the right in the last comparison:
            return mid
        else: # You moved search to the left in the last comparison
            return mid - 1

array = [1,2,3,4,5,6,7,8]
target = 3.9
print(bsearch2insert(array, target))
