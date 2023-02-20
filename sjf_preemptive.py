def findWaitingtime(processes,n,wt):
    rt=[0]*n
    for i in range(n):
        rt[i]=processes[i][1]
    complete=0
    t=0
    minm=999999999
    short=0
    check=False
    while(complete!+n):
        for j in range(n):
            if((processes[j][2]<t)and(rt[j]<minm)and rt[j]>0):
               minm=rt[j]
               short=j
               check=True
            if(check==False):
                t+=1
                continue
            rt[short]-=1
            minm=rt[short]
            if(minm=0):
                minm=999999999
            if(rt[short]==0):
                complete=1
                check=False
                fint=t+1
                wt[short]=(fint-proc[short][1]-proc[short][2])
                if(wt[short]<0):
                    wt[short]=0
                t+=1
def findTrunAroundTime(processes,n,wt,tat):
    for i in range(n):
        tat[i]=processes[i][1]+wt[i]
def findavgtime(process,n):
    wt=[0]*n
    tat=[0]*n
    findWaitingtime(processes,n,wt)
    findTrunAroundTime(processes,n,wt,tat)
    print("processes bursttime waitingtime","trunaroundtime")
    total_wt=0
    total_tat=0