num = 0
try:
    while num != '#':
        for i in map(int, input().split()):
            num += i
        print(num)
except ValueError:
    print(num)