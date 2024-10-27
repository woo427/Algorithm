str = input()

answer = ''

for i in str:
    if i.isupper() == True:
        answer += i.lower()
    else :
        answer += i.upper()

print(answer)
