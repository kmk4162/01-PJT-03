import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
start_list = ['3', '4', '5', '6', '9']

for test_case in range(T):
    number = input()
    if '-' in number:
        x = number.split('-')
        number = ''.join(x)
        # - 있으면 split로 나누고 다시 join으로 - 제거
    if number[:1] not in start_list:
        print(f'#{test_case + 1} 0')
    elif len(number) != 16:
        print(f'#{test_case + 1} 0')
    else:
        print(f'#{test_case + 1} 1')
