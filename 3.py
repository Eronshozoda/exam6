def fibonach(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fibonach(n-1)+fibonach(n-2)

a=int(input())
print(fibonach(a))    

