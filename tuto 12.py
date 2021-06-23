# setes in python sets can return unique valeu
s = set () #blanck set
print(type(s))
s_from_liss = set([1,2,3,4])
print(s_from_liss)
print(type(s_from_liss))

s.add(1)
s.add(3)
print(s)
s1 = s.union({1,2,3,4,5})
s2 = s.intersection({1,2,3})
s3 = {2,4}
print(s.isdisjoint(s3))
print(s1,s2)

