def findWaitingTime(processes,n,wt):
    wt[0]=0
    for i in range(1,n):
        wt[i]=process[i-1][1]+wt[i-1]
def findTrunAroundTime(processes,n,wt,tat):
    for i in range(n):
        tat[i]=processes[i][1]+wt[i]
def findavgTime(processes,n):
    wt=[0]*n
    tat=[0]*n
    findWaitingTime(processes,n)
    findTrunAroundTime(processes,n,wt,tat)
    total_wt=0
    total_tat=0
    for i in range(n):
        total_wt=total_wt+wt[i]
        total_tat=total_tat+tat[i]
        print(" ",processes[i][0],"\t\t",processes[i][1],"\t\t",wt[i],"\t\t",tat[i] )
    print("\n avg wt=%5f",(total_wt/n))
    print("avg tat=",(total_tat/n))
def priorityScheduling(proc,n):
    proc=sorted(proc,key=lambda proc:proc[2],reverse=True)
    print("order in which process gets executed")
    for i in proc:
        print(i[0],end=" ")
    findavgTime(proc,n)
if __name__ == "__main__":
    proc=[[1,0,1],[2,5,0],[3,8,1]]
    n=3
    priorityScheduling(proc,n)