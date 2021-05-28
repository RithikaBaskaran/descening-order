from collections import OrderedDict
str1=input("enter a string= ")
def remove_duplicate(str1):
    return"".join(OrderedDict.fromkeys(str1))
str2=remove_duplicate(str1)
x=len(str2)
cnt=[0]*x
cnt1=[0]*x
str3=str2
str4=[]*x
i=0
for s in str2:
    cnt[i]=str1.count(s)
    i+=1
for k in range(0,x):
    str3=str2
    max =cnt[k]
    for j in range(k+1,x):
        if cnt[j]>max:
            k
            temp=cnt[k]
            cnt[k]=cnt[j]
            cnt[j]=temp
            max=cnt[k]
            
            temp1=str2[k]
            temp2=str2[j]
            str2=str2.replace(str2[k],temp2)
            str3=str2[k+1:]
            str3=str3.replace(str2[j],temp1)
            str3=str2[:k+1]+str3
            str2=str3
    print("Count of ",str3[k]," : ",cnt[k] ) 

