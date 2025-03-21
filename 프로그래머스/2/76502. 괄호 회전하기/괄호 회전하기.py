def solution(s):
    answer = 0
    for i in range(len(s)):
        rotate = s[i:] + s[:i]
        if is_valid(rotate):
            answer += 1
    return answer

def is_valid(rotate):
    stack = []
    value = ""
    
    for ch in rotate:
        if ch in "({[":
            stack.append(ch)
        else :
            if not stack:
                return False
            value = stack.pop()
            if ch == ")" and value != "(":
                return False
            elif ch == "}" and value != "{":
                return False
            elif ch == "]" and value != "[":
                return False
    if not stack:
        return True