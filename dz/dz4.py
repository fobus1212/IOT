sek=int(input())  
minet=0 
hour=0  
sektik=0
for i in range(sek+1): 
    sektik+=1   
    if sektik==60:  
        minet+=1  
        sektik=0
    elif minet ==60 : 
        minet=0 
        hour+=1  

print(f'{hour} час(а/ов) и {minet} минут(а/ы)')