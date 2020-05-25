# -*- coding: utf-8 -*-

from typing import List


class Sort:
    """
    所有排序算法的基类
    """

    def sort(self, nums: List[int]) -> List[int]:
        """

        :param nums: 整数列表
        :return: 排好序的新的整数列表
        """
        raise NotImplementedError()
