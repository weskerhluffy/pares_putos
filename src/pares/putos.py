# !/usr/bin/py
'''
Created on 21/11/2016

@author: ernesto
https://www.hackerrank.com/challenges/pairs
'''
import logging


nivel_log = logging.ERROR
nivel_log = logging.DEBUG
logger_cagada = None

# Head ends here
def pairs(a, k):
    idx_izq = 0
    idx_der = 0
    tam_a = 0
    answer = 0
    # a is the list of numbers and k is the difference value
    a_ord = sorted(a)
    tam_a = len(a)
    
    if(not tam_a):
        return 0
    
    while(idx_izq < tam_a):
        conteo_operando_izq = 0
        conteo_operando_der = 0
        conteo_parejas_pendejas = 0
        num_actual = a_ord[idx_izq]
        num_requerido = num_actual + k
        while(idx_der < tam_a):
            if(num_requerido <= a_ord[idx_der]):
                break
            idx_der += 1
        
        while(idx_izq < tam_a and a_ord[idx_izq] == num_actual):
            conteo_operando_izq += 1
            idx_izq += 1
        while(idx_der < tam_a and a_ord[idx_der] == num_requerido):
            conteo_operando_der += 1
            idx_der += 1
        
        conteo_parejas_pendejas = min([conteo_operando_izq, conteo_operando_der])
        
        answer += conteo_parejas_pendejas
    
    return answer

# Tail starts here
if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size = a[0]
    _k = a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b, _k))

