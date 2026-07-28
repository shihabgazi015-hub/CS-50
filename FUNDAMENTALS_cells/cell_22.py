def main():
  x = int(input("What's x?\n"))
  print("x squared is", square(x))

def square(n):
  return pow(n,2) # we can also use n**2

# calling the main() function
main()