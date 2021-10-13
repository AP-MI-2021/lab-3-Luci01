
def citire():
    '''
    Functie care citeste o lista
    :return: O lista de numere intregi
    '''
    lista = []
    dimensiune = int(input("Dimensiune lista: "))
    while dimensiune:
        element = int(input())
        lista.append(element)
        dimensiune = dimensiune - 1
    return lista

def prim(nr):
    '''
    Functie care verifica daca un numar este prim
    :param nr: int
    :return: bool, true daca este prim, false altfel
    '''
    if nr<2:
        return False
    if nr == 2:
        return True
    if (nr%2==0) & (nr!=2):
        return False
    i=3
    while i*i<=nr:
        if nr%i==0:
            return False
        i+=2
    return True

def test_prim():
    '''
    Functie care testeaza functia prim
    :return:
    '''
    assert(prim(2) == True)
    assert(prim(3) == True)
    assert(prim(4) == False)
    assert(prim(175) == False)
    assert(prim(666013) == True)

def get_longest_all_primes(lst):
    '''
    Functie care determina cea mai lunga subsecventa in care toate numerele sunt prime
    :param lst:
    :return:
    '''
    lmax = 0
    lactual = 0
    secv_max = []
    secv_act = []
    for el in lst:
        if(prim(el)):
            lactual = lactual + 1
            secv_act.append(el)
        else:
            if(lactual > lmax):
                lmax = lactual
                secv_max = secv_act
            lactual = 0
            secv_act = []
    if(lactual > lmax):
        lmax = lactual
        secv_max = secv_act
    return secv_max

def test_get_longest_all_primes():
    '''
    Functie care testeaza functia get_longest_all_primes
    '''
    assert (get_longest_all_primes([1,5,7,12,7,3,5,19,15,2]) == [7,3,5,19])
    assert (get_longest_all_primes([1,5,7,12,7,3,5,19]) == [7,3,5,19])
    assert (get_longest_all_primes([4,6,8,10,15,49]) == [])
    assert (get_longest_all_primes([1,2,4,5,8,7]) == [2])

def nr_div(nr):
    '''
    Functie care numara divizorii unui numar 
    :param nr: int
    :return: Numarul divizorilor 
    '''
    if nr == 1:
        return 1
    n = 2
    for i in range (2 ,int(nr/2)+1) :
        if(nr % i == 0):
            n = n + 1
    return n

def test_nr_div():
    assert (nr_div(1) == 1)
    assert (nr_div(2) == 2)
    assert (nr_div(9) == 3)
    assert (nr_div(10) == 4)
    assert (nr_div(16) == 5)
    assert (nr_div(8) == 4)

def get_longest_same_div_count(lst):
    '''
    Functie care determina cea mai lunga subsecventa in care toate numerele au acelasi numar de divizori
    :param lst:
    :return: O lista de intregi care reprezinta cea mai lunga subsecventa in care toate numerele au acelasi numar de divizori
    '''
    lactual = 0
    lmax = 0
    secv_max = []
    secv_actuala = []
    nrdiv = 0

    lactual = 1
    nrdiv = nr_div(lst[0])
    secv_actuala = [lst[0]]
    for el in range (1,len(lst)):
       if(nr_div(lst[el]) == nrdiv):
            lactual = lactual + 1
            secv_actuala.append(lst[el])
       else:
           if(lactual > lmax):
                lmax = lactual
                secv_max = secv_actuala
           secv_actuala = [lst[el]]
           lactual = 1
           nrdiv = nr_div(lst[el])
    if(lactual > lmax):
        lmax = lactual
        secv_max = secv_actuala
    return secv_max

def test_get_longest_same_div_count():
    '''
    Functie care verifica functia get_longest_same_div_count
    '''
    assert (get_longest_same_div_count([6,8,10,9,25,2]) == [6,8,10])
    assert (get_longest_same_div_count([7,2,9,25]) == [7,2])
    assert (get_longest_same_div_count([1,2,4]) == [1] )
    assert (get_longest_same_div_count([6,9,25,49,10,8,2]) == [9,25,49])

def cifre_prime(nr):
    '''
    Functie care verifica daca numarul este format doar din cifre prime
    :return: Bool, true daca numarul este format doar din cifre prime, false in caz contrar
    '''
    if nr == 0:
        return False
    while nr:
        if nr % 10 == 1 or nr % 10 == 4 or nr % 10 == 6 or nr % 10 == 8 or nr % 10 == 9:
            return False
        nr = nr // 10
    return True

def  get_longest_prime_digits(lst):
    '''
    Functie care determina cea mai lunga subsecventa in care toate numerele sunt formate din cifre prime
    :param lst: 
    :return: Cea mai lunga subsecventa in care toate numerele sunt formate din cifre prime
    '''
    lmax = 0
    lactual = 0
    secv_max = []
    secv_act = []
    for el in lst:
        if (cifre_prime(el)):
            lactual = lactual + 1
            secv_act.append(el)
        else:
            if (lactual > lmax):
                lmax = lactual
                secv_max = secv_act
            lactual = 0
            secv_act = []
    if (lactual > lmax):
        lmax = lactual
        secv_max = secv_act
    return secv_max



def test_get_longest_prime_digits():
    '''
    Functie care testeaza functia get_longest_prime_digits
    '''
    assert(get_longest_prime_digits([2,5,6,7,8]) == [2,5])
    assert(get_longest_prime_digits([55,35,72,4,6]) == [55,35,72])
    assert(get_longest_prime_digits([4,6,10,13,54]) == [])
    assert(get_longest_prime_digits([27,8,72,35,90,84,5,7,5]) == [5,7,5])

def meniu():
    '''
    Functie care afiseaza meniul
    '''
    print("Meniu \n ")
    print("1.Citire date.")
    print("2.Determinare cea mai lunga subsecventa in care toate numerele sunt prime")
    print("3.Determinare cea mai lunga subsecventa in care toate numerele au acelasi numar de divizori")
    print("4.Determinare cea mai lunga subsecventa in care toate numerele sunt formate din cifre prime")
    print("5.Iesire")


def main():
    test_prim()
    test_get_longest_all_primes()
    test_nr_div()
    test_get_longest_same_div_count()
    test_get_longest_prime_digits()
    meniu()
    optiune = 0
    lst = []
    while optiune != 5 :
        optiune = int(input("Alegeti o optiune: "))
        if optiune == 1 :
            lst = citire()
        elif optiune == 2 :
            secv1 = get_longest_all_primes(lst)
            print (secv1)
        elif optiune == 3 :
            secv2 = get_longest_same_div_count(lst)
            print (secv2)
        elif optiune == 4 :
            secv3 = get_longest_prime_digits(lst)
            print (secv3)
        elif optiune == 5 :
            break

main()