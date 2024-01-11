# i 번쨰 기름 값이 i+1보다  싸면 다음 장소까지 구매
# 보다 비싸면 필요 거리만큼만 구매
# k가 가장 작을 수 일 때 까지 k를 곱하고 그 다음엔 
N= int (input())
a= list(map(int,input().split()))
b= list(map(int,input().split()))
Sum=0

for i in range (0,N-1):
  if b[i] < b[i+1] :
    b[i+1] = b[i]
  

for i in range (0,N-1):
  Sum+= a[i] * b[i]

print (Sum)