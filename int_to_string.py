def intTOStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    res = ''
    count = 0;
    while i > 0:
        print("First i ", i)
        print('i % 10', i%10)
        res = digits[i%10] + res
        i = i//10
        print("second i ", i)
        count+= 1
    return res;


# print(intTOStr(0))
print(intTOStr(584493))
# intTOStr(584493)
# intTOStr(58449748393)
# intTOStr(123456789)