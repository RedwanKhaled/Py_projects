__author__ = 'khaled'
# Thanks to Mimino for help...


def S(n):
    return n*(n+1)/2

def S2(n):
    return n*(n+1)*(2*n+1)/6


T = int(raw_input())

while T>0:

    n = long(raw_input())

    n = (n+1)/2
    MOD = 10**9 + 7

    X = 2*S(n-1)%MOD

    diag_up_right = S2(2*n)%MOD - 4*S2(n)%MOD    # Formula is on Notes for series sum
    diag_up_left = diag_up_right - X
    diag_down_left = diag_up_left - X
    diag_down_right = diag_down_left - X

    total = (diag_up_right + diag_up_left + diag_down_left + diag_down_right)%MOD
    print total - 3


    T-=1

