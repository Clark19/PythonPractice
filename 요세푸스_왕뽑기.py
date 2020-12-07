# 엘리스 프리트랙 - 체셔의 논리력 퀴즈6. 동물의 왕 - 왕 뽑기 문제
# '요세푸스 문제 (Josephus Problem)' 라는 전산학, 수학 분야에서 유명한 문제를 재구성한 퀴즈

survivors = list(range(1, 101))
# print(len(survivors))
stickownerIndex = 0

while len(survivors) > 1:
    loserIdx = (stickownerIndex + 1) % len(survivors)
    del survivors[loserIdx]
    stickownerIndex = loserIdx

print(survivors)

x=2
if(x%2==0):
    print(str(x) + '는 짝수입니다.')
else:
    print(str(x)+'는 홀수입니다.')

