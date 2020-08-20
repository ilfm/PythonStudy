# continue & break
absent = [2,5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11) : # 1,2,3,4,5,6,7,8,9,10
    if student in absent:    # student가 absent 에 있다면
        continue             # continue 뒤에 문장은 skip하고 다시 반복한다
    elif student in no_book:
        print("오늘 수업 여기까지.{0}는 교무실로 와".format(student))
        break                # break 는 반복문을 끝낸다.
    print("{0}, 책을 읽어봐".format(student))