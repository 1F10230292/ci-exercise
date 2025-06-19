def fact(n):
    if n<0:
        raise ValueError("n must be a non-nagative integer")
    result =1
    for i in range(1,n+1):
        result*=i
    return result


def gcd(a,b):
    if (a<0 or b<0):
        a = abs(a)
        b= abs(b)
    
    if(a==0 and b==0):
        return 0
    if(a==0 and b!=0):
        return b
    if(a!=0 and b==0):
        return a
    
        

    while((a%b)!=0):
        r= a%b
        a = b
        b = r
    ##r=0の時
    return b

