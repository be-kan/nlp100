s1 = 'パトカー'
s2 = 'タクシー'

r = [s1+s2 for s1, s2 in zip(s1, s2)]
print("".join(s for s in r))
