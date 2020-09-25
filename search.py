def ser(li,target):
    left = 0
    right = len(li) - 1
    #二分查找
    while left <= right:
        mid = (left+right) // 2
        if li[mid] == target:
            return mid
        elif li[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,15]
print(ser(li,18))
