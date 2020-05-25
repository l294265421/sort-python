# -*- coding: utf-8 -*-

from typing import List
import copy

from sort.sort_interface import Sort


class MergeSort(Sort):
    """
    归并排序
    """

    def _merge(self, nums: List[int], start, mid, end):
        """
        p <= q < r，其中nums[start: mid + 1]和nums[mid + 1: end + 1]是有序的，合并之后，使得nums[start: end + 1]是有序的
        :param nums:
        :param start:
        :param mid:
        :param end:
        :return:
        """
        nums1 = copy.deepcopy(nums[start: mid + 1])
        nums2 = copy.deepcopy(nums[mid + 1: end + 1])
        i = 0
        j = 0
        k = start
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                k += 1
                i += 1
            else:
                nums[k] = nums2[j]
                k += 1
                j += 1

        while i < len(nums1):
            nums[k] = nums1[i]
            k += 1
            i += 1
        while j < len(nums2):
            nums[k] = nums2[j]
            k += 1
            j += 1

    def inner_sort(self, nums: List[int], start, end):
        if start < end:
            mid = (start + end) // 2
            self.inner_sort(nums, start, mid)
            self.inner_sort(nums, mid + 1, end)
            self._merge(nums, start, mid, end)

    def sort(self, nums: List[int]) -> List[int]:
        """

        :param nums:
        :return:
        """
        nums_sorted = copy.deepcopy(nums)
        if nums_sorted is None or len(nums_sorted) < 2:
            return nums_sorted
        self.inner_sort(nums_sorted, 0, len(nums_sorted) - 1)
        return nums_sorted


if __name__ == '__main__':
    bubble_sort = MergeSort()
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