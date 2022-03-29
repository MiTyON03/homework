import numpy as np

mas = np.random.randint(-99, 99, (9, 7))
pos = []

print("Массив 9*7:", "\n", mas, "\n")

for i in range(len(mas)):
    for j in mas[i]:
        if j > 0:
            pos.append(j)
print("Массив положительных чисел:", "\n", pos, "\n")


for i in range(len(pos)):
    x = pos[i]
    y = i - 1
    while y >= 0 and x < pos[y]:
        pos[y + 1] = pos[y]
        y = y - 1
    pos[y + 1] = x

print("Отсортированный массив:", "\n", pos)
