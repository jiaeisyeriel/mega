# Data Types
# 프로그래밍 언어를 두 가지로 나눌 수 있음
# 1. 컴파일 언어
# - 데이터 타입을 미리 정함
# - dollar -> int(정수) dollar = 10 or String(문자) dollar = "10"
# - 하나라도 틀리면(컴파일 과정) 걸러짐

# 2. 인터프리터 언어 ex. Python, JavaScript
# - 데이터 타입을 그 때 정함
# - 일단 돌리고 봄.(오류를 프로그램을 실행하기 전까지 알 수 없음, 판매용으로 사용이 적음, 개인 연구 보조용으로 사용 多)

# 1. str (문자열)
a = "메가스터디"
print(type(a))
# 2. int (정수)
b = 123
print(type(b))
# 3. float (실수)
c = 123.123
print(type(c))
# 4. list (들어갈 수 있는 데이터 타입이 자유로움, but 양날의 검
d = [123, '4566', 12.35, [1,2,3]]
print(Type(d))
#5. dict (Key -> Value ex.인스타그램 해시태그 - 연관된 사진)
e = {'name':'joshua', 'age':21, 'language':['c', 'js', 'ts', 'java']}
print(type(e))
#6. set(집합)
f = {"apple", "banana", "orange", "apple"}
print(f)
