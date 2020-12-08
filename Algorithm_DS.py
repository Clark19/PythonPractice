# 최대공약수(GCD), 최소공배수(LCM) 구현하기
"""
* 최대 공약수란?
 : 두 개 이상의 자연수의 공통된 약수 중 최대로 큰 수.
 : 두 자연수 a, b 가 있을때 a(피젯수,dividend)도 나눌수 있고, b를 나눠도 나머지가 0인 자연수 n(젯수, divisor).

< 최대 공약수 (인간이) 계산하는 세가지 방법 > - https://mathbang.net/202
1. 모든 약수를 구해서 그 중에 제일 큰거
2. 공약수로 나누기 - 소인수 분해처럼 공약수로 나눈후 다 나누어 떨어지면(나머지가 0),
   이 나누는 (소수가 아니여도 됨)공약수들의 곱이 최대 공약수.
3. 지수이용 - (조건: 소인수 분해 되있어야 함.) 두 수에 공통인 소수 중에서 지수가 더 작은 것들의 곱
4. 유클리드 호제법 이용 - "유클리드 알고리즘" 원리.
임의의 두 자연수 a, b가 주어졌을때. 둘중 큰 값이 a라고 가정해보겠습니다.
a를 b로 나눈 나머지를 n 이라고 하면 (a%b = n)
n이 0일때, b가 최대 공약수(GCD)입니다.
만약 n이 0이 아니라면, a에 b값을 다시 넣고 n를 b에 대입 한 후 다시 위에 step2부터 반복하면 됩니다.

< 최대 공약수(gcd) (코딩) 구현하는 세가지 방법 >
 1. 반복문 이용, 2.유클리드 호제법 이용(반복문), 3.유클리드 호제법 이용(재귀 함수)

 42와 120의 최대공약수를 구하라.
"""

# 1. 반복문 이용 (ex. while 루프)
# 두 정수 a,b에 대하여 O(min(a,b))의 시간 복잡도를 가짐. -> 시간 많이 걸릴 가능성 있음.
gcd = 0
n = 42
while True:
    if 42 % n == 0 and 120 % n == 0:
        gcd = n
        break
    n -= 1
print(f'gcm 최대 공약수: {gcd}')

# 2. 유클리드 호제법 & 반복문 이용
#  정수 a,b 에 대하여 O(log2(min(a,b))시간 복잡도 가짐
def gcd(num1, num2):
    # if (num2 > num1): # 큰 수 빠꿔주는 루틴 없어야 더 빠름. 이거 없어도 처음 연산시 한번 알아서 바뀜.
    #     num1, num2 = num2, num1
    while(num2 != 0):
        remainer = num1 % num2
        num1, num2 = num2, remainer
    return num1

# 3. 유클리드 호제법 & 재귀 함수이용
def gcd_recur(num1, num2):
    remainer = num1 % num2
    if remainer:
        return gcd_recur(num2, remainer)
    else:
        return num2
# 3-1. 유클리드 호제법 & 재귀 함수 & 삼항 연산자 축약형 (자바/kotlin나 C/C++)
# def gcd_recur2(num1, num2):
#     return num1 % num2 == 0 ? num2 : gcd_recur2(num2, num1 % num2)

print(f'gcd 최대 공약수: {gcd(42,120)}')
print(f'gcd 최대 공약수2: {gcd(33,22)}')
print(f'gcd Recursive 최대 공약수: {gcd_recur(42,120)}')
print(f'gcd Recursive 최대 공약수2: {gcd_recur(33,22)}')


"""
* 최소 공배수란?
 : 2개 이상의 자연수의 공통된 배수중 가장 작은 수
 : 두 자연수 a, b 가 있을때 a(젯수, divisor)로도 나누어 떨어지고, b로도 나눠도 나머지가 0인 자연수 중 제일 작은 수 n(피젯수,dividend).

< 최소 공배수(lcm) (수학적) 구하는 방법 > - https://mathbang.net/204
 1. 공배수를 모두 구한다. 그 중에 제일 작은 수.
 2. 공약수로 나누기 - 최대 공약수 구하기와 유사하게 서로소가 나올때 까지 공약수로 계속 나눈 후, 공약수에 서로소까지 곱하면 됨.
    만약, 세 자연수의 최소공배수를 구한다면, 세 수에서 공약수를 찾을 수 없을 때는 두 수를 선택해서 둘의 공약수로 나눔.
    세 수에서 모두 서로소가 나올 때까지 계속 나눔.
3. 지수 이용 - (소인수분해를 해서 지수가 나오게 수를 바꾸거나 소인수분해된 상태에서 사용)
   공통된 소수 중 지수가 높은 수들과 공통되지 않은 모든 소수 곱. 

< 최소 공배수(lcm) (코딩) 구현하는 방법 - 파이썬>
1. (Brute force) 반복문 이용
2. 최소 공배수 공식 이용(최대 공약수를 이용): 최소공배수 x 최대공약수 = A x B
   => (A x B)/최대공약수
"""
# 6과 45의 최소공배수를 while 루프로 구현해봐라
num1, num2 = 6, 45

# 1. (Brute force) 반복문 이용.
lcm = 0
n = 45
while True:
    if n % 6 == 0 and n % 45 == 0:
        lcm = n
        break
    n += 1
print(f'lcm 최소 공배수: {lcm}')


# 2. 최대공약수 이용
# ab/gcd(a,b)
def gcd(num1, num2):
    remainer = num1 % num2
    if remainer:
        return gcd(num2, remainer)
    else:
        return num2

def lcm(num1, num2):
    return num1*num2 // gcd(num1, num2)

print(f"lcm: {lcm(num1, num2)}")