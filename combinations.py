'''
    Problem Link: https://www.hackerrank.com/challenges/itertools-combinations
    Date: Aug 24,2016 

'''
from itertools import combinations

st = raw_input().split(' ')

N = int(st[1])
st = list(st[0])
st.sort()
st = ''.join(st)

comb = []
for i in range(1,N+1):
    a = list(combinations(st,i))
    for j in a:
        print(''.join(map(str,j)))