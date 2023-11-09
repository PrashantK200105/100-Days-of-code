numbers = 100
for fizz_buzz in range(1, numbers + 1):
 if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
  print("Fizz Buzz")
 elif fizz_buzz % 3 == 0:  
   print("Fizz")
 elif fizz_buzz % 5 == 0:
   print("Buzz")
 else:
   print(fizz_buzz)


