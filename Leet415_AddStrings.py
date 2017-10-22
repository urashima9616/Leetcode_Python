def addStrings(s1, s2):
    """
    type s1, s2: String
    rtype string
    """
    digit2num = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
    pt1, pt2 = len(s1)-1, len(s2)-1
    carry = 0
    res = []
    while pt1 >= 0 and pt2 >= 0:
        digit_sum = digit2num[s1[pt1]] + digit2num[s2[pt2]] + carry
        carry = digit_sum/10
        res.append(str(digit_sum%10))
        pt1 -=1
        pt2 -=1
    else:
        if pt1 < 0:
            while pt2 >=0 :
                digit_sum = digit2num[s2[pt2]] + carry
                carry = digit_sum/10
                res.append(str(digit_sum%10))
                pt2 -=1
        else:
            while pt1 >=0 :
                digit_sum = digit2num[s1[pt1]] + carry
                carry = digit_sum/10
                res.append(str(digit_sum%10))
                pt1 -=1
    if carry != 0:
        res.append(str(carry))
    return "".join(reversed(res))

print addStrings("9919", "12312")

