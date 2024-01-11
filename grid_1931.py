n = int(input())
listA = []
for _ in range(n): # 리스트A 선언
    listA.append(list(map(int, list(input().split()))))

# 0번쨰와 1번쨰 두개 모두 순서대로 재배열
listA.sort(key=lambda x:x[0])
listA.sort(key=lambda x:x[1])
start=0
end=0
count=0
#     2번째 숫자를   chk ,chki+1값보다 작을 떄 chk까지 작은수 없으면 +1후 다음 시작 회차 chk
for j in range (0,n-1):
 
  if end<= listA[j][0] and listA[j][1]<= listA[j+1][1]:
    end= listA[j][1]
    count+=1

if end<= listA[n-1][0] :
    count+=1

print(count)

