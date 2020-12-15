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

print("Maximum is", largest)
print("Minimum is", smallest)


"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines
 of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values
and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing 
below enter mbox-short.txt as the file name.
"""
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
cnt = 0
fnum = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    # print(line)
    pos = line.find(':')
    fnum += float(line[pos + 1:].strip())
    cnt += 1

print("Average spam confidence:", fnum / cnt)


"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words 
using the split() method.
 The program should build a list of words. For each word on each line check to see if the word is already in the list
and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()

for line in fh:
    lst = line.split()
    for word in lst:
        if word not in words:
            words.append(word)

words.sort()
print(words)


"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of 
the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output 
to see how to print the count.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname)
count = 0
pieces = list()

for line in fh:
    if not line.startswith('From '): continue
    pieces = line.split()
    print(pieces[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")
