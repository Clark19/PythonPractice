"""
이진수 변환
10진수를 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단, 재귀호출을 이용하여 작성합니다.

입력 예시
10      19

출력 예시
1010    10011
"""

import sys

sys.setrecursionlimit(100000)


def convertBinary(n):
    '''
    10진수 n을 2진수로 변환하여 반환합니다.

    *주의* : 변환된 2진수는 문자열이어야 합니다.

    예를 들어, 19가 입력될 경우 문자열 "10011"이 반환되어야 합니다.
    '''
    dividend = n
    quotient = 0 # 몫
    remainder = 0
    stack = []
    answer = ""

    while quotient != 1:
        quotient = dividend // 2
        # 몫: 5
        remainder = dividend % 2
        # 나머지: 0, => 이진수의 첫째자리

        dividend = quotient  # 이전 연산의 몫이 다음 연산시 피젯수가 됨
        stack.append(str(remainder))
    stack.append(str(quotient))



    for i in range(len(stack)):
        answer += stack.pop()

    return answer

# 재귀 방식으로 만들어 볼 것 - 만들다 만것
def recur(quotient):
    result = {}
    if quotient == 1:
        # return or set
        print('')
    else:
        print("")
    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    # input()
    n = int(10)

    print(convertBinary(n))


if __name__ == "__main__":
    main()
