# 

n,k=map(int,input().split())


count =0

coin = [0] * (n+1)#여기에 문제있을듯
for i in range (0,n) :
    coin[i]=int(input())
    #coin.append(int(input()))

coin.sort(reverse=True)
print(coin)

for i in coin :
    if k >= i :
        count += k//i
        k%=i
     

print(count)