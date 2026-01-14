import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame
"""
To find a real root of a non linear equation using Secant Method
"""
eqn = input("Enter the equation in terms of x using python syntax: ")

def f(x):
    try:
        return eval(eqn)
    except Exception as e:
        print("Syntax error:", e)
        return None

a, b = float(input("Enter two initial guesses a: ")), float(input("Enter two initial guesses b: "))

if f(a)*f(b) > 0:
    print(f"No roots lies between {a} and {b}")
else:
    e = float(input("Enter tolerance error: "))
    N = int(input("Enter maximum number of iterations: "))

    A = []
    B = []
    FA = []  # Store f(A) values
    i = 1

    while i <= N:
        if f(b) - f(a) == 0:
            print("Division by zero encountered in Secant formula.")
            break
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        A.append(c)
        FA.append(f(c))  # Store f(c) for plotting
        if abs(a-b) < e:
            break
        else:
            a = b
            b = c
        iteration_data = [i, a, b, c, f(a), f(b), f(c), abs(a-b)]
        B.append(iteration_data)
        i += 1

    if i > N:
        print(f"The method did not converge in {N} iterations")
    else:
        print(f"The root is approximately at: {c}")
        columns = ['Iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', '|a-b|']
        results_df = pd.DataFrame(B, columns=columns)
        print(results_df)

    # Plot 1: Function plot with grid and axis lines
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # First subplot: x vs f(x)
    x = np.linspace(min(A)-2, max(A)+2, 400)
    y = f(x)
    ax1.plot(x, y, label='f(x)', color='blue', linewidth=2)
    
    # Draw horizontal and vertical red lines
    ax1.axhline(0, color='red', linewidth=1.5, linestyle='-', label='y = 0')
    ax1.axvline(0, color='red', linewidth=1.5, linestyle='-', label='x = 0')
    
    # Mark x-intercept (final root)
    ax1.plot(c, 0, 'go', markersize=10, label=f'Root ≈ {c:.6f}', zorder=5)
    
    # Enable grid
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('f(x)', fontsize=12)
    ax1.set_title('Function Plot: x vs f(x)', fontsize=14, fontweight='bold')
    ax1.legend()
    
    # Second subplot: Iteration vs Root Approximations with scatter plot
    iterations = np.arange(1, len(A)+1)
    ax2.scatter(A, FA, color='orange', s=100, alpha=0.6, edgecolors='black', label='Root Approximations')
    ax2.plot(A, FA, color='purple', linewidth=1.5, alpha=0.5, linestyle='--')
    
    # Draw horizontal and vertical red lines
    ax2.axhline(0, color='red', linewidth=1.5, linestyle='-', label='f(A) = 0')
    ax2.axvline(c, color='green', linewidth=1.5, linestyle='--', label=f'Final Root: {c:.6f}')
    
    # Mark x-intercept on scatter plot
    ax2.plot(c, f(c), 'go', markersize=12, label='Final Root Point', zorder=5)
    
    # Enable grid
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.set_xlabel('A (Root Approximation)', fontsize=12)
    ax2.set_ylabel('f(A)', fontsize=12)
    ax2.set_title('Scatter Plot: A vs f(A)', fontsize=14, fontweight='bold')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Plot 3: Visualization of iteration data (convergence)
    fig2, ax3 = plt.subplots(figsize=(10, 6))
    x1 = np.arange(1, len(A)+1)
    ax3.plot(x1, A, marker='o', color='blue', linewidth=2, markersize=8, label='Approximate Root (c)')
    ax3.axhline(c, color='green', linewidth=1.5, linestyle='--', label=f'Final Root: {c:.6f}')
    
    # Enable grid
    ax3.grid(True, alpha=0.3, linestyle='--')
    ax3.set_xlabel('Iteration', fontsize=12)
    ax3.set_ylabel('Root Approximation (c)', fontsize=12)
    ax3.set_title('Convergence of Root Approximations', fontsize=14, fontweight='bold')
    ax3.legend()
    
    plt.tight_layout()
    plt.show()