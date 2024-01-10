## 문자열로 입력받은뒤 
## 열 재배치
## 문제풀이는 작은 순서대로 재배치 후 총합

N= int (input())
a= list(map(int,input().split()))
a.sort()
T=0
Sum=0
for i in range(N):
    T= T+a[i]
    Sum+=T
   
print(Sum)