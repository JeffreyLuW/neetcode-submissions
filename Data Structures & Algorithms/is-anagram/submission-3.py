class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for char in t:
            dic[char] = dic.get(char, 0) - 1
            if dic.get(char)== 0:
                del dic[char]
        return not dic

        