#############################################################
#                                                           #
# Problem Statement : https://projecteuler.net/problem=007  #
#                                                           #
# ###########################################################

def seive(n):
    prime=[True for i in range(n+1)]
    p=2
    while (p*p <=n):
        for i in range(p*2,n+1,p):
            prime[i]=False
        p+=1
    
    prime[0]=prime[1]=False

    primes=[int(i) for i in range(len(prime)) if prime[i]==True]
    return primes


primes=seive(200000)
print(len(primes))
print(primes[10001-1])