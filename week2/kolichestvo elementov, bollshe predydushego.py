a = int(input())
answer = 0
while a != 0:
    next = int(input())
    if next != 0 and a < next:
        answer += 1
    a = next
print(answer)
