def poly_diff(p):
    deg_p = len(p) - 1
    if deg_p == 0:
        return [0]
    else:
        return [k*p[k] for k in range(1,deg_p+1)]
    
def poly_eval(p,a):
    """Given a list representing the coefficients of a polynomial in increasing order and a, return p(a)"""
    
    cumsum = 0
    
    for n,t in zip(p, range(len(p))):
        
        r = n * a ** t
        cumsum = r + cumsum
        
    return cumsum