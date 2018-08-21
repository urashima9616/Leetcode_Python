class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        dict_l20 = {0:"", 1: "One", 2:"Two", 3: "Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty" }
        dict_g20 = {0:"", 1:"One", 2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
        unit = ["", "Thousand", "Million", "Billion"]
        def readThousand(num):
            hundred = num/100
            num = num%100
            if num <= 20:
                tmp = dict_l20[num]
            else:
                ten = num/10
                residual = num%10
                if residual == 0:
                    tmp = dict_g20[ten]
                else:
                    tmp = dict_g20[ten] + " " + dict_l20[residual]
            if not hundred:
                return tmp
            else:
                return (dict_l20[hundred] + " " + "Hundred" + " " + tmp).rstrip()
                    
        if num == 0:
            return "Zero"
        res = []
        i = 0
        while num > 0: 
            temp = num%1000
            cur = readThousand(temp) 
            if cur:
                res.append(cur + " " +unit[i]) 
            num /= 1000
            i += 1
        return " ".join(res[::-1]).rstrip()