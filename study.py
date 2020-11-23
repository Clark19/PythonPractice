import numpy as np
from pprint import pprint
#안녕
d = np.array([[1,2,3,4,5],
    [2,4,5,6,7],
    [5,7,8,9,9]])

print(d[1][2])
print(d[1, 2])
print(d[1:, 3:])

pprint(d, indent=4, width=30)

def adder(num1, num2):
    return num1 + num2

print(adder(5, 3))

def test_method(n1, n2):
    sum = n1 + n2
    print(sum)
    return sum

def no_param_method():
    test_method(2, 3)

# 올바른 호출문은 test_method(2, 3)과 no_param_method() 이다
test_method
no_param_method