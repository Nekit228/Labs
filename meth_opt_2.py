import numpy as np
import numpy.linalg as ln
import scipy as sp
import scipy.optimize

# Objective function
def f(x):
    return(x[0]**2 - x[0]*x[1] + x[1]**2 + x[0] - 2*x[1])

# Derivative
def f1(x):
    return np.array([2*x[0] - x[1] + 1, -x[0] + 2*x[1] - 2])

def bfgs_method(f, fprime, x0, maxiter=None, epsi=10e-3):
    if maxiter is None:
        maxiter = len(x0) * 200

    k = 0
    gfk = fprime(x0)
    N = len(x0)
    
    I = np.eye(N, dtype=int)
    Hk = I
    xk = x0
   
    while ln.norm(gfk) > epsi and k < maxiter:
        pk = -np.dot(Hk, gfk)

        line_search = sp.optimize.line_search(f, f1, xk, pk)
        alpha_k = line_search[0]
        
        xkp1 = xk + alpha_k * pk
        sk = xkp1 - xk
        xk = xkp1
        
        gfkp1 = fprime(xkp1)
        yk = gfkp1 - gfk
        gfk = gfkp1
        
        k += 1
        
        ro = 1.0 / (np.dot(yk, sk))
        A1 = I - ro * sk[:, np.newaxis] * yk[np.newaxis, :]
        A2 = I - ro * yk[:, np.newaxis] * sk[np.newaxis, :]
        Hk = np.dot(A1, np.dot(Hk, A2)) + (ro * sk[:, np.newaxis] *
                                                 sk[np.newaxis, :])
        
    return xk


result = bfgs_method(f, f1, np.array([0, 0]))

print('Метод сопряженных направлений')
print('X1, X2 = ', (result))
print('Func = ', f(result))
