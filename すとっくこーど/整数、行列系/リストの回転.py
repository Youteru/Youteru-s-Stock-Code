A=[[3*i+j for j in range(3)] for i in range (3)]

#上下反転
B=A[::-1]
#左右反転
C=list(zip(*list(zip(*A))[::-1]))
#転置
D=list(zip(*A))
#右90度回転
E=list(zip(*A[::-1]))
#左90度回転
F=list(zip(*A))[::-1]
#180度回転
G=list(zip(*list(zip(*A))[::-1]))[::-1]
print(F)
