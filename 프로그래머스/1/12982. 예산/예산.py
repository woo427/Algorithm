def solution(d, budget):
    d.sort()
    for idx in range(len(d)):
        budget -= d[idx]
        if budget < 0:
            return idx
    return idx+1