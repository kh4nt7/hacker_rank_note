from itertools import combinations

a,n = input().split()

for j in range(int(n)):
    s = [''.join(i) for i in combinations(sorted(a),j+1)]
    print(*[i for i in sorted(s)],sep='\n')
