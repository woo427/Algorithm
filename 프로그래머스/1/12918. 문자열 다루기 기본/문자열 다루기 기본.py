def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if ord(i) < 48 or ord(i) > 57:
                return False
            else:
                continue
        else:
            return True
    else:
        return False