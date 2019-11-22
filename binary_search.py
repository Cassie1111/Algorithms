# 二分查找及变式


# 普通的二分查找
# 闭区间 【L, R】
# 循环条件为 L <= R
def bs1(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == key:
            return m
        if arr[m] < key:
            l = l + 1
        else:
            r = r - 1

    return -1


# 右开区间[L, R)
# 循环条件 L < R
def bs2(arr, key):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r-l) // 2
        if arr[m] == key:
            return m
        if arr[m] > key:
            r = m
        else:
            l = m + 1

    return -1


# 多个相同key，返回第一个
# 循环条件 L <= R
def bs3(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] >= key:
            r = m - 1
        else:
            l = m + 1

    if l < len(arr) and arr[l] == key:
        return l

    return -1


# 第一个 >= key
# 循环条件 L <= R
def bs4(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] >= key:
            r = m - 1
        else:
            l = m + 1

    return l


# 第一个 > key
# 循环条件 L <= R
def bs5(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] > key:
            r = m - 1
        else:
            l = m + 1

    return l


# 最后一个 = key
# 循环条件  L <= R
def bs6(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] <= key:
            l = m + 1
        else:
            r = m - 1

    if r >= 0 and arr[r] == key:
        return r

    return -1


# 最后一个 <= key
# 循环条件 L <= R
def bs7(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] <= key:
            l = m + 1

        else:
            r = m - 1

    return r


# 最后一个 < key
# 循环条件 L <= R
def bs8(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] < key:
            l = m + 1
        else:
            r = m - 1

    return r


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8]
    print(bs1(arr, 4))
    print(bs2(arr, 5))
    print(bs3(arr, 7))
    print(bs3(arr, 8))
    print(bs4(arr, 5))
    print(bs5(arr, 5))
    print(bs6(arr, 6))
    print(bs7(arr, 7))
    print(bs8(arr, 7))