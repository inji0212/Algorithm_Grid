# 백준  grid 1789번
# 수들의 합

S = int (input())
N = 0
Count = 1
SumNum = 0

#이전의 합에 현재 가장 작은 수의 합보다 S가 작을 때
#sum + 어떤 수 = S가 될 수 있다. 
#즉 1~n까지 의 합의 max
#SumNum= n(n+1)/2
while SumNum < S :
  if Count > S - SumNum :
      break
  N += 1
  SumNum += Count 
  Count += 1
#print(n,Count)
print(N)

