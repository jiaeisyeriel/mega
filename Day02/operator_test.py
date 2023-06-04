# operator = 연산자
# 자기자신의(정의역과 공역이 동일한) 함수 ?

# 할당 연산자 =, -=, +=, *=
a = 1
a +=  1 #a에 재할당
a -= 1
a *= 1

# 수리 연산자 +, =, *, /(몫), %(나머지)
b = 10/3 #b의 몫, 즉 값은 3
b = 10%3 #b의 나머지, 즉 값은 1

# 비교 연산자 <, >, <=, >=, ==, !=
# 무조건 결과값은 True or False (Boolean Type)
x = 1
y = 2
# == 같니? # != 다르니?
print(x == y) # 값은 False (같니? - 아니)
print(x != y) # 값은 True (같니? - 응)
print(x > y)
print(x < y)

# 논리 연산자 및 우선순위 연산자 and, or, not, ()
bitcoin = 100
doge = 20
print(bitcoin > 0 and bitcoin < 200)
print((bitcoin > 0 and bitcoin < 200) or doge > 100)
# 앞의 값이 True, 뒤의 값이 False 그러나 논리 연산자가 or이기 때문에 값은 Ture !
print(not(bitcoin > 0)) # 답은 False
print(bitocin <= 0) # 답은 True

# in 연산자 [리스트]
x = ['mega', 'study', 'shinchon']
print('study' in x)


