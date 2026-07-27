class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            # it's important to have length before #
            # this is important because if length is multiple characters long (eg: 100)
            # we need to be able to parse the characters of the length until the #.
            s = s + str(len(string)) + '#'  + string
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        strs = []


        while i<len(s):
            strLen = 0
            while s[j] != '#':
                j = j+1

            while i<j:
                strLen = strLen*10 + int(s[i])
                i = i+1

            start = i+1
            end = start + strLen
            strs.append(s[start:end])
            i = end
            j=i
            
        return strs



