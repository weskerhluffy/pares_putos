# !/usr/bin/py
'''
Created on 21/11/2016

@author: ernesto
https://www.hackerrank.com/challenges/pairs
'''
import logging
import heapq
import sys


nivel_log = logging.ERROR
# nivel_log = logging.DEBUG
logger_cagada = None

def crea_monton(numeros):
    for idx_num, nume in enumerate(numeros):
        num_ultimo = nume
        idx_act = idx_num
        logger_cagada.debug("anadiendo %s en id %u" % (num_ultimo, idx_act))
        while idx_act:
            num_act = numeros[(idx_act - 1) >> 1]
            logger_cagada.debug("num act %u contra num ult %u en %u" % (num_act, num_ultimo, (idx_act - 1) >> 1))
            if num_ultimo > num_act:
                numeros[idx_act] = num_act
            else:
                break
            idx_act = (idx_act - 1) >> 1
        assert numeros[idx_act] <= num_ultimo
        numeros[idx_act] = num_ultimo
        logger_cagada.debug("finalmente %u kedo en %u" % (num_ultimo, idx_act))
#         logger_cagada.debug("nums asta aora %s"%numeros)
        for idx_nume in range(idx_num + 1):
            num_act_tmp = numeros[idx_nume]
            idx_i = (idx_nume << 1) | 1
            idx_d = idx_i + 1
            if(idx_i < idx_num + 1):
                assert numeros[idx_i] < num_act_tmp
                if(idx_d < idx_num + 1):
                    assert numeros[idx_d] < num_act_tmp, "l ijo der %u act %u" % (numeros[idx_d], num_act_tmp)
    logger_cagada.debug("nada orig %s" % (numeros))


def monton_sort(numeros):
    tam_nume = len(numeros)
    crea_monton(numeros)
    for idx_nume in range(tam_nume):
        num_act = numeros[idx_nume]
        idx_i = (idx_nume << 1) | 1
        idx_d = idx_i + 1
        if(idx_i < tam_nume):
            assert numeros[idx_i] < num_act
            if(idx_d < tam_nume):
                assert numeros[idx_d] < num_act, "l ijo der %u act %u" % (numeros[idx_d], num_act)


    logger_cagada.debug("el tope %u" % numeros[0])
    for idx_num, nume in enumerate(numeros):
        limite_heap = tam_nume - idx_num - 1
        num_ultimo = numeros[limite_heap]
        idx_act = 0
        logger_cagada.debug("num u;t %s limite heap %u" % (num_ultimo, limite_heap))
        numeros[limite_heap] = numeros[0]
        logger_cagada.debug("ordenado %u en pos %u" % (numeros[0], limite_heap))
        assert not limite_heap or numeros[limite_heap] >= numeros[limite_heap - 1]
        while ((idx_act << 1) | 1) < limite_heap:
            idx_i = (idx_act << 1) | 1
            idx_d = idx_i + 1
            if(idx_i < limite_heap):
                idx_maior = idx_i
            if(idx_d < limite_heap) and numeros[idx_i] < numeros[idx_d]:
                    idx_maior = idx_d
            num_act = numeros[idx_maior]
                
            logger_cagada.debug("num act %u contra num ult %u" % (num_act, num_ultimo))
            if num_ultimo < num_act:
                numeros[idx_act] = num_act
            else:
                break
            idx_act = idx_maior
        logger_cagada.debug("asignando %u a pos %u" % (num_ultimo, idx_act))
        numeros[idx_act] = num_ultimo
        logger_cagada.debug("nums asta aora %s" % numeros)
    logger_cagada.debug("alelu %s" % (numeros))

    logger_cagada.debug("die monster die %s" % numeros)
    return numeros
# Head ends here
def pairs(a, k):
    idx_izq = 0
    idx_der = 0
    tam_a = 0
    answer = 0
    # a is the list of numbers and k is the difference value
#    a_ord = sorted(a)
    logger_cagada.debug("ve must %s" % a)
    a_ord = monton_sort(a)
    logger_cagada.debug("sven nat  %s" % a_ord)
    logger_cagada.debug("sven nat1 %s" % sorted(a))
    tam_a = len(a)
    assert len(a) == len(a_ord)
    assert a_ord == sorted(a)
    
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

