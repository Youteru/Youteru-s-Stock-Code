N=int(input())
for b in range(2 ** (N)):
    bit = bin(b)[2:].zfill(N)
    B=list(map(int,bit()))
    print(B)
