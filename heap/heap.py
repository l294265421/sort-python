# -*- coding: utf-8 -*-

from typing import List


class Heap:
    """
    堆
    """

    def __init__(self, nums: List[int], heap_size: int):
        self.nums = nums
        self.heap_size = heap_size

    def parent(self, i):
        return 0 if i == 0 else (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def heapify(self, i):
        raise NotImplementedError()

    def build_heap(self):
        for i in range(self.parent(self.heap_size - 1), -1, -1):
            self.heapify(i)


class MaxHeap(Heap):
    """
    大根堆
    """

    def __init__(self, nums: List[int], heap_size: int):
        super().__init__(nums, heap_size)

    def heapify(self, i):
        l = super().left(i)
        r = super().right(i)
        largest = i
        if l < self.heap_size and self.nums[l] > self.nums[i]:
            largest = l
        if r < self.heap_size and self.nums[largest] < self.nums[r]:
            largest = r
        if largest != i:
            temp = self.nums[i]
            self.nums[i] = self.nums[largest]
            self.nums[largest] = temp
            self.heapify(largest)
