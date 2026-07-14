class Solution:
    def twoSum(sef, nums: List[int], target: int) -> List[int]:

        hash_ = {}

        for i in range(len(nums)) :
            if (target - nums[i]) in hash_ :
                return [hash_[target-nums[i]] , i ]
            else:
                hash_[nums[i]] = i
        return []