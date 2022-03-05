def bisection(f, a, b, e=10**-4, N = 100):
  x_a = a
  x_b = b
  f_a = 
  f_b =
  
  if f(x_a)*f(x_b) >= 0:
    print("Use another guess range")
    return None
  
  for n in range (1,N):
    x_m = (x_a + x_b)/2
    print('|f(x_m)| = ',abs(f(x_m)))
    if abs(f(x_m)) < e:
      return (x_m)
    else:
      if f(x_a)*f(x_m) < 0:
        x_b = x_m
      elif f(x_b)*f(x_m) < 0:
        x_a = x_m
  return (x_m)
f = lambda x: x**3+x**2-3
a = 0.25
b = 1.75
x_root = bisection(f,a,b)
print(x_root)
