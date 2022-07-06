import pprint

s = [(x,y,z) for x in range( 5) for y in range(2,5) if x != y for z in range(4,5) if y != z]
pprint.pprint(s )

# 가독성 떨어뜨리는 주의 해야 할 리스트 컴프리헨션 예
strls = [str1[i: i+2].lower() for i in range(len(str)-1) if re.findall('[a-z]{2}', str1[i : i+2].lower())]

