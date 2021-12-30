def isHan(num):
    if num<100 or num>=1000:
        return 0
    else:
        hun = num//100
        ten = (num-(hun*100))//10
        one = num - (hun *100 + ten*10)
        if hun - ten == ten - one:
            return 1


num = int(input())
result = 0
if num < 100:
    result = num
else:
    result = 99
    for i in range(100, num + 1):
        if isHan(i) == 1:
            result += 1
        else:
            continue

print(result)