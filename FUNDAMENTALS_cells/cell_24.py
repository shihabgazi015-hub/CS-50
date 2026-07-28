%%writefile timecount.py
# %%timeit
x = 4
u = 0
if x < u:
  print("x is greater than u")
elif x > u:
  print("x is less than u")
else:
  print("x and u are equal")