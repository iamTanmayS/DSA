
def isIsomorphic(s,t):
        dic1 = {}
        dic2 = {}
        if len(s) != len(t):
            return False
        for i,j in zip(s,t):
            if i in dic1 and dic1[i] != j:
                return False
            if j in dic2 and dic2[j] !=i:
                return False
            dic1[i] = j
            dic2[j] = i
        return True


print(isIsomorphic("egg","add")) # Expected: True

    
