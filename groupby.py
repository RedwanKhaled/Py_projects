'''
    Problem Link: https://www.hackerrank.com/challenges/compress-the-string
    Date: Aug 24,2016

'''


from itertools import groupby

st = raw_input()

for k,c in groupby(st):
    print '('+str(len(list(c)))+", "+str(k)+')',
    