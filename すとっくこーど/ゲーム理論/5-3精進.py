n=int(input())
MAP=[False for i in range(5001*5001)]
A=[]
B=[]
C=[]
for i in range(n) :
    A.append(list(map(int,input().split())))
    MAP[A[-1][0]+5001*A[-1][1]]=True
    if (A[-1][0]+A[-1][1])%2==0 :
        B.append([A[-1][0],A[-1][1]])
    if (A[-1][0]+A[-1][1])%2==0 :
        C.append([A[-1][0],A[-1][1]])
ans=0
for i in range(len(B)) :
    for j in range(i) :
        x,y,X,Y=B[i][0],B[i][1],B[j][0],B[j][1]
        if x+X+y+Y-2*max([x,X,y,Y])>-1 and x+X+y+Y-2*min([x,X,y,Y])<10001 :
            if MAP[int(0.5*(x+X+y-Y)+2500.5*(-x+X+y+Y))] and MAP[int(0.5*(x+X-y+Y)+2500.5*(x-X+y+Y))] :
                ans=max([ans,((x-X)**2+(y-Y)**2)/2])
for i in range(len(C)) :
    for j in range(i) :
        x,y,X,Y=C[i][0],C[i][1],C[j][0],C[j][1]
        if x+X+y+Y-2*max([x,X,y,Y])>-1 and x+X+y+Y-2*min([x,X,y,Y])<10001 :
            if MAP[int(0.5*(x+X+y-Y)+2500.5*(-x+X+y+Y))] and MAP[int(0.5*(x+X-y+Y)+2500.5*(x-X+y+Y))] :
                ans=max([ans,((x-X)**2+(y-Y)**2)/2])
print(int(ans))
