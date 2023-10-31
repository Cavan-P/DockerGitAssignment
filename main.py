import sys

data = sys.stdin.readlines()

n = data[0]
values = data[1].split(' ')

sum = 0

for i in values:
    sum += int(i)

print(sum//int(n))