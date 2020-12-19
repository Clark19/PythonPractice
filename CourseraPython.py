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


# !제일 많이 나오는 단어를 리턴하는 코드(From 텍스트 파일): 텍스트 라인들을 읽어, 나오는 단어들을 분류
"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
 The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
 The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
 they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum 
 loop to find the most prolific committer.
"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

wordCount = dict()
pieces = list()
for line in handle:
    if not line.startswith('From '): continue
    pieces = line.split()
    wordCount[pieces[1]] = wordCount.get(pieces[1], 0) + 1

bigWord = None
bigCnt = None
for word, cnt in wordCount.items():
    if bigCnt is None or cnt > bigCnt:
        bigWord = word
        bigCnt = cnt

print(bigWord, bigCnt)


# 출현 빈도 탑 10 단어 추출 코드: The top 10 most common words
fhand = open('romeo.txt')
counts = {}

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
    print(key, val)


"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
enumerate()
hourCnt = dict()
for line in handle:
    if not line.startswith('From '): continue
    pieces = line.split()
    time = pieces[5].split(':')
    hour = time[0]
    hourCnt[hour] = hourCnt.setdefault(hour,0) + 1

list = sorted([(k,v) for k,v in hourCnt.items()])
for k, v in list:
    print(k, v)