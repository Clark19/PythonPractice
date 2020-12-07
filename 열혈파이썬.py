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
print()
str = "ABCDEFG"
# str1 = str.
show_reverse2(str)
# show_reverse([1,2,3,4,5])

print(min(str))
print(max(str))

st = [1,2]
st[2:] = [3,4,5]
print(st)

def main():
    print("main:")
    num = 5; #int(input("input number: "))
    if num > 0:
        print("+")
    elif num < 0:
        print("-")
    else:
        print("0")

    print( 1 < num < 5)

    num = 0
    while num < 10:
        print(num, end = " ")
        num += 1
    print()

    num = 0
    expression = 3 * num /2
    while expression != 63:
        num += 1
        expression = 3*num / 2
    print(num)

    dc = {
        'clark': {'name': '박진화', 'minbun': 8001021, 'gender': '남성', 'height': 176},
        'minhye9': {'name': '구민혜', 'minbun': 8305312, 'gender': '여성', 'height': 170}
    }

    print(dc['clark'])
    print(dc['minhye9'])
    print(dc['clark']['gender'])
    print(dc['minhye9']['gender'])

main()


