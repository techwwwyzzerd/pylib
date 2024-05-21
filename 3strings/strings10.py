S="Theatree"
T="UPcompany"

# for i in range (len(T)):
#     New_str=S+T[i]
# S[7]=New_str
# print(S)

S=S [:7]
for i in range (len(T)):
    S += T[i]
print(S)