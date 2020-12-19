"""
'객체처럼 다뤄지는 함수 그리고 람다' 강의 실습
 : 함수도 객체이다(파이썬은 클래스도 객체로 다룬다. 파이썬은 모든걸 객체로 다룬다)
 : 이름 없이 만들어진 함수를 가리켜 '람다 함수(lambda function)' 또는 '람다식(lambda expression) 또는 람다(lambda)라 부른다'
 : 람다의 기본 구조: lambda [args(매개변수)]: expression(함수내용/몸체)
"""
# 객체인 함수 실습
def make_exponent(exp):
    def exponent(base_num):
        return base_num ** exp
    return exponent

pow2 = make_exponent(2)
pow3 = make_exponent(3)
pow4 = make_exponent(4)
print(f'squre: {pow2(3)}')
print(f'cube: {pow3(3)}')
print(f'3 to the 4th power: {pow4(3)}')

def show(s):
    print(s)

ref = show
ref('hi')

# 람다 실습
ref = lambda s: print(s)
ref('oh')

# 위 make_exponent(exp) 함수 람다로 만들어보기
exp = lambda base, exp: base ** exp
print(f'3의 4승 = {exp(3, 4)}')

showExpResult = lambda base, exponent: print(f'{base} to the {exponent}th power:', exp(base, exponent))
showExpResult(5, 3)
print('5 to the 3th power', str(exp(5, 3)))


# namedtuple 사용 예
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "job"])

a = Person(name="홍길동", age=25, job="Programmer")
b = Person("김철수", 32, "Manager")
c = Person("김영희", 41, "Designer")

for person in [a, b, c]:
    print("이름:%s" % person.name)
    print("나이:%s" % person.age)
    print("직업:%s" % person.job)



# Iterable 객체, Iterator 객체 실습
ds = [1,2,3,4]
ir = iter(ds)
print(next(ir)) # special method 직접 호출하지 않아도 인터프리터에 의해 호출되는 메서드 : 형태 = __xx__
print(next(ir))
print(next(ir))
print(next(ir))
try: print(next(ir))
except StopIteration as e: print('StopIteration exception',e)
print(dir(ds))
print(hasattr(ds, '__iter__'))

# iterator 객체는 iterable 객체이다 -> for 루프에 와도 됨.
ir = iter([1,2,3])
for i in ir:
    print(i, end =' ')
print()
ir1 = iter([1,2,3])
ir2 = iter(ir1)
print(ir1 is ir2) # True
print(id(ir1))
print(id(ir2)) # ir1 is ir2.


# set, srozenset
A = set(['a', 'c','d','f'])
B = set('fdca')
print(A)
print(B)
print(A==B)
B.add('p')
print('a' in A)
print('b' not in B)
for c in A & B:
    print(c, end=' ')
d = {} # empty dictionary
print(type(d))
s = set() # empty set
print(type(s))

# removing duplication in using Set
t = [3,3,3,7,7,'z','z']
t = list(set(t))
print(t); print()

# 정렬
ns = [('Park', 29), ('Yoon', 33), ('Lee', 12), ('Park', 11)]
def age(t):
    return t[1]
ns.sort(key=age, reverse=True)
ns.sort(key = lambda t : t[1], reverse=True)
# ns.sort()
print('ns:', ns)

# dictionary 에 대한 정렬
dic = {'cd': 7, 'ab': 10, 'cc':7, 'gh': 8, 'cf':7, 'ef':9}
# sdic = sorted(dic.items()) # 키 이외의 다른 값도 정렬하고 싶으면 dict.items() 방식 사용하지 말것.
sdiclist = [(k,v) for k,v in dic.items()]
# sdiclist.sort() # 원본 수정 방식
# sdiclist.sort(key= lambda t: t[1], reverse=True)
lst = sorted(sdiclist) # 원본 수정않고 새 리스트 생성 방식
lst = sorted(lst, key=lambda t: t[1], reverse=True)
print(f'dic: {dic}')
print('sdiclist', sdiclist)
print(f'SORTED() DICT: {lst}')

org = ('321', '214', '197')
cpy = tuple(sorted(org, key=lambda s: s[0]))
print(cpy)


names = ['윤나은', '김현주', '장현지', '이지선', '박선주']
dnames = {k:v for k,v in enumerate(sorted(names), 1)}
print(f'\ndnames: {dnames}')

# 표현식 기반 문자열 조합
print('\n표현식 기반 문자열 조합')
s = 'My friend %s is %d years old and %fcm tall.' % ('Jung', 22, 178.5)
print('문자열 조합:', s)
s = 'My friend %s is %s years old and %scm tall.' % ('Jung', 22, 178.5)
print('문자열 조합2:', s)
dic = {'name': 'Yoon', 'age': 22}
s = "%(name)s : %(age)d" % dic
s2 = "%(name)s : %(age)d" % {'name': 'Yoon', 'age': 22}
print('문자열 조합3-1-(딕셔너리 이용):', s)
print('문자열 조합3-2-(딕셔너리 이용):', s2)

print('height: %f' % 3.14)
print('height: %.2f' % 3.14)
print('height: %7.2f' % 3.14)
print('height: %07.2f' % 3.14)
print('height: %010.2f' % 3.14)
print('height: %-7.2f입니다.' % 3.14)
print('height: %-10.2f입니다.' % 3.14)
print('num: %+d' % 3)
print('num: %+d' % -1)
print('height: %-+10.3f' % 3.14)
print('%(h)s: %(v)-+10.3f' % {'h': 'height', 'v': 3.14})

# 메서드 기반 문자열 조합: (장점) 표현식(%)기반보다 다양한 옵션 지정가능 & 코드 유연하게 작성가능(ex. 언패킹 활용)
print('\n메서드 기반 문자열 조합: (장점) 표현식(%)기반보다 다양한 옵션 지정가능 & 코드 유연하게 작성가능(ex. 언패킹 활용)')
print('{0}...{1}...{2}'.format('Robot', 125, 'Box'))
print('{2}...{1}...{0}'.format('Robot', 125, 'Box'))
print('{}...{}...{}'.format('Robot', 125, 'Box'))
print('{toy}...{num}...{item}'.format(toy='Robot', num=125, item='Box'))
my = ['Robot', 125, 'Box']
print('언패킹 방식: {0}...{1}...{2}'.format(*my))
print('배열 방식: {0}...{1}...{2}'.format(my[0], my[1], my[2]))
my = ['Box', (24, 31)]
print('인덱싱 방식: {0[0]}...{0[1]}...{1[0]}..{1[1]}'.format(*my))
d = {'toy': 'Robot', 'price': 3500}
print('toy = {0[toy]}, price = {0[price]}'.format(d))
print('표현식 기반 문자열 조합: %9.4f' % 3.14)
print('메서드 기반 문자열 조합: {0:9.4f}'.format(3.14))
print('w정렬: {0:<10.4f}'.format(3.14))
print('{0:>10.4f}'.format(3.14))
print('{0:^10.4f}'.format(3.14))
print('표현식 기반 문자열 조합: %+d, %+d' % (5, -5))
print('메서드 기반 문자열 조합: {0:+d}, {1:+d}'.format(5, -5))
print('메서드 기반 문자열 조합(생략1): {0:+}, {1:+}'.format(5, -5))
print('메서드 기반 문자열 조합(생략2): {:+}, {:+}'.format(5, -5))
print('{0:*^10.4f}'.format(3.14))
print('{0:+<10}'.format(7))
print('{0:^^10}'.format('hi'))
