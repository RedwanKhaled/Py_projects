'''
    https://www.hackerrank.com/challenges/itertools-permutations
    Aug 22,2016

'''



from itertools import permutations

st = raw_input().split(' ')
#print st
k = int(st[1])
st = list(st[0])
st.sort()
#print st
P = list(permutations(st,k))

for i in P:
    print(''.join(map(str,i)))


