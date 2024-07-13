n = int(input())
stack = list(map(int, input().split()))
dig = -1
for i in range(n):
    last = stack.pop()
    if last % 2 == 0:
        dig = last
        break
print(dig)
