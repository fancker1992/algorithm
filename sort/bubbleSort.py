def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for i in range(n - 1):
        count = 0
        for j in range(n - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        if count == 0:  # 若列表完全正序，循环一遍即可退出
            break


if __name__ == '__main__':
    alist = [23, 5, 88, 1, 56, 44, 89, 90, 23, 2]
    bubble_sort(alist)
    print(alist)
