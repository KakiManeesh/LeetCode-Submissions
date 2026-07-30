class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0

        multiplier = 1
        count = 8
        hash = {}
        for i in word :
            hash[i] = hash.get(i,0) + 1

        ans = [ i for i in hash.values() ]
        print(ans)
        ans.sort(reverse = True)

        for i in ans :
            if count == 0 :
                count = 8
                multiplier += 1
            count -= 1

            total += i*multiplier
        return total