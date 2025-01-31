import math

def solution(array):
    center = len(array) / 2
    idx = math.floor(center)
    array.sort()
    return array[idx]
