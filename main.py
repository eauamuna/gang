import math
def f(x):
    return 7*x+2+0.7*math.cos(5*x)
def F(x,k,b):
    return 2*(f(x)-k*x-b)*(-x)
def G(x,k,b):
    return 2*(f(x)-k*x-b)*(-1)
def Fk(x):
    return 2*x*x
def Gb(x):
    return 2

k0=4
b0=1
e=0.001
n=40
a=0
b=4
x=[]
fx = []
y = []
error = []
h=abs((a+b)/n)
for i in range(n):
    x.append(x[i]+h)
    fx.append(f(x[i]))
    y.append(k0*x[i]+b0)
    error.append(fx[i]-y[i])

