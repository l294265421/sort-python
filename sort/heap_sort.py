# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Baidu.com, Inc. All Rights Reserved
#
"""

Authors: liyuncong(liyuncong@baidu.com)
Date:    2020/5/25 16:09
"""

from typing import List
import copy

from sort.sort_interface import Sort
from heap.heap import MaxHeap


class HeapSort(Sort):
    """
    堆排序
    """

    def sort(self, nums: List[int]) -> List[int]:
        """

        :param nums:
        :return:
        """
        nums_sorted = copy.deepcopy(nums)
        if nums_sorted is None or len(nums_sorted) < 2:
            return nums_sorted

        heap = MaxHeap(nums_sorted, len(nums_sorted))
        heap.build_heap()
        temp = nums_sorted[-1]
        nums_sorted[-1] = nums_sorted[0]
        nums_sorted[0] = temp
        for heap_size in range(len(nums_sorted) - 1, 1, -1):
            heap.heap_size = heap_size
            heap.heapify(0)
            temp = nums_sorted[heap_size - 1]
            nums_sorted[heap_size - 1] = nums_sorted[0]
            nums_sorted[0] = temp
        return nums_sorted


if __name__ == '__main__':
    bubble_sort = HeapSort()
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