import numpy

# CH4_enuc = 13.497304462033398
CH4_enuc = numpy.load('CH4_enuc.npy')
s = numpy.load('s.npy') # S_μv
h = numpy.load('h.npy') # H_μv
eri = numpy.load('eri.npy') # (μv|σλ)

s_s = s.shape # get the shape of overlap matrix s
l, u = numpy.linalg.eigh(s)
s_l = numpy.zeros(s_s)
for i in range(s_s[0]):
    s_l[i,i] = 1.0 / l[i]**0.5 # use eigvalue to update diagonalization matrix
x_t = numpy.dot(numpy.dot(u, s_l), numpy.linalg.inv(u)) # X
x_a = numpy.matrix.getH(x_t) # X^T

p_d = numpy.zeros(s_s)

def calc_e0_rhf(density, h, f):
    h_f = h + f
    e0 = 0
    for u in range(s_s[0]):
        for v in range(s_s[0]):
            e0 += density[v,u] * h_f[u,v] # calculate every steps' energy
    e0 *= 0.5
    return e0

def calc_p_rhf(c):
    density = numpy.zeros(s_s)
    for u in range(s_s[0]):
        for v in range(s_s[0]):
            for x in range(10//2): # int(electrons/2) Num.  electron= 10
                density[u,v] += 2*c[u,x]*c[v,x] # update P with C and C*
    return density

MAX_ITERS = 10
G = numpy.zeros(s_s)

def get_G(density):
    for u in range(s_s[0]): # μ
        for v in range(s_s[0]): # v
            temp = 0
            for la in range(s_s[0]): # λ
                for sig in range(s_s[0]): # σ
                    temp += density[la][sig]*(eri[u][v][sig][la] - 0.5*eri[u][la][sig][v]) # -40.19863935369017, -40.19869049846915
                    # temp += density[la][sig]*(eri[u][v][la][sig] - 0.5*eri[u][sig][la][v]) # -40.19863935369027, -40.19869049846915
            G[u][v] = temp
    return G

for i in range(MAX_ITERS):
    g = get_G(p_d)
    f = h + g # F_μv = H_μv + G_μv
    f_p = x_a.dot(f.dot(x_t)) # F'=X^TFX
    _, c_p = numpy.linalg.eigh(f_p) # diag, obtain C'
    c_new = x_t.dot(c_p) # C = XC'
    p_d_new = calc_p_rhf(c_new) # update P
    E0 = calc_e0_rhf(p_d, h, f) # calculate E0
    p_d = p_d_new
    Etot = CH4_enuc + E0 # total energy
    print('{}\t{}'.format(i,Etot))
