N=int(input())
sum_num=0
li_number=list(map(int,input().split()))
li_weight=list(map(int,input().split()))
for i in range(0,len(li_number)):
    sum_num=sum_num+((li_number[i]*li_weight[i])/sum(li_weight))
print(format(sum_num))