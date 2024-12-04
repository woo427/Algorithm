def solution(sizes):
    width = []
    height = []
    width_max = 0
    height_max = 0
    answer = 0
    
    for size in sizes:
        width.append(max(size))
        height.append(min(size))
                
    width_max = max(width)
    height_max = max(height)
    
    answer = width_max * height_max
    return answer