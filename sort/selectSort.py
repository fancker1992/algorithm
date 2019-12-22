def select_sort(alist):
    n = len(alist)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]


if __name__ == '__main__':
    alist = [12, 3, 67, 8, 2, 99, 1, 7, 4]
    print(alist)
    select_sort(alist)
    print(alist)
