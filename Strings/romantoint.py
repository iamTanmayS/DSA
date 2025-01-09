def romanToInt(s):
        romandic = {"I" : 1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        for i in range(len(s)):
            sum+=romandic[s[i]]
            if i> 0 and romandic[s[i]]>romandic[s[i-1]]:
                sum -= 2 * romandic[s[i - 1]]
        return sum
            

s = "MCMXCIV"
print(romanToInt(s))