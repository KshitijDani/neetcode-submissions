class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedS = ""
        for ch in s:
            if ch.isalnum():
                cleanedS+=ch.lower()

        i=0
        j=len(cleanedS)-1


        while(i<=j):
            if cleanedS[i]!=cleanedS[j]:
                return False
            i+=1
            j-=1

        return True