#Replace all ______ with rjust, ljust or center. 
from itertools import permutations

string = "HACK"

strings = list(permutations(string,2))
result = []
for s in strings:
	result.append(''.join(s))

for ss in sorted(result):
	print(ss)
