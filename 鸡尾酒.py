def cock(list):
    for i in range(len(list)//2):
        is_sorted = True
        for j in range(i,len(list)-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                is_sorted = False
                print(list,1)
        if is_sorted:
            break
        is_sorted = True
        for j in range(len(list)-i-1,i,-1):
            if list[j] <list[j-1]:
                list[j],list[j-1] = list[j-1],list[j]
                is_sorted = False
                print(list,2)
        if is_sorted:
            break

import random
li = [random.randint(0,1000) for i in range(10)]
print(li)
cock(li)
print(li)