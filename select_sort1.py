def select_sort(li):
    for i in range(len(li)-1): #第i趟
        min_v = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_v]:
                min_v = j
        li[i],li[min_v] = li[min_v],li[i]
        print(li)

li = [3,5,8,7,5,1,4,9]
print(li)
select_sort(li)
