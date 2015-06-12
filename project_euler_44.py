__author__ = 'khaled'


a = []

def generate():

    for i in range(1,10000):
        a.append(i*(3*i-1)/2)


def get_sol():

    for i in range(1,len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j] in a:
                #print "Hello",a[i],a[j]
                if (a[j] - a[i]) in a:
                    print a[i],a[j]
                    print

generate()
get_sol()


# this is a brute force solution..... Need to learn a good solution.....

#print a