n=int(input("enter the no. of processer:"))
print("enter the processid,bursttime and priority:")
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        if l[i][2]>l[j][2]:
            l[i],l[j]=l[j],l[i]
ct=0
for i in range(n):
    ct+=l[i][1]
    l[i].append(ct)
tat,wt=0,0
print("Pid Bt Priority At Tat Wt")
for i in range(n):
    print(l[i][0]," ",l[i][1]," ",l[i][2]," ",0," ",l[i][3]," ",l[i][3]-l[i][1])
tat=0
wt=0
for i in range(n):
    tat+=l[i][3]
    wt+=l[i][3]-l[i][1]
print("avg tat:",tat/n)
print("avg wt:",wt/n)

'''
enter the no. of processer:5
enter the processid,bursttime and priority:
1 10 3
2 1 1 
3 2 4
4 1 5
5 5 2
Pid Bt Priority At Tat Wt
2   1   1   0   1   0
5   5   2   0   6   1
1   10   3   0   16   6
3   2   4   0   18   16
4   1   5   0   19   18
avg tat: 12.0
avg wt: 8.2
'''