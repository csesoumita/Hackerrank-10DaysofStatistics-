N=int(input())
li=list(map(int,input().split()))
li.sort()
print(li)
half=len((li))//2
a=[]
def median_value(a):
    length_half=int(len(a)/2)
    if len(a)%2==0:
        median=int((a[length_half]+a[length_half-1])/2)
        print(median)
    else:
        median=int((a[length_half]))
        print(median)   
if N%2==0:
    lower=li[:half]
    upper=li[half:]
    print(lower)
    print(upper)
    median_value(lower)
    print(int((li[half]+li[half]-1)/2))
    median_value(upper)
else:
    lower=li[:half]
    upper=li[half+1:]
    print(lower)
    print(upper)
    median_value(lower)
    print(li[half])
    median_value(upper)
