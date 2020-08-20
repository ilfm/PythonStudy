# 한줄 for 문

# 출석번호가 1,2,3,4 앞에 100을 붙이기로함 -> 101 , 102, 103, 104
# 예제 1
# students = [1,2,3,4,]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 예제 2 
# students = ["아이언맨","토르","그루트"]
# print(students)
# students = [len(i) for i in students]
# print(students)

# 예제 3
students = ["iron man", "thor"]
print(students)
students = [i.upper() for i in students]
print(students)