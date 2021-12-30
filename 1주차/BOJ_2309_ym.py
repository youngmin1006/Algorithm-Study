dwarf = [int(input()) for i in range(9)]

total = sum(dwarf)

for j in range(9):
    for k in range(j+1,9):
        first = dwarf[j]
        second = dwarf[k]
        if (first + second) == (total - 100):
            dwarf.remove(first)
            dwarf.remove(second)
            break
    if len(dwarf)<9:#for 문을 빠져나오는 처리 필요
        break

dwarf.sort()
for num in range(7):
    print(dwarf[num])