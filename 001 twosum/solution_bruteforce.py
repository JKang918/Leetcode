class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for k in range(i + 1, len(nums) - i):      #starts with i + 1 to avoid adding the same element twice
                if nums[i] + nums[i + k] == target:    #checks all pairs with two for loops
                    return [i, i + k]
        return []

example1 = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
print(example1.twoSum(nums1, target1))                  #[0, 1]

example2 = Solution()
nums2 = [3, 2, 4]
target2 = 6
print(example2.twoSum(nums2, target2))                  #[1, 2]

example3 = Solution()
nums3 = [3, 3]
target3 = 6
print(example3.twoSum(nums3, target3))                  #[0, 1]