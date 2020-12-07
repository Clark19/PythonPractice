import csv

# a[i] = dictionary {num, wnum, ynum} : 요일별로 각 시간대에 저장해야 할 데이터
# 7 x 24 크기의 리스트 필요 : 2차원 리스트 만들기
a = [[],[],[],[],[],[],[]]


# (실습) csv.DictReader(파일객체) : 딕셔너리 형식으로 데이터를 읽음
with open('passby_data.CSV', 'r') as f : #파일객체 f로 얻어옴
  # (실습) 딕셔너리 형식(csv.DictReader(f))으로 데이터 읽음
    reader = csv.DictReader(f)    # 열이름을 딕셔너리 key로 지정해 각 행(row)의 정보와 매핑해줌.
    i = j = 0                       # i (요일),  j(시간대)
    for row in reader :             # reader에서 한 행씩 꺼내서 row에 저장하고
       #(실습) 인덱스 i번째 리스트에 row 값을 추가함
        a[i].append(row)   #  j(시간대)의 {num, wnum, ynum}
        j = j + 1                   # j : 시간대 증가
        if(j % 24 == 0) :           # 24개의 행 추가(24시간)후, 다음 요일의 리스트로 이동
            i = i + 1               # 다음 요일의 리스트로 이동

x_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']

# 각 요일별 시간대 유동인구수 출력하기
for i in range (0, 7) :
    for j in range (0, len(a[i])) :
        print(x_title[i], "[", j, "] = ", a[i][j])