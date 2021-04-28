import time

start = time.time()
####
end = time.time()
print(end - start)

x = [200,300]

def foo(x):
  print(x.pop(0))
foo(x)
print(x)
