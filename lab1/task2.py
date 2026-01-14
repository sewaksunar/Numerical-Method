import numpy as np
import pandas as pd

eq = input("Enter the equation in terms of x using python syntax: ")

def f(x):
    return eval(eq, {"__builtins__": {}}, {"x": x, "np": np})

# validate equation
try:
    f(1)
except Exception as e:
    print("Invalid equation:", e)
    exit()

a = float(input("Enter lower initial guess: "))
b = float(input("Enter upper initial guess: "))

if f(a) * f(b) > 0:
    print(f"No root lies between {a} and {b}.")
    exit()

e = float(input("Enter tolerable error: "))
N = int(input("Enter max no of iterations: "))

B = []
i = 1

while i <= N:
    c = (a + b) / 2

    B.append([i, a, b, c, f(a), f(b), f(c), abs(b - a)])

    if abs(f(c)) < e:
        print("Converged: f(c) close to zero")
        break

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    if abs(b - a) < e:
        print("Converged: interval width small enough in {i} iteraation")
        break
    i += 1

columns = ["No. of iterations", "a", "b", "c", "f(a)", "f(b)", "f(c)", "Error"]
df = pd.DataFrame(B, columns=columns)
print(df.to_string(index=False))

