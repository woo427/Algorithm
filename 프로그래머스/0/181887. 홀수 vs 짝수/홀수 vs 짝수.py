def solution(num_list):
    odd = 0
    even = 0
    for i in range(0,len(num_list),2):
        odd += num_list[i]
    for j in range(1,len(num_list),2):
        even += num_list[j]
    if odd <= even:
        return even
    else :
        return odd