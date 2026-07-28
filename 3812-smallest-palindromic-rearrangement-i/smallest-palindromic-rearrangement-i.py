class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n&1 == 1 :
            middle = s[n//2]
        else:
            middle= ''
        '''
        first = s[:n//2]
        first = "".join(sorted(first))
        
        ans = first + middle + first[::-1]

        return ans
        '''

        hash = {}

        for i in s :
            hash[i] = hash.get(i,0) + 1

        first = ""

        for i in range(97,97+26) :
            if chr(i) in hash :
                first += chr(i) * (hash[chr(i)]//2) 
        return first + middle + first[::-1]