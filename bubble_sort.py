def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ', str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp





testList = [10,4,43,32,5,632,54,32,5,2,5,3,678,232,547,32,4,3,2,67,8,5,3]
print(bubble_sort(testList))
