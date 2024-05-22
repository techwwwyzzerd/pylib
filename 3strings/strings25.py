l = ["Orcas", "Dolphins", "Whales", "are", "animals"]
word = l[4][3] + l[4][0] + l[4][3]*2 + l[4][0] + l[4][5:]
l[4]=word
S=" ".join(l)
print(S)