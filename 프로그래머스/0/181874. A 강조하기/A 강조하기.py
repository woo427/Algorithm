def solution(myString):
    answer = ''
    for char in myString:
        if char == "a":
            answer += "A"
        elif char == "A":
            answer += "A"
        else :
            answer += char.lower()
    return answer