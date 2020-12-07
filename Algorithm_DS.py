"""
*최소 공배수(lcm) 구하기
 : 최소 공배수란? 두 자연수 a, b 가 있을때 a(젯수, divisor)로도 나누어 떨어지고, b로도 나눠도 나머지가 0인
   자연수 중 제일 작은 수 n(피젯수,dividend).
 - 파이썬:
"""
# 6과 45의 최소공배수를 while 루프로 구현해봐라
lcm = 0
n = 45
while True:
    if n % 6 == 0 and n % 45 == 0:
        lcm = n
        break
    n += 1
print(f'lcm 최소 공배수: {lcm}')


"""
*최대 공약수(gcm) 구하기
 : 최대 공약수란? 두 자연수 a, b 가 있을때 a(피젯수,dividend)도 나눌수 있고, b를 나눠도 나머지가 0인 자연수 n(젯수, divisor).
"""
#  42와 120의 최대공약수를 구하라. while 루프 기반으로
gcm = 0
n = 42
while True:
    if 42 % n == 0 and 120 % n == 0:
        gcm = n
        break
    n -= 1
print(f'gcm 최대 공약수: {gcm}')