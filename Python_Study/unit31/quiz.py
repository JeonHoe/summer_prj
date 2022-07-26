# 연습문제 : 회문 판독
from unittest import result


def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[len(word)-1]:
        return False
    return is_palindrome(word[1:-1])
print(is_palindrome('hello'))
print(is_palindrome('level'))

# 심사문제 : 재귀호출로 피보나치 수 구하기

def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))
