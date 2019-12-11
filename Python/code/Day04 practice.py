'''
# 시작값, 끝값, 조건값(무조건 1) 입력 받아서
# 7의 배수만 출력(한줄로)
sta=int(input("시작 값 입력\t: "))
end=int(input("끝 값 입력\t: "))
grow=int(input("조건 값 입력\t: "))
for i in range(sta,end+1,grow):
    if i % 7 == 0:
        print(i,end=" ")

# 1~100까지 숫자 중 3의배수이면서 5의배수(=15의 배수) 전체의 합
sum = 0
for i in range(1,101,1):
    if i%3==0 and i%5==0 :
        sum += i
print(sum)

# 0 - 00000, 1 - 01234, 2 - 02468 ... 4까지 출력
for i in range(0,5,1):
    print(i,"-",end=" ")
    for j in range(0,5,1):
        print(j*i,end=" ")
    print()

# 1 ~ 25 한줄에 5개씩 출력 (2중for문 사용)
num=1
su=1
for i in range(0,6,1):
    num=i*5
    for k in range(su,num+1,1):
        print(k,end="\t")
    print()
    su=num+1
'''