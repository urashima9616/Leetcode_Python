def bsearch(array, target):
            start = 0
            end = len(array) - 1
            while start <= end:
                mid = (start+end)/2
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    end = mid-1
                else:
                    start = mid + 1
            return start
array = [1,2,3,4,5,6,7,8]
target = 5.6
print bsearch(array, target)