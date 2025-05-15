N = int(input())
N2 = list(map(int, input().split()))
A = set(N2)
B = []
for c in range (N):
    B.append(c)
B1 = set(B)
print (len(A.intersection(B)))
