# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시요.

# 조건1: 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 :15분)
# [ ] 2번째 손님 (소요시간 :50분)
# [0] 3번째 손님 (소요시간 :5분)
# ...
# [ ] 50번째 손님 (소요시간 :16분)

# 총 탑승 승객 : 2분

#  내 풀이 ------------------------------------------------------------------------------------
"""
from random import *
index = 0   # 반복문 변수
count = 0   # 총탑승승객
customer =[]
while index != 50:
    customer.append(randrange(5,51))
    # 매칭 성공 경우
    if customer[index]>=5 and customer[index]<=15:
        print("[o] {0}번째 손님 (소요시간 : {1})".format(index,customer[index]))
        count+=1
    else:   # 매칭 실패 경우
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(index,customer[index]))
    index += 1
    

print("총 탑승 승객 : ",count)

"""
#  강시님 풀이 ------------------------------------------------------------------------------------
# random 클래스 import
from random import *

# 변수 선언
cnt = 0     # 총탑승객 수

for i in range(1,51): 
    time = randrange(1,51)
    if(5 <= time <= 15):
         print("[o] {0}번째 손님 (소요시간 : {1})".format(i,time))
         cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i,time))

print("총 탑승 승객 : ", cnt)
    


