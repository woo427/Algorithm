def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    total1 = 0
    total2 = 0
    if a < b :
        return -1
    elif a > b :
        return 1
    else :
        for num1 in arr1 :
            total1 += num1
        for num2 in arr2 :
            total2 += num2
        if total1 == total2 :
            return 0
        elif total1 < total2 :
            return -1
        else :
            return 1
