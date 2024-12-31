def solution(arr, n):
    arr_len = len(arr)
    answer = []
    
    if arr_len % 2 == 0 :
        for i in range(arr_len) :
            if i % 2 == 0 :
                answer.append(arr[i])
            else : 
                answer.append(arr[i] + n)
    else :
        for i in range(arr_len) :
            if i % 2 != 0 :
                answer.append(arr[i])
            else :
                answer.append(arr[i]+n)
    return answer