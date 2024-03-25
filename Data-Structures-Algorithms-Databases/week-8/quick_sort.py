class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # using quick sort
        def quick_sort(nums, left=0, right=len(nums)-1):
            if left < right:
                pivot_index = partition(nums, left, right)
                # sort the smaller elements on the left side
                quick_sort(nums, left, pivot_index - 1)
                # sort the larger elements on the right side
                quick_sort(nums, pivot_index + 1, right)

        def partition(nums, left, right):
            pivot = nums[left]
            low = left + 1
            high = right
            while True:
                while low <= high and nums[high] >= pivot:
                    high -= 1
                while low <= high and nums[low] <= pivot:
                    low += 1
                if low <= high:
                    nums[low], nums[high] = nums[high], nums[low]
                else:
                    break
            nums[left], nums[high] = nums[high], nums[left]
            return high

        quick_sort(nums)
        return nums


if __name__ == "__main__":
    nums = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
    print("Original array:", nums)
    solution = Solution()
    solution.sortArray(nums)
    print("Sorted array:", nums)