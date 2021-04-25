#############################################################
#                                                           #
# Problem Statement : https://projecteuler.net/problem=012  #
#                                                           #
# ###########################################################



def countFactors(n):
    c=0 
    upper=int(n**0.5)+1
    for i in range(1,upper):
        if n%i==0:
            if n//i==i:
                c+=1
            else:
                c+=2
    return c


def find():
    n=1
    c=2
    ans=n
    while True:
        factors=countFactors(n)
        print(n,factors)
        n=n+c
        c=c+1
        if factors>500:
            ans=n
            print("FOUND")
            break
find()



