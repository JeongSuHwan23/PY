#2023-07-17

#부호바꾸기
n = int(input())
print(-n) #변수 앞에 '-'를 붙이면 부호가 반대인 값이 된다

#다음 문자 출력
c = ord(input()) #문자를 정수 값으로 입력 받는다
print(chr(c+1)) #정수에 1을 더한 값을 문자로 바꿔서 출력한다

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
print(w*int(n)) #(문자) * (정수)를 하면 정수만큼 문자를 출력한다

#거듭제곱 계산
a, b = input().split()
c = int(a)**int(b) # a**b = a를 b번 제곱한다
print(c)

#몫 계산
a, b = input().split()
print(int(a)//int(b)) #'//'는 몫이 정수형(int)으로 나온다

#나머지 계산
a, b = input().split()
print(int(a)%int(b))

#자동 계산
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
c = float(a)/float(b) #'/'는 몫이 실수형(float)으로 나온다
print(format(c, ".2f"))

#합, 평균 계산
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = a+b+c
avg = float(a+b+c)/3
print(sum, format(avg, ".2f"))