# 윤성우의 열혈 파이썬 기초편
# 리스트 챕터(5장) 내용 실습

st=  [ 1,2,3,4,5] + [8, 9]

# st[0], st[-1] = st[-1], st[0]
print(st)
print(st * 2)

st.reverse()
print(st)
st2 = list(reversed(st))
print(st2)

st3 = [1,2,3,4,5]
st3[1:4] = [3]
print(st3)

st3 = [1,2,3,4,5]
# st3.insert(3, 3.5)
# st3[2:4] = [3,3.5,4]
print(st3)
print(st3.index(3))
st3 = []
print(st3)

st =  [1,2,3,4,5,6,7,8,9,10]
print(st[::2])
print(st[1::2])


def show_reverse(list):
    idx = range(len(list))
    indices = reversed(idx)
    for i in indices:
        print(list[i], end=" ")

def show_reverse2(list):
    for i in range(len(list)):
        print(list[(i+1) * -1], end=", ")

str = "ABCDEFG"
# str1 = str.
show_reverse2(str)
# show_reverse([1,2,3,4,5])
