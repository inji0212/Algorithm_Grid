S= int (input())
FivN=S//5
ThrN=S//3
Fal=-1
Chk=S


while 1:
    Chk= S - FivN *5
    if (Chk%3)==0:

        ThrN=Chk//3
        print(FivN+ThrN)
        break
    FivN-=1
    if FivN==0:
        break

    ## 4로 넣으면 -값되서 다시 더해짐
       
    
  
if FivN==0 :
    if (S%3)==0:
        ThrN=S//3
        print(ThrN)
    else :
        print(Fal)
     
      
        

            