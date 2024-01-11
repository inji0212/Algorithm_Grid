n= int (input())
a=[]

for _ in range(n):
  a.append(int(input()))

a.sort()
d= len(a)
Result=[]
for i in range (0,n) :
  Result.append(a[i] * d)
  d-=1


print(max(Result))

  