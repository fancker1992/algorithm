def insert_sort(alist):
    n = len(alist)

    for i in range(1, n):  #从第二个元素开始与前一个有序数组中元素比较
        for j in range(i, 0, -1):  # 此处注意  j移动到1即可 否则j = 0时j-1 = -1
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            else:
                break   # alist左侧已为有序  不必进行无畏的循环判断


if __name__ == '__main__':
    alist = [12, 5, 34, 7, 8, 32, 1, 0]
    print(alist)
    insert_sort(alist)
    print(alist)
