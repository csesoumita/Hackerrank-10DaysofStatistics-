N=int(input())
li=list(map(int,input().split()))
fr=list(map(int,input().split()))
li_freq=[]

for i,j in zip(li,fr):
       li_freq=li_freq+([i]*j)
li_freq.sort()
print(li_freq)
half=len((li_freq))//2
a=[]
def median_value(a):
    length_half=int(len(a)/2)
    if len(a)%2==0:
        median=(a[length_half]+a[length_half-1])/2
    else:
        median=(a[length_half])
    return median
if N%2==0:
    lower=li_freq[:half]
    upper=li_freq[half:]
    #print(lower)
    #print(upper)
    Q1=median_value(lower)
    #print(int((li_freq[half]+(li_freq[half]-1))/2))
    Q3=median_value(upper)
    IQR=Q3-Q1
    print(float(IQR))
else:
    lower=li_freq[:half]
    upper=li_freq[half+1:]
    #print(lower)
    #print(upper)
    Q1=median_value(lower)
    #print(li_freq[half])
    Q3=median_value(upper)
    IQR=Q3-Q1
    print(float(IQR))
