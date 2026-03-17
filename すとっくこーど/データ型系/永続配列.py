Q=int(input())
Tree=[(0,-1,[])]
P={}
P[0]=0
S=set()
#Aはページ0とする
for q in range(Q) :
    w=input()
    if w[0]=="A" :
        x=int(w.split()[-1])
        L=len(Tree)
        Tree[P[0]][2].append(L)
        Tree.append((P[0],x,[]))
        P[0]=L
    elif w[0]=="D" :
        P[0]=Tree[P[0]][0]
    elif w[0]=="S" :
        y=int(w.split()[-1])
        P[y]=P[0]
        S.add(y)
    elif w[0]=="L" :
        z=int(w.split()[-1])
        if z in S :
            P[0]=P[z]
        else :
            P[0]=0
    print(Tree[P[0]][1],end=" ")
print()
        
