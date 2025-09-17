from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        if m == 0 and n == 0:
            raise ValueError("Both arrays are empty")

        low, high = 0, m
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (m + n + 1) // 2 - cut1

            l1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            l2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            r1 = nums1[cut1] if cut1 < m else float('inf')
            r2 = nums2[cut2] if cut2 < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        raise RuntimeError("Should not reach here")

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))        # 2.0
    print(s.findMedianSortedArrays([1, 2], [3, 4]))    # 2.5
    print(s.findMedianSortedArrays([], [1]))           # 1.0
