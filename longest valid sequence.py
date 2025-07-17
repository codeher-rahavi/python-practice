class Solution:
    def maximumLength(self, nums):
        even = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even += 1

        odd = len(nums) - even
        same = max(even, odd)

        alter = 1
        l = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 != l:
                alter += 1
                l = nums[i] % 2

        return max(alter, same)

s=Solution()
print(s.maximumLength([1,2,3,4]))