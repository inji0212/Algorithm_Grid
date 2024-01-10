S = int (input())
N = 0
Count = 1
SumNum = 0

while SumNum < S :
  if Count > S - SumNum :
      break
  N += 1
  SumNum += Count 
  Count += 1
#print(n,Count)
print(N)

'''s= int(input())
val=1
ans=0
while s > 0 :
    if val > s:
        break
    s-=val
    val+=1
    ans +=1
print(ans)'''
S = int (input())
N = 0
Count = 1
N_sum = 0

while N_sum < S :
   if Count > S - N_sum :
     break
     N += 1
     N_sum += Count 
     Count += 1
     #print(N,Count)
print(N)
