class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for start in range(len(nums) - 2):
            if start > 0 and nums[start] == nums[start-1]:
                continue
            for end in range(len(nums)-1, start+1, -1):
                if end < len(nums)-1 and nums[end] == nums[end+1]:
                    continue
                if -nums[start]-nums[end] in nums[start+1:end]:
                    result.append([nums[start], -nums[start]- nums[end], nums[end]])
        return result

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0,0,0,0]))
print(s.threeSum([-1,0,1,2,-1,-4]))