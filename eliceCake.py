# [출처] 실전편 ② 나를 먹어요 케이크 해답|작성자 엘리스코딩
def solver(input1, input2, input3):
    minimum = min([input1, input2, input3])
    check_list = []
    num = 0
    while len(check_list) <= minimum:
        possible_range = [num//input1, num//input2, num//input3]
        feasibility = False
        for i in range(0, possible_range[0] + 1):
            for j in range(0, possible_range[1] + 1):
                for k in range(0, possible_range[2] + 1):
                    if input1 * i + input2 * j + input3 * k == num:
                        check_list.append(num)
                        feasibility = True
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
        if feasibility == False:
            check_list = []
        num += 1
    answer = check_list[0] - 1
    return answer


def solver_DP(input1, input2, input3):
    minimum = min([input1, input2, input3])
    maximum = max([input1, input2, input3])
    memoization_table = [True]
    check_list = []

    for num in range(0, maximum+1):
        possible_range = [num//input1, num//input2, num//input3]
        memoization_table.append(False)
        for i in range(0, possible_range[0] + 1):
            for j in range(0, possible_range[1] + 1):
                for k in range(0, possible_range[2] + 1):
                    if input1 * i + input2 * j + input3 * k == num:
                        memoization_table[num] = True
                    # break
            else:
                continue
            break
        else:
            num += 1
            continue
            break

    while len(check_list) <= minimum:
        memoization_table.append(False)
        if memoization_table[num - input1] \
            or memoization_table[num - input2] \
            or memoization_table[num - input3]:
            memoization_table[num] = True
            check_list.append(num)
        else:
            memoization_table[num] = False
            check_list = []
        num += 1

    answer = check_list[0] - 1
    return answer

solution_B = solver(7, 11, 17)
print(solution_B)
solution = solver_DP(7, 11, 17)
print(solution)


# [퀴즈3] 하트여왕의 생일의 수학적 & 프로그래밍 풀이
for i in range(1, 32):
    b = i
    a = b-7
    c = b+7
    d = b-1
    if (a+b+c+d == 79):
        print(a)




