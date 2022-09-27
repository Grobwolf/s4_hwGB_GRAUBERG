# 1 Вычислить число π c заданной точностью d
#
# *Пример:*
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = 0.001  # До 8 знаков точно считает, а начиная с 9-го вычисления длятся слишком долго.
n = 0
s2 = 0
n += 1
s1 = s2 + 4 / ((2 * n) - 1)
n += 1
s2 = s1 - 4 / ((2 * n) - 1)
while s1 - s2 >= d:
    n += 1
    s1 = s2 + 4 / ((2 * n) - 1)
    n += 1
    s2 = s1 - 4 / ((2 * n) - 1)
pi = str(((s1 + s2) / 2))
d = str(d)
length_pi = 0
print(d)
if len(d) == 5 and d[4] != str(1):
    length_pi = d[4]
elif len(d) == 5 and d[3] != str(0):
    print(pi)
    quit()
else:
    length_pi = len(d) - 2
print(length_pi)
for i in range(0, (int(length_pi) + 2)):
    print(pi[i], end="")
