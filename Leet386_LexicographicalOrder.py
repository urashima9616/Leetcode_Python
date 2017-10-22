def LexiOrder(n):
    cnt_n = len(str(n))
    res = []
    cnt = 1
    cnt_num = 1
    num = 1
    res.append(num)
    while cnt_num < n:
        if cnt < cnt_n and num* 10 <= n:
            num *= 10
            cnt += 1
        elif num == n or num%10 == 9:
            num = num/10
            cnt -= 1
            while num%10 == 9:
                num = num/10
                cnt -= 1
            num += 1
        else:
            num += 1
        res.append(num)
        cnt_num += 1
    return res

print LexiOrder(23)     


    