#!/usr/bin/env python

import numpy as np
from . import parameter
from .geometry import Geometry
from timeit import default_timer as timer


CH4 = Geometry('CH4',
               coor='''
                       C  -0.000000000000   0.000000000000   0.000000000000
                       H   1.183771681898  -1.183771681898  -1.183771681898
                       H   1.183771681898   1.183771681898   1.183771681898
                       H  -1.183771681898   1.183771681898  -1.183771681898
                       H  -1.183771681898  -1.183771681898   1.183771681898
                   ''',
                   charge=0,
                   multi=1,
                   basisname='cc-pvdz',
                   unit='bohr')

s = CH4._get_S()
#print(s)
h = CH4._get_HCore()
#print(h)
eri = CH4._get_ERI()
#print(eri)


