def solution(word):
    words = 'AEIOU'
    dic = []
    
    def dfs(cnt, w):
        if cnt == 6:
            return
        for i in range(len(words)):
            dic.append(w + words[i])
            dfs(cnt+1, w + words[i])
            
    dfs(1, '')
    return dic.index(word) + 1