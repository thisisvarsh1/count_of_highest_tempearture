import numpy as n
print("Welcome to my era!!")
x=int(input("how many days temperature u want me to calculate?: "))
tmp_list=[]
for i in range(x):
    y=int(input("enter day %d's temperature: "%(i+1)))
    tmp_list.append(y)
a=n.array(tmp_list)
avg=sum(a)/len(a)
print("average temperature is %d "%avg)
days_count=0
for i in a:
    if i > avg:
        days_count+=1

print("the number of days above average temperature is: %d"%days_count)



