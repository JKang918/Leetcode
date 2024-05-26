class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in table:
                table[nums[i]] = i
            else:
                return [table[diff], i]
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