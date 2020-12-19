"""
'객체처럼 다뤄지는 함수 그리고 람다' 강의 실습
 : 함수도 객체이다(파이썬은 클래스도 객체로 다룬다. 파이썬은 모든걸 객체로 다룬다)
 : 이름 없이 만들어진 함수를 가리켜 '람다 함수(lambda function)' 또는 '람다식(lambda expression) 또는 람다(lambda)라 부른다'
 : 람다의 기본 구조: lambda [args(매개변수)]: expression(함수내용/몸체)
"""
import collections

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
print(t)


