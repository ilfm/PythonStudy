# While문 
# while(조건) 조건이 true 일때 계속 반복한다.
# 예제 1 -----------------------------------------
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다.{1}번남았어요" .format(customer,index))
    index -= 1
    if index == 0:
        print("커피가 폐기 처분 되었습니다.")


# 예제 2 무한루프는 while True

# 예제 3 -----------------------------------------

customer = "토르"
person = "unknown"

while customer != person:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")