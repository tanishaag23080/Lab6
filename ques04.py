n = int(input())
n_backup = n

if n > 0:
  octal = 0
  i = 0
  while n > 0:
    remainder = n%8
    octal += remainder*(10**i)
    n = n//8
    i += 1

  print('Octal:', str(octal))

  if octal == oct(n_backup):
    print('It matches the built-in function output')
else:
  print('Invalid Input')
