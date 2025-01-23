import numpy
from src.project1 import CH4, s, h, eri
# change molecule in src.project1
numpy.save('CH4_enuc.npy', CH4.enuc) # save enuc from molecule of project1
numpy.save('s.npy', s)
numpy.save('h.npy', h)
numpy.save('eri.npy', eri)

'''
Number  Elements  (No.)         X                Y               Z
     0      C       6     -0.0000000000     0.0000000000     0.0000000000
     1      H       1      1.1837716819    -1.1837716819    -1.1837716819
     2      H       1      1.1837716819     1.1837716819     1.1837716819
     3      H       1     -1.1837716819     1.1837716819    -1.1837716819
     4      H       1     -1.1837716819    -1.1837716819     1.1837716819
Nuclear energy= 13.497304462033398
Num.  electron= 10
Num.  basisset= 35
Num.  basshell= 18
Overlap  integrals from Python take 1.222588 sec.
One-body integrals from Python take 8.097328 sec.
Two-body integrals from Python take 73.318191 sec
'''