def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:
        return
    mid = alist[end]  # mid = end  先从左侧向右侧赋值，mid = start，则先从右侧向左侧赋值
    left = start
    right = end
    while left < right:

        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]
        while left < right and alist[right] >= mid:
            right -= 1
        alist[left] = alist[right]

    alist[left] = mid
    quick_sort(alist, start, left - 1)
    quick_sort(alist, left + 1, end)


if __name__ == '__main__':
    li = [23, 64, 1, 7, 90, 34, 54, 77, 2, 110]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
