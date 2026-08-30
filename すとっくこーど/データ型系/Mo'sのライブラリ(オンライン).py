import math
def Xup_func(x,y,a) :
    return a+x+y+1
def Yup_func(x,y,a) :
    return a+x+y+1
class Mos_online :
    #通常のMo'sの方が速い局面はたくさんある
    def __init__(self,H,W,A,Xup_func,Yup_func) :
        #A...(0,0)の値
        #乗せるのはイミュータブルなものであること
        self.BH=math.isqrt(H)
        self.BW=math.isqrt(W)
        self.SH=1+(H-1)//self.BH
        self.SW=1+(W-1)//self.BW
        self.Arr=[[0 for k in range(self.SW)] for j in range(self.SH)]
        self.Arr[0][0]=A
        self.Xf=Xup_func
        self.Yf=Yup_func
        if H>=W :
            C=A
            for i in range(self.SH-1) :
                for j in range(self.BH) :
                    C=Xup_func(j+self.BH*i,0,C)
                self.Arr[i+1][0]=C
            for i in range(self.SH) :
                D=self.Arr[i][0]
                for j in range(self.SW-1) :
                    for k in range(self.BW) :
                        D=Yup_func(self.BH*i,j*self.BW+k,D)
                    self.Arr[i][j+1]=D
        else :
            C=A
            for i in range(self.SW-1) :
                for j in range(self.BW) :
                    C=Yup_func(0,j+self.BW*i,C)
                self.Arr[0][i+1]=C
            for i in range(self.SW) :
                D=self.Arr[0][i]
                for j in range(self.SH-1) :
                    for k in range(self.BH) :
                        D=Xup_func(j*self.BH+k,self.BW*i,D)
                    self.Arr[j+1][i]=D
    def query(self,X,Y) :
        Xf=self.Xf
        Yf=self.Yf
        C=self.Arr[X//self.BH][Y//self.BW]
        baseX=self.BH*(X//self.BH)
        baseY=self.BW*(Y//self.BW)
        for i in range(X%self.BH) :
            C=self.Xf(baseX+i,baseY,C)
        for i in range(Y%self.BW) :
            C=self.Yf(X,baseY+i,C)
        return C
A=0
H=99
W=100
mo=Mos_online(H,W,A,Xup_func,Yup_func)
print(mo.query(65,4))
