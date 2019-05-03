from itertools import groupby

data = input()
groups = []
uniquekeys = []
data = data
t = []
for k, g in groupby(data):
    l = []
    l.extend((len(list(g)), int(k)))
    t.append(tuple(l))           # below is note from pydoc
    #groups.append(list(g))      # Store group iterator as a list
    #uniquekeys.append(k)
t = tuple(t)
print(*[i for i in t])
