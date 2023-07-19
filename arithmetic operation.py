#2023-07-17

#부호바꾸기
n = int(input())
print(-n) #변수 앞에 '-'를 붙이면 부호가 반대인 값이 된다

#다음 문자 출력
c = ord(input())
print(chr(c+1))

#차 계산
a, b = input().split()
c = int(a) - int(b)
print(c)

#곱 계산
a, b = input().split()
c = float(a) * float(b)
print(c)

#단어 여러 번 출력
w, n = input().split()
print(w*int(n))

#거듭제곱 계산
a, b = input().split()
c = int(a)**int(b)
print(c)

#몫 계산
a, b = input().split()
print(int(a)//int(b))

#나머지 계산
a, b = input().split()
print(int(a)%int(b))

#소수점 이하 자리 변환
n = float(input())
print(format(n, ".2f"))

#자동 계산
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
c = float(a)/float(b)
print(format(c, ".2f"))

#합, 평균 계산
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = a+b+c
avg = float(a+b+c)/3
print(sum, format(avg, ".2f"))