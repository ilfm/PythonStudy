# Tuple은 리스트와 다르게 변경이나 추가 할수 없다.
# 하지만 속도는 빠르다 그래서 변경되지 않은 정보를 다룰 때 사용한다.

menu = ("돈가스","치즈까스")
print(menu[0])
print(menu[1])

# name = "김종국"
# age = 20
# hobby ="코딩"
# print(name, age, hobby)

(name, age, hobby) =("김종국", 20, "코딩")
print(name, age, hobby)
