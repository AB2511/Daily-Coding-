class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        prefix_sum = {0: 1} 

        for n in nums:
            total += n  

            if total - k in prefix_sum:
                count += prefix_sum[total - k]

            prefix_sum[total] = prefix_sum.get(total, 0) + 1

        return count
