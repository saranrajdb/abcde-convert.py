def convert(n):
    d={'A':1,'B':2,'C':3,'D':4,'E':5}
    n=list(n)
    c=1 
    s=0
    while len(n):
        r=d[n.pop()]*c 
        s+=r
        c*=5
    return s 
n=input()
print(convert(n))