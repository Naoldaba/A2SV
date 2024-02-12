from collections import defaultdict
 
test=int(input())
for i in range(test):
    n=int(input())
    List=list(map(int,list(input())))
    prefix=0
    Map=defaultdict(int)
    Map[0]=1
    ans=0
    for i in range(len(List)):
        prefix+=List[i]
        if prefix-(i+1) in Map:
            ans+=Map[prefix-(i+1)]
        Map[prefix-(i+1)]+=1
 
    print(ans)