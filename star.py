# for반목문을 이용하여 원하는 값만큼 특정값을 출력하기
for x in range(1,10) :
    print(f"{x}번 별 *")

# for 반목문을 이용하여 가로로 원하는 값을 출력하기

for x in range(5) :
    print("*", end="")

# end = '[구분자]'는 print함수로 문구를 출력하고, 마지막에 \n이 아닌 다른 값으로 설정할 수 있습니다.
print("hello", end=' ')
print("world")

# sep 전달인자를 사용하면, print함수 내에 여러 문구열을 표시할 때, 그 사이에 출력할 구분자를 표시할 수 있습니다.
print("010","1234","5678", sep='-')

# 문제 1번
# ****
# ****
# ****
# ****

# print("****")
# print("****")
# print("****")
# print("****")

for x in range(5) :
    print("*" * 5)

# 문제 2번
# *
# **
# ***
# ****
# *****

for x in range(5) :
    print("*" * (x + 1))

num = int(input("숫자를 입력해주세요 : "))
for x in range(num):
    print("*" * (x + 1))