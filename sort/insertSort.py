def insert_sort(alist):
    n = len(alist)

    for i in range(1, n):
        for j in range(i, 0, -1):  # 此处注意  j跟到1即可 否则j = 0时j-1 = -1
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


if __name__ == '__main__':
    alist = [12, 5, 34, 7, 8, 32, 1, 0]
    print(alist)
    insert_sort(alist)
    print(alist)
