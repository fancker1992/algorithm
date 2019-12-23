def shell_sort(alist):
    """希尔排序"""
    n = len(alist)

    gap = n // 2

    # while gap >= 1:
        # for j in range(gap, n + 1):
        #     if alist[j] < alist[j - gap]:
        #         alist[j], alist[j - gap] = alist[j - gap], alist[j]
        #
        # gap //= 2


if __name__ == '__main__':
    alist = [2, 6, 43, 1, 0, 5, 3, 12]
    shell_sort(alist)
    print(alist)
