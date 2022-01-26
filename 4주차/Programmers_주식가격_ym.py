def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):  # 마지막은 항상 0
        while stack and stack[-1][1] > prices[i]:  # 가격이 떨어지면 stack 에서 pop 하고 답 저장
            idx, price = stack.pop()
            answer[idx] = i - idx
        stack.append((i, prices[i]))  # 스택에 가격 추가
    while stack:  # 끝까지 돌았는데 스택이 남았을 경우 처리
        idx, price = stack.pop()
        answer[idx] = n - 1 - idx

    return answer