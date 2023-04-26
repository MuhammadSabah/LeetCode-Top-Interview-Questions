class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverseList(self, arr):
            j = len(arr) - 1
            i = 0
            while i < j:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                i += 1
                j -= 1

            return arr

        nums = reverseList(self, nums)
        left_side = reverseList(self, nums[:k])
        right_side = reverseList(self, nums[k:])

        nums[:] = left_side + right_side

