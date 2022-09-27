# 3 Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input().split()))
print(numbers)
single_numbers = []
for i in range(0, len(numbers)):
    count = 0
    for n in range(0, len(numbers)):
        if numbers[i] == numbers[n]:
            count += 1
            if count > 1:
                break
    if count == 1:
        single_numbers.append(numbers[i])
print(single_numbers)
