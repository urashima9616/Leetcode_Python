def longestPalindrome(s):
    """
    type s: string
    rtype n: int
    """
    opt = [1 for _ in range(len(s))]
    pos = [[_] for _ in range(len(s))]
    i = 1
    while i < len(s):
        temp = 1
        for each in pos[i-1]:
            if each == 0:
                continue
            if i - 1 == each and s[each] == s[i]:
                pos[i].append(each)
                if temp < 2:
                    temp = 2
            elif s[i] == s[each-1]:
                pos[i].append(each-1)
                if temp < i - each + 2:
                    temp = i - each + 2
        opt[i] = temp
        i +=1
    return max(opt)
print longestPalindrome("aacecaaa")