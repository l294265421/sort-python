# -*- coding: utf-8 -*-

from typing import List
import copy

from sort.sort_interface import Sort


class InsertionSort(Sort):
    """
    插入排序
    """

    def sort(self, nums: List[int]) -> List[int]:
        """

        :param nums:
        :return:
        """
        nums_sorted = copy.deepcopy(nums)
        if nums is None or len(nums) < 2:
            return nums_sorted
        for i in range(1, len(nums_sorted)):
            j = i - 1
            nums_i = nums[i]
            while j >= 0 and nums_sorted[j] > nums_i:
                nums_sorted[j + 1] = nums_sorted[j]
                j -= 1
            nums_sorted[j + 1] = nums_i
        return nums_sorted


if __name__ == '__main__':
    bubble_sort = InsertionSort()
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
