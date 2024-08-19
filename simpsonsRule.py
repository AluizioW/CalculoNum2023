from math import log
from math import exp

n = float(input("Numero de traezios: "))
x0 = float(input("x0 = "))
xf = float(input("xf = "))
h = (xf - x0) / n

def f(x):
  #y = 1 / (x)
  #y = (x**2 + 1 / x)
  #y = x*log(x)
  y = x**2 * log(x) + 1
  #y = exp(x**2)
  return(y)

x = x0
count = 0
area = 0

while count < n:
  b = f(x)
  B = f(x + h)
  area += h * (b + B) / 2
  print("b = {}".format(b))
  print("B = {}".format(B))
  print(area)
  count += 1
  x += h
