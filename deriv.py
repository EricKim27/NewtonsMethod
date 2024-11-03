import sympy as sp
from typing import Callable, List

def derivative(func: Callable[[float], float], x: float):
    h = sp.symbols('h')
    if not callable(func):
        func = sp.lambdify(sp.symbols('x'), func)
    return sp.limit((func(x + h) - func(x)) / h, h, 0)

def tanline(func: Callable[[float], float], x0: float):
    x = sp.symbols('x')
    if not callable(func):
        func = sp.lambdify(x, func)
    slope = derivative(func, x).subs(x, x0)
    y0 = func(x0)

    def _tan(x) -> float:
        return slope * (x - x0) + y0

    return _tan

def newton(func: Callable[[sp.Symbol], sp.Expr], tol: float = 1e-7) -> list[Callable[[float], float]]:
    a: float = 10.0
    tanlist = []
    x = sp.symbols('x')
    resint = 0

    for i in range(1, 1000):
        tanl = tanline(func, a)
        tanlist.append(tanl)
        tanl_expr = tanl(x)
        new_a = sp.solve(tanl_expr, x)[0]
        resint = round(new_a)
        if abs(new_a - a) < tol:
            break
        a = new_a
        resint = None
    
    print(f"The solve for x to equation(x) = 0 is: {resint}")
    return tanlist
