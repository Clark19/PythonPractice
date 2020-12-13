"""
Coursera 'Python for everybody' = py4e
강의 실습: 파이썬 기초 마지막 강의

"""
"""
문제. 5.2 Write a program that repeatedly prompts a user for integer numbers
 until the user enters 'done'. Once 'done' is entered, print out the largest
 and smallest of the numbers. If the user enters anything other than a valid
 number catch it with a try/except and put out an appropriate message 
and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num2 = int(num)
    except:
        print('Invalid input')
        continue
    if largest == None:
        largest = num2
    elif num2 > largest:
        largest = num2

    if smallest == None:
        smallest = num2
    elif num2 < smallest:
        smallest = num2

#print(num)


print("Maximum is", largest)
print("Minimum is", smallest)
