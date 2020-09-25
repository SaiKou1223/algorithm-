import random


def bubble_sort(li):
    for i in range(len(li) - 1): #第i趟
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        print(li)
        if not exchange:
            return
            

li = [random.randint(0,1000) for i in range(10)]
print(li)
bubble_sort(li)
print(li)