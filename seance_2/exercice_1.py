import time

def chronometre(func):
    def wrapper(*args):
        debut = time.time()
        resultat = func(*args)
        fin = time.time()
        duration = fin - debut
        print(f"La fonction grosse_multiplication a pris (en secondes) {duration} {resultat}")
        return resultat
    return wrapper

@chronometre
def grosse_multiplication(multiplicateur):
    multiplicande = 1000000000000000*9999
    resultat = 0
    for i in range(1,multiplicateur):
        resultat += (multiplicande * multiplicateur *i)
    return  resultat
print(grosse_multiplication(56897*2))