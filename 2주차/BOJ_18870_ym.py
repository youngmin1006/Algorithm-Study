N = int(input())
num = list(map(int,input().split()))
sorted_arr = sorted(list(set(num)))#중복 제거, 정렬 후 num 값을 해당 arr에서 찾아 그 인덱스 값을 반환
dic = {sorted_arr[i] : i for i in range(len(sorted_arr))} #enumerate 사용하면 더 효율적임.
for i in num:
    print(dic[i], end = ' ')#처음엔 dictionary쓰지 않고 sorted_arr.index[i]로 시도 -> O(n) 시간초과 발생, 딕셔너리로 바꿈