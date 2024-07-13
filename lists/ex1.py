n = int(input())
array = list(map(int, input().split()))
element = int(input())
cnt = 0
for i in range(n):
    if array[i]!=element:
        cnt+=1
print(cnt)