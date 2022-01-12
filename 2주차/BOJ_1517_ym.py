import sys
N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
cnt = 0
def mergeSort(start, end):
    global cnt
    if start < end:
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)

        low_index= start
        high_index = mid + 1
        tmp = []
        while low_index <= mid and high_index <= end:
            if arr[low_index] <= arr[high_index]:
                tmp.append(arr[low_index])
                low_index += 1

            else:
                tmp.append(arr[high_index])
                high_index += 1
                cnt += (mid - low_index + 1)  # 스와핑 했을 때 개수추가
        if low_index <= mid:
            tmp = tmp + arr[low_index:mid+1]
        if high_index <= end:
            tmp = tmp + arr[high_index:end+1]

        for i in range(len(tmp)):
            arr[start + i] = tmp[i]

mergeSort(0,N-1)
print(cnt)
#합병정렬로 풀이.
#출처: https://gaza-anywhere-coding.tistory.com/105