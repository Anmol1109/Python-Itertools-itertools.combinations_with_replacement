# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
a,b = input().split()
for i in combinations_with_replacement(sorted(a),int(b)):
    print("".join(i))
