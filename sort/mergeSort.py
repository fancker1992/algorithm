def merge_sort(alist):
    n = len(alist)
    if n == 1:  # 递归必须有条件退出   否则下面的语句会报错None相关错误
        return alist
    mid = n // 2

    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    left, right = 0, 0
    left_n = len(left_list)
    right_n = len(right_list)
    merge_list = []
    while left < left_n and right < right_n:
        if left_list[left] <= right_list[right]:
            merge_list.append(left_list[left])
            left += 1
        elif left_list[left] > right_list[right]:
            merge_list.append(right_list[right])
            right += 1
    merge_list += left_list[left:]
    merge_list += right_list[right:]
    return merge_list


if __name__ == '__main__':
    alist = [23, 6, 34, 55, 76, 1, 0, 11, 5]
    print(alist)

    print(merge_sort(alist))
