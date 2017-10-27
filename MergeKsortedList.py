def mergelist(nums):
    """
    type nums: List[List[int]]
    """
    def Merge(nums):
        if len(nums) == 2:
            return mergetwolist(nums[0], nums[1])
        elif len(nums) == 1:
            return nums[0]
        mid = (len(nums)-1)/2
        num1 = Merge(nums[:mid])
        num2 = Merge(nums[mid:])
        return mergetwolist(num1, num2)
    
    def mergetwolist(num1, num2):
        pt_1, pt_2 = [0] *2
        num = []
        while pt_1 <len(num1) and pt_2 < len(num2):
            if num1[pt_1] <= num2[pt_2]:
                num.append(num1[pt_1])
                pt_1 += 1
            else:
                num.append(num2[pt_2])
                pt_2 += 1
        else:
            if pt_1 == len(num1):
                num += num2[pt_2:]
            else:
                num += num1[pt_1:]
        return num
    return Merge(nums)

            
print mergelist([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])