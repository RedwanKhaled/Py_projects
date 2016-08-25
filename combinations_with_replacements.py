'''
    https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
    Aug 23,2016
'''


from itertools import combinations_with_replacement


st = raw_input().split(' ')

k = int(st[1])
st = list(st[0])
st.sort()

comb = list(combinations_with_replacement(st,k))

for i in comb:
    print ''.join(map(str,i))
