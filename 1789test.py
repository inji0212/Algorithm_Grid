'''##성공
S = int (input())
N = 1
while N*(N+1)/2 <=S:
    N+= 1
print(N-1)
'''
##성공
S = int (input())
N = 0
SumNum = 0
while SumNum <= S:
    N+= 1
    SumNum = N*(N+1)/2
print(N-1)

# 백준  grid 1789번
# 수들의 합
'''
S= int (input())
N = 0
Count = 1

#k까지의 숫자들중 가장 작은 숫자들끼리 더해야 n이 최대가 됨(1+2+3+...)
#(k-1까지 모든 숫자들의 합) + 어떤 수 = S가 될 수 있다. 
# 1~ n까지의 숫자 합이 아니라 1~n-1까지의 숫자 합 + a= s가 되서 최대 갯수는 n이다. 

#SumNum= n(n+1)/2

while 1:
    SumNum = N*(N+1)/2
    if SumNum + (N+1) >= S:
        break
    N+= 1
print(N)
'''