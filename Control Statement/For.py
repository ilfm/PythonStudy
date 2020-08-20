# for문

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 :{0}".format(waiting_no))

# 예제 1
for waiting_no in range(1,6):
    print("대기번호 :{0}".format(waiting_no))

# 예제 2
starbucks = ["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))