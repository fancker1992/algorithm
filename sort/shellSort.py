def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):  # 类似插入排序，从每个数组的第二个元素开始与前面的有序数组进行比较
            i = j
            while (i - gap) >= 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


def shell_sort_2(alist):
    """希尔排序  方法二"""
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if j - gap >= 0 and alist[j] < alist[j - gap]:
                    alist[j], alist[j - gap] = alist[j - gap], alist[j]
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    alist = [2, 6, 43, 1, 0, 5, 3, 12]
    print(alist)
    shell_sort_2(alist)
    print(alist)
