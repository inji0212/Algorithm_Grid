#500,100,50,10
#n원 최소 갯수

n= int (input())
coin=[500,100,50,10]
count =0
for i in coin :
    if n>= i:
        count+=n//i
        n= n%i

print(count)


coin.sort(reverse=True)