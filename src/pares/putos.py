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
nivel_log = logging.DEBUG
logger_cagada = None


class PriorityQueue(object):
    """Priority queue based on heap, capable of inserting a new node with
    desired priority, updating the priority of an existing node and deleting
    an abitrary node while keeping invariant"""

    def __init__(self, heap=[]):
        """if 'heap' is not empty, make sure it's heapified"""

        heapq.heapify(heap)
        self.heap = heap
        self.entry_finder = dict({i[-1]: i for i in heap})
        logger_cagada.debug("el finder es %s" % self.entry_finder)
        self.REMOVED = sys.maxsize

    def insert(self, node, priority=0):
        """'entry_finder' bookkeeps all valid entries, which are bonded in
        'heap'. Changing an entry in either leads to changes in both."""

        if node in self.entry_finder:
            self.delete(node)
        entry = [priority, node]
        self.entry_finder[node] = entry
        heapq.heappush(self.heap, entry)
        logger_cagada.debug("el finde aora es %s" % self.entry_finder)
        logger_cagada.debug("el heap aora es %s" % self.heap)

    def delete(self, node):
        """Instead of breaking invariant by direct removal of an entry, mark
        the entry as "REMOVED" in 'heap' and remove it from 'entry_finder'.
        Logic in 'pop()' properly takes care of the deleted nodes."""

        logger_cagada.debug("norrando nodo %s" % node)
        entry = self.entry_finder.pop(node)
        entry[-1] = self.REMOVED
        return entry[0]

    def pop(self):
        """Any popped node marked by "REMOVED" does not return, the deleted
        nodes might be popped or still in heap, either case is fine."""

        while self.heap:
            logger_cagada.debug("elem de heap %s" % self.heap)
            priority, node = heapq.heappop(self.heap)
            if node is not self.REMOVED:
                del self.entry_finder[node]
                return priority, node
        raise KeyError('pop from an empty priority queue')

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

