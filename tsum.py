def twosum(nums,target):
    n = len(nums)
    for i in range(n):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [j,i]

li = [1,2,3,4,5,6,7,8,9]
print(twosum(li,10))