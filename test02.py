#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 21:57:19
# @Author  : wangshaobo (370788717@qq.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$


def bubble_sort(arr):
    count = len(arr)
    for j in range(count - 1):
        for i in range(count - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


if __name__ == "__main__":
    arr = [1, 5, 2, 3, 2, 6, 4, 4]
    bubble_sort(arr)
    print(arr)
    ii = input('input')
    print(type(ii))
