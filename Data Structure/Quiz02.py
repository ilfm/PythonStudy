'''
Quiz) 당신의 하굑에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해대슬 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됩니다.

조건 1 : 편의상 댓글 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정
조건 2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듈의 shuffle 과 sample 을 활용

( 출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

'''
"""
# 활용예제
from random import *
lst = [1,2,3,4,5]
# print(lst)
#--=> [1, 2, 3, 4, 5]
# shuffle(lst)
#--==> [3, 4, 5, 2, 1]
#--==> [3, 4, 1, 5, 2]
#print(lst)
#print(sample(lst,1))
"""
# random 클래스 import
from random import *
# 1. 참여자 20명을 리스트에 넣는다.
winner = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle 함수를 통해 섞는다.
shuffle(winner)
# sample 함수를 통해 하나를 뽑아 낸다.
# sample 함수은 list로 return 하기 때문에 .pop() 함수를 통해 요소를 뽑아낸다.
chickenList = sample(winner,1)
chicken = chickenList.pop()
idx = winner.index(chicken)
# 찾아낸 인덱스를 통해 치킨당첨자는 제거한다.
winner.remove(idx)
# 커피당첨자도 동일하게 한다.
coffee = sample(winner,3)

# 결과 출력
print("-- 당첨자 발표 ---")
print("치킨 당첨자",chicken)
print("커피 당첨자",coffee)
print("-- 축하드립니다. ---")


# 강사님 풀이 ------------------------------------------

users = range(1,21) # 1부터 20 까지 숫자를 생성
print(type(users)) #<class 'range'>
print(type(list(users))) # <class 'list'>
users = list(users)
# 섞기
shuffle(users)

winners = sample(users,4)
# 결과 출력
print("-- 당첨자 발표 ---")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하드립니다. ---")

