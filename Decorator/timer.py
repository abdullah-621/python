import time

def timer(func):
  def wrapper(*args):
    print(square.__name__)
    start = time.time()
    func(*args)
    print("Time taken by",func.__name__,time.time() - start, "secs")
  return wrapper

@timer
def square(a,b):
  time.sleep(1)
  print(a**b)

square(2,3)