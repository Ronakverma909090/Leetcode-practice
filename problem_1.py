class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        out_put = list()
        for i in range(len(nums)):
            for j in range(len(nums)):
                result = nums[i] + nums[j]
                if i == j:
                    continue
                if result == target:
                    out_put.append(i)
                    out_put.append(j)
                    return out_put