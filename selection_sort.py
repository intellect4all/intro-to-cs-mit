def selection_sort(L):
    start_suffix = 0

    while start_suffix != len(L):
        for i in range(start_suffix, len(L)): 
            if L[i] < L[start_suffix] :
                L[start_suffix], L[i] = L[i], L[start_suffix]
        start_suffix+=1
    return L

testList = [10,4,43,32,5,632,54,32,5,2,5,3,678,232,547,32,4,3,2,67,8,5,3]

print(selection_sort(testList))