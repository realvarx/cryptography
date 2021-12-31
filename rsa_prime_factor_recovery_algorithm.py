from math import gcd, sqrt
import random

def isEven(z):
    return z%2 == 0

def result(y, n):
    p = gcd((y-1), n)
    q = int(n // p)
    return p, q

def coPrime(a, b):
    return gcd(a, b) == 1

def factors(c):
    factorsList = []
    for i in range(1, c+1):
        if c%i == 0:
            factorsList.append(i)
    return factorsList

def getED(n, phi):
    ed = 0
    relatevelyPrime = []
    candidatesList = []
    for i in range(1, 30):
        candidatesList.append(phi*i + 1)
    for candidate in candidatesList:
        factorsList = factors(candidate)
        for factor in factorsList:
            if coPrime(factor, phi):
                if factor != 1 and factor!= n:
                    relatevelyPrime.append(factor)
        if(len(relatevelyPrime) >= 2):
            # for p in relatevelyPrime:
            #     tempList = relatevelyPrime.pop(p)
            #     for t in tempList:
            #         if(p*t == )
            ed = candidate
            return ed
        else:
            factorsList.clear 

# Algoritmo definido en el APPENDIX C de este link
# https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Br1.pdf
def computePQ(n, ed):
    k = ed - 1
    if(isEven(k)):
        r = k
        t = 0

        while((isEven(r))):
            r = int(r // 2)
            t = t+1
        success = False

        for i in range(1, 101):
            g = random.randint(0, n)
            y = pow(g, r, n)

            if(y == 1 or y == (n-1)):
                continue
                
            else:
            
                for j in range(1, t):
                    x = pow(y, 2, n)

                    if(x == 1):
                        success = True
                        break

                    if(x == (n-1)):
                        continue

                    y=x
                    x = pow(y,2) % n

                    if(x == 1):
                        success = True
                        break
        if success:
            return result(y, n)
        else:
            print("Error")
    else:
        print("Error")

# Comprobación por factorización directa
def checkFactorizing(n, phi):

    # phi(n) = (p-1)*(q-1)*p*q -p-q+1
    # n = p*q
    # n = p(n+1-phi(n)-p) = -p^2 + (n+1-phi(n))*p
    # p^2 - (n+1-phi(n))p + n = 0

    p = int(((n+1-phi) - sqrt(abs(n + 1 -phi)**2 - 4*n))/2)
    q = int(((n+1-phi) + sqrt(abs(n + 1 -phi)**2 - 4*n))/2)
    return p, q

def main():
    n = 667
    phi = 616
    ed = getED(n, phi)

    p, q = n, n
    while(p == n or q == n):
        p, q = computePQ(n, ed)
    
    directP, directQ = checkFactorizing(n, phi)

    print("Los factores primos son : p = " + str(p) + " y q = " + str(q) + """
    \nSe ha utilizado el Prime-Factor Recovery Algorithm, el cual recupera los factores primos 
de un módulo a partir de los exponentes público(e) y privado(d).""")
    print("\nPara comprobar el resultado, por factorización directa obtenemos : p = " + 
    str(directP) + " y q = " + str(directQ))
    print("\n¿Son los factores obtenidos por ambos métodos iguales? : " +  
    str((p == directP or p == directQ) and (q == directQ or q == directP)))

    salir = input("\nPresiona enter para salir")

if __name__ == '__main__':
    main()