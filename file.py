def fibb(n):
    fib_series=[0,1]

    if n<0:
        print("not valid")
    elif n==1:
        print (fib_series[0])
    elif n==2:
        print (fib_series[1])
    else:
        for i in range(2,n):
            fibnum=fib_series[-1]+fib_series[-2]
            fib_series.append(fibnum)
        print (fib_series[-1])  
    



num=int(input("Enter the number"))
fibb(num)




    