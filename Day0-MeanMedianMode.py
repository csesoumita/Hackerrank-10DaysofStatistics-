
# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
li=list(map(int,input().split()))
li.sort()
sum_n=0
#Mean
for k in range(0,N):
    sum_n=sum_n+li[k]
mean_n=(sum_n/N)
print(mean_n)
#Median
if N%2==0:
    l_half=int(len(li)/2)
    median1=li[l_half]
    median2=li[(l_half-1)]
    median=(median1+median2)/2
    print(median)
else:
    print(li[(len(li)/2)])
#Mode
high_fre=0
hig_fre_ele=0
for j in range(0,len(li)):
    counter=li.count(li[j])
    if (counter>high_fre):
        high_fre=counter
        high_fre_ele=li[j]
mode=high_fre_ele
print(mode)