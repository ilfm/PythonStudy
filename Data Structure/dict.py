# key value
# key의 값은 정수, 문자열 상관없다.
cabinet ={3:"유재석",100:"김태호"}

# 사전 데이터 가져오는 방법1
print(cabinet[3])
print(cabinet[100])

# 사전 데이터 가져오는 방법 2
print(cabinet.get(3))

# 사전에 대한 오류
# key 값이 없는 경우 [] 대괄호에 경우는 오류 발생
# print(cabinet[5])
# print("hi")
"""
raceback (most recent call last):
  File "c:/PythonStudy/dic.py", line 13, in <module>
    print(cabinet[5])
KeyError: 5
"""

#  get에 경우에는 None 값을 리턴한다.
print(cabinet.get(5))
print("hi")
"""
None
hi
"""

# None 처리하기
print(cabinet.get(5,"사용가능"))
print("hi")
"""
사용가능
hi
"""

# 
print(3 in cabinet) # True
print(5 in cabinet) # False


cabinet2 = {"A-3":"유재석","B-100":"김태호"}

# cabinet2 새로운 데이터 넣기
cabinet2["C-20"] = "조세호"
# "A-3" 기존에 있는 key에 새로운 데이터를 넣는경우(덮어쓰기 된다.)
cabinet2["A-3"] = "김종국"
print(cabinet2["A-3"]) # 김종국

# 데이터 삭제
print(cabinet2)
del cabinet2["A-3"]
print(cabinet2)
"""
{'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}
{'B-100': '김태호', 'C-20': '조세호'}
"""

# key 들만 출력
print(cabinet2.keys())
# dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet2.values())
# dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet2.items())
# dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 데이터 모두 제거
cabinet2.clear()
print(cabinet2)
# {}