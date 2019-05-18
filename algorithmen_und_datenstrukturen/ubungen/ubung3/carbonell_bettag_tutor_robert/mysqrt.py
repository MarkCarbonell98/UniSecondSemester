def mysqrt(x):
    if (x<0):
          raise ValueError("sqrt of negative number")
    y = x / 2
    while y**2!=x:
          y =(y + x/y) / 2
    return y
    
print(mysqrt(1))

