# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)
# {1, 2, 3}

java = {"유재석", "김태호","하하"}
python = set(["유재석","박명수"])

# 교집합(java와 python 을 모두 할수 있는 개발자)
print(java & python)
print(java.intersection(python))
# {'유재석'}
# {'유재석'}

# 합집합 (java 할수 있거나 python 할수 있는 개발자)
print(java | python)
print(java.union(python))
"""
{'김태호', '하하', '박명수', '유재석'}
{'김태호', '하하', '박명수', '유재석'}
"""

# 차집합(java는 할수 있찌만 python는 하지 못하는 개발자)
print(java - python)
print(java.difference(python))
"""
{'하하', '김태호'}
{'하하', '김태호'}
"""

# python 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)
# {'김태호', '박명수', '유재석'}

# java를 까먹었어요 
java.remove("김태호")
print(java)
# {'하하', '유재석'}