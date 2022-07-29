import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for test_case in range(T):
    cnt = 0
    numbers = list(map(int, input().split()))
    for i in range(len(numbers)):
        if i % 2 == 0:
            cnt += (numbers[i] * 2) # 홀수번째 자리는 곱하기 2하고 더하기
        else:
            cnt += numbers[i]       # 짝수번째는 그냥 더하기
    digit = cnt % 10 # 1~15번째 자리까지 더한 수의 일의 자리 찾기
    if digit == 0:
        result = 0
    else:
        result = 10 - digit
    # 이전까지 합의 일의자리가 0이면 이미 룬 공식 만족하므로 N이 0이고
    # 나머지 경우는 digit와 result를 더해서 10이 돼야하기 때문에
    # result = 10 - digit
    print(f'#{test_case + 1} {result}')
