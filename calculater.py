import math

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def power(x, y):
  return x ** y

def square_root(x):
  return math.sqrt(x)

def log(x):
  return math.log(x)

def main():
  print("Welcome to the calculator!")

  while True:
    print("Enter your calculation:")
    x = input()

    if x == "quit":
      break

    try:
      y = eval(x)
      print("The answer is:", y)
    except Exception as e:
      print("Error:", e)

if __name__ == "__main__":
  main()