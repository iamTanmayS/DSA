class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]= 1

        items = list(dic.items())

        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j][1] < items[j + 1][1]: 
                    items[j], items[j + 1] = items[j + 1], items[j]


        sorted_dict = dict(items)
        m = ""
        for i in sorted_dict:
            m += "".join(i*sorted_dict[i])
        return m
