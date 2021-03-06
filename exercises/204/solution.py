# -*- coding: utf-8 -*-
"""
You'll expose a perfect_shuffle(deck) function, perfectly shuffling
the given iterable.
@author: CharlotteVDD
"""
import itertools


def perfect_shuffle(deck):
    pf = []
    n = len(deck)
    mid = int(n / 2)
    if n == 2:
        pf = [deck[0], deck[1]]
    elif n > 2:
        deck1 = list(itertools.islice(deck, mid))
        deck2 = list(itertools.islice(deck, mid, n))
        for i in range(mid):
            pf.append(deck1[i])
            pf.append(deck2[i])
        if n % 2 != 0:
            pf.append(deck2[mid])
    return(pf)
