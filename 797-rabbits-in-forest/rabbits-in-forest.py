class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        hash = {}

        for i in answers :
            hash[i] = hash.get(i,0) + 1
        count = 0

        for key,value in hash.items():
            if key == 0 :
                print(key,value,count)
                continue
            key += 1
            if key >= value :
                count += key-value
            else:
                value = value % key
                if value != 0 :
                    count += key-value

        return len(answers) + count