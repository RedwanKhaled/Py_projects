#
#https://www.hackerrank.com/contests/pythonist3/challenges/capitalize
#The problem was pretty straight forward
#Pretty much confused with Python 2 and Python 3
#raw_input() does not work with Python 3
#Learnt about join,capitalize,title functions
#

from string import *

st = raw_input()
st = st.split(' ')

for i in range(0,len(st)):
    
    if len(st[i])==0: continue		#have to take care of space
    st[i] = list(st[i])
    
    if ord(st[i][0])>=97 and ord(st[i][0])<=122:st[i][0] = chr(ord(st[i][0])-32)
	
    st[i] = "".join(st[i])

st = " ".join(st)

print (st)

