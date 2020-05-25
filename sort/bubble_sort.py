# -*- coding: utf-8 -*-

from typing import List
import copy

from sort.sort_interface import Sort


class BubbleSort(Sort):
    """
    冒泡排序：
    1. https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F
    """

    def sort(self, nums: List[int]) -> List[int]:
        """

        :param nums:
        :return:
        """
        nums_sorted = copy.deepcopy(nums)
        if nums is None or len(nums) < 2:
            return nums_sorted
        for i in range(len(nums_sorted), 1, -1):
            for j in range(i - 1):
                if nums_sorted[j] > nums_sorted[j + 1]:
                    temp = nums_sorted[j + 1]
                    nums_sorted[j + 1] = nums_sorted[j]
                    nums_sorted[j] = temp
        return nums_sorted


if __name__ == '__main__':
    bubble_sort = BubbleSort()
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
