def findWaitingTime(processes,n,bt,wt,quantum):
    rem_bt=[0]*n
    for i in range(n):
        rem_bt[i]=bt[i]
    t=0
    while(1):
        done=True
        for i in range(n):
            if(rem_bt[i]>0):
                t+=quantum
                rem_bt[i]=quantum
            else:
                t=t+rem_bt[i]
                wt[i]=t_bt[i]
                rem_bt[i]=0
            if(done==true):
                break
def findTrunAroundTime(processses,n,bt,wt,tat):
    for i in range(n):
        tat[i]=bt[i]+wi[i]
def findavgTime(process,n,bt,quantum):
    wt=[0]*n
    tat=[0]*n
    findWaitingTime(processes,n,bt,wt,quantum)
    findTrunAroundTime(processses,n,bt,wt,tat)
    print("proceses bt wt tat")
    total_wt=0
    total_tat=0
    for i in ange(n):
        total_wt=total_wt+wt[i]
        total_tat=total_tat+tat[i]
        print(" ",i+1,"\t\t",bt[i],"\t\t",wt[i],"\t\t",tat[i])
        print("\n avg wt=%5f"%(total_wt/n))
        print("avg tat=%5f"%(total_tat/n))
if __name__=="__main__":
    proc=[1,2,3]
    n=3
    brust_time=[10,5,8]
    quantum=2
    findavgTime(proc,n,brust_time,quantum)