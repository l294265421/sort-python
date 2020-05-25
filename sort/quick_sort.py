# -*- coding: utf-8 -*-

from typing import List
import copy

from sort.sort_interface import Sort


class QuickSort(Sort):
    """
    快排
    """

    def _partition(self, nums: List[int], start: int, end: int) -> int:
        """

        :param nums:
        :param start:
        :param end:
        :return:
        """
        pivot = nums[end]
        final_pivot_position_minus_one = start - 1
        for i in range(start, end, 1):
            if nums[i] <= pivot:
                final_pivot_position_minus_one += 1
                temp = nums[final_pivot_position_minus_one]
                nums[final_pivot_position_minus_one] = nums[i]
                nums[i] = temp
        result = final_pivot_position_minus_one + 1
        temp = nums[result]
        nums[result] = pivot
        nums[end] = temp
        return result

    def _quick_sort(self, nums: List[int], start: int, end: int):
        if start < end:
            mid = self._partition(nums, start, end)
            self._quick_sort(nums, start, mid - 1)
            self._quick_sort(nums, mid + 1, end)

    def sort(self, nums: List[int]) -> List[int]:
        """

        :param nums:
        :return:
        """
        nums_sorted = copy.deepcopy(nums)
        if nums_sorted is None or len(nums_sorted) < 2:
            return nums_sorted
        self._quick_sort(nums_sorted, 0, len(nums_sorted) - 1)
        return nums_sorted


if __name__ == '__main__':
    bubble_sort = QuickSort()
    nums = [3, 1, 0, 9, 10]
    print(bubble_sort.sort(nums))
    nums = None
    print(bubble_sort.sort(nums))
    nums = []
    print(bubble_sort.sort(nums))
    nums = [2]
    print(bubble_sort.sort(nums))
    nums = [2, 1]
    print(bubble_sort.sort(nums))