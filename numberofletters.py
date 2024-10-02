name="HAHAHANANJODYSBBBHDODODOOOOOOOOOKSKSSSSSYYYYYY"
dict={}
for i in name:
    count=name.count(i)
    dict[i]=count
sorted = list(dict.values())
sorted.sort(reverse=True)
print(dict)
print(sorted)
topthree = sorted[:3]
print(topthree)
x=[]
count=0
flag=False
for i in topthree:
    x.clear()
    for j in dict:
        if dict[j]==i:
            x.append(j)
    length=len(x)
    if length==1:
        print(x[0])
        count+=1
        if count==3:
           flag=True
           break
    else:
        x.sort()
        for i in range(len(x)):
            print(x[i])
            count+=1
            if count==3:
                flag=True
                break
    if flag==True:
        break            


                