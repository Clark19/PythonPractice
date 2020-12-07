for outidx in range(6):
    for i in range(6):
        # print("move()")
        print(".pick_carrot()")

    if (outidx % 2) == 0:
        print(".turn_left()")
        # rabbit.move()
        # rabbit.turn_left()
    else:
        print("turn_right")
        # rabbit.move()
        # turn_right

print(0 % 2 == 0)

"""
당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *

가로, 세로 길이가 8, 7인 당근밭을 소환합니다.
create_world(avenues=8, streets=7)

create_world(avenues=5, streets=5)
create_world(avenues=10, streets=7)
토끼를 소환하고 토끼의 경로를 표시합니다.
rabbit = Rabbit()
rabbit.set_trace(‘blue’)
rabbit.set_pause(0.1)

여러분의 코드를 작성해주세요!
"""

# 2. 토끼가 당근 위에 있을 때 당근을 줍는 반복문을 쓰세요.
while rabbit.on_carrot():
    rabbit.pick_carrot()
# 창고에 갔으면 토끼가 당근을 갖고 있으면 당근을 놓는 반복문을 쓰세요.
while rabbit.carries_carrots():
    rabbit.drop_carrot()
rabbit.front_is_clear()
rabbit.on_carrot()

rabbit.carries_carrots(), front_is_clear(), on_carrot()

# no.2
def turn_right():
    rabbit.turn_left()
    rabbit.turn_left()
    rabbit.turn_left()


is_find = False
for o in range(4):
    for i in range(4):
        rabbit.move()
        if (rabbit.on_carrot()):
            rabbit.pick_carrot()
            is_find = True
            break
    if is_find == False:
        turn_right()

# No.3
def turn_right():
    rabbit.turn_left()
    rabbit.turn_left()
    rabbit.turn_left()


while rabbit.on_carrot() == False:
    if rabbit.front_is_clear():
        rabbit.move()

rabbit.pick_carrot()
rabbit.turn_left()
rabbit.turn_left()

while rabbit.front_is_clear():
    rabbit.move()
rabbit.drop_carrot()

# no4.
def turn_right():
    rabbit.turn_left()
    rabbit.turn_left()
    rabbit.turn_left()

for i in range(4):
    rabbit.move()
    turn_right()
    rabbit.move()
    if rabbit.on_carrot():
        rabbit.pick_carrot()
    rabbit.turn_left()


# no.5
# 좌표 (1.1)에 모든 당근이 있고, 가로줄 (1,3,5,7,...)에만 (칸마다)모두 당근을 심어라.
def turn_right():
    rabbit.turn_left()
    rabbit.turn_left()
    rabbit.turn_left()

def go_right_and_drop():
    global row_num
    if rabbit.carries_carrots():
        rabbit.drop_carrot
    if rabbit.front_is_clear():
        rabbit.move()
    else:
        rabbit.turn_left()
        if rabbit.front_is_clear():
            rabbit.move()
            rabbit.turn_left()
            row_num += 1
        else:
            return False
    return True

def go_left():
    global row_num
    if rabbit.front_is_clear():
        rabbit.move()
    else:
        turn_right()
        if rabbit.front_is_clear():
            rabbit.move()
            turn_right()
            row_num += 1
        else:
            return False
    return True


row_num = 1

while rabbit.on_carrot():
    rabbit.pick_carrot()

while True:
    if (row_num % 2) == 1:
        if go_right_and_drop(): pass
        else: break
    else:
        if go_left(): pass
        else: break
