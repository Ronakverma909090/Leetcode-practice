class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = str(n)
        lst = list(nums)
        num_sum = 0
        product = 1
        for i in lst:
            a = int(i)
            num_sum = num_sum +a
            product = product*a
        return product - num_sum