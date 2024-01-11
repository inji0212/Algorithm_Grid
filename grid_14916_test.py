#2원과 5원으로 거스름돈 최소 동전 갯수 
# 5원으로 짝수가 될 떄까지 --
n= int(input())

i=n//5

# 5로 나눈 몫 - i을 뺸 뒤 2로 나눴을 떄 0이면
#다 실패시 짝수면 
# 전부 미포함 -1
while i>=0:
  ans2= (n-n*i)//2
  if (5*i+ans2*2 )==n :
    print(i+ans2)
    break
  i-=1

if i==0:
  if n%2==0:
    print(n//2)
  else:
    print(-1)


