from deriv import *
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import sympy as sp
import numpy as np
import sys

x = sp.symbols('x')
while True:
    try:
        raw_eq = input("Enter equation: ")
        eq = sp.sympify(raw_eq)
        break
    except (sp.SymplifyError, SyntaxError) as e:
        print("Invalid Input")
    except Exception as e:
        print(f"An exception occured during execution: {e}")

try:        
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    tlist = newton(eq)

    #configure graph
    ax.set_ylim(-60, 60)
    ax.set_xlim(-20, 20)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)

    x_vals = np.linspace(-20, 20, 400)
    y_vals_eq = [eq.subs(sp.symbols('x'), x) for x in x_vals]
    ax.plot(x_vals, y_vals_eq, 'r-', lw=1)

    # Configure animation
    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        x_vals = np.linspace(-20, 20, 400)
        y_vals = [tlist[frame](x) for x in x_vals]
        line.set_data(x_vals, y_vals)
        return line,

    anim = ani.FuncAnimation(fig, update, frames=len(tlist), init_func=init, interval=100, blit=True)

    plt.show()
except Exception as e:
    print(f"An exception occured during execution: {e}")
