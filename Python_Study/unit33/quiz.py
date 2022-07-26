# 연습문제
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count

c = counter()
for i in range(10):
    print(c(), end=' ')

print('\n')

# 심사문제
def countdown(n):
    i = n + 1
    def count():
        nonlocal i
        i -= 1
        return i
    return count


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')


