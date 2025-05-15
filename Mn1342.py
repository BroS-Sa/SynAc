A = int(input())
B = int(input())
A1 = []
for i in range (A):
    A1.append(i)
B1 = []
for i1 in range (B):
    B1.append(i1)
A2 = set (A1)
B2 = set (B1)
# Как я понял, тут  нужно объеднить, исходя из задния
print (len(A2.union(B2)))

# Или же просто вывести колчиство чисел как в первом варианте, так и во втором
print (A2)
print (B2)
# Возможно немного не понял задачку