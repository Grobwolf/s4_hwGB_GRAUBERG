# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input())
s_multi = []
d = 2
while d * d <= n:
    if n % d == 0:
        s_multi.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    s_multi.append(n)
print(s_multi)
