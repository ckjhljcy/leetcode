class Solution(object):
    def get_nearest(self, nums, target):
        for index in range(0, len(nums)-1):
            if target > nums[index] and target < nums[index+1]:
                if target-nums[index] < nums[index+1]-target:
                    return nums[index] - target
                else:
                    return nums[index+1] - target
        return nums[0]

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if target > nums[-1] + nums[-2] + nums[-3]: return nums[-1]+nums[-2]+nums[-3]
        if target < nums[0] + nums[1] + nums[2]: return nums[0]+nums[1]+nums[2]
        dif = 0xffffffff
        for start in range(0, len(nums)):
            for end in range(len(nums) - 1, start+1, -1):
                want = (target - nums[start] - nums[end])
                if want > nums[end-1] :
                    if abs(dif) > abs(want-nums[end-1]):
                        dif = nums[end-1] - want
                    break
                elif want < nums[start+1]:
                    if abs(dif) > abs(want-nums[start+1]):
                        dif = nums[start+1] - want
                    continue
                elif want in nums[start+1:end]:
                    return target
                else:
                    new_dif = self.get_nearest(nums[start+1:end], want)
                    if abs(dif) > abs(new_dif):
                        dif = new_dif
        return target+dif

class Solution2():
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return target
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum > target:
                    k -= 1
                else:
                    j += 1
        return result


s = Solution2()
#print(s.threeSumClosest([-1, 2, 1, -4], 1))
#print(s.threeSumClosest([-1,-2,-3,-4,-5], -100))
#print(s.threeSumClosest([1,2,3,4,5,6,7], -1))
assert(s.threeSumClosest([0,0,0], 1) == 0)
assert(s.threeSumClosest([0,2,1,-3],1) == 0)
assert(s.threeSumClosest([1,1,-1,-1,3],-1) == -1)
assert(s.threeSumClosest([1,6,9,14,16,70],81) == 80)
