# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, M):
    # write your code in Python 2.7
    chocoAte = []
    ate = M % N
    while ate not in chocoAte:
        chocoAte.append(ate)
        ate = (ate + M) % N
    return len(chocoAte)

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

#suppose the position repeated is iM = jM and iM mod N = jM mod N -> iM + kN = jM
#prove that i is always 0 for the smallest j (j = num of choco ate)
#kN = jN = lcm(N,M)

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
        
def lcm(a,b):
    return a*b / gcd(a,b)

def solution(N, M):
    # write your code in Python 2.7
    if N >= M:
        return lcm(N,M)/M
    else:
        return lcm(M,N)/M
    