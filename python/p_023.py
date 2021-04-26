#############################################################
#                                                           #
# Problem Statement : https://projecteuler.net/problem=023  #
#                                                           #
# ###########################################################


# O(sqrt(n)) algo to find sum of factors
def sumFactors(n):
    s=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if n//i == i:
                s+=i
            else:
                s+=n//i
                s+=i 
    return s

# range all abundant numbers less than 28123
def listAbundant():
    lst=[]
    for i in range(1,28123):
        if sumFactors(i) > i:
            lst.append(i)
    return lst

def isPossible(num,lst,lstSet):
    for i in lst:
        temp=num-i
        if temp in lstSet:
            return True
    return False

def sumNumbers(lst):
    s=0
    lstSet=set(lst)
    for i in range(1,28123+1):
        if not isPossible(i,lst,lstSet):
            s+=i
    return s


lst=listAbundant()
print(len(lst))
print(sumNumbers(lst))
