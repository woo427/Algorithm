def solution(participant, completion):
    hashDict = {}
    sum = 0
    for name in participant:
        hashDict[hash(name)] = name
        sum += hash(name)
    for i in completion:
        sum -= hash(i)
    return hashDict[sum]