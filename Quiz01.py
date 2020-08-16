# Quiz ) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오
"""
 예시) http://naver.com
 규칙1 : http:// 부분은 제외 ==> naver.com
 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver.com
 규칙3 : 남은 글자 중 처음 세자리 +   글자 개수 + 글자 내 'e' 개수 + "!" 로 구성
 
 예 ) 생성된 비밀먼호 : nav51!
"""
# url = "http://naver.com"
url = "http://daum.com"
# http:// 제거
url = url[7:]
    # 다른 방법
    # url = url.replace("http://","")

# e 글자 개수 찾기
eCount = url.count("e")

# 처음 만나는 점(.) 이후 부분은 제외
# 1. "." 위치 찾기
point = url.find(".")
# 2. "." 이후 부분 제외시키기
#print(url[:point])
url = url[:point]
wCount = len(url)
# 3. 남은 처음 세자리
url = url[:3]


password = url + str(wCount) + str(eCount) + "!"
# !!! int 형 일때 str() 로 감싸주는것 주의하기
print("{0}의 패스워드는 {1}입니다." .format(url,password))
