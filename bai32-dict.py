d={"tung":1.65,"tuan":1.65,"linh":1.64}
print(d)
d["hung"]=1.90
print(d)
del d["hung"]
print(d)

print(len(d))
d.clear()
print(d)
print(type(d))