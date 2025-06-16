#Question1
from math import ceil

def is_prime(n):
  is_prime = True
  if n < 0:
    raise ValueError("Negative numbers cannot be prime.")
  if n <= 1:
    print(f"{n} is not a prime number")
  for i in range(2, ceil(n**0.5) + 1):
    if n % i == 0:
      is_prime = False
      break

  if is_prime:
    print(f"{n} is a prime number")
  else:
    print(f"{n} is not a prime number")

is_prime(int(input("Enter a number: ")))