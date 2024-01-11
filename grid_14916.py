#2원과 5원으로 거스름돈 최소 동전 갯수 
# 5원으로 짝수가 될 떄까지 --
n= int(input())

ans2=0
ans5=0
# 5로 나눴을 떄 0이 될때까지 2를 빼고 ans2+=1
result=0
while n>0:
  if n%5==0:
    ans5=n//5
    break
  else:
    n-=2
    ans2+=1
result=ans2+ans5
if n<0 :
  result=-1

print(result)
    
  

    