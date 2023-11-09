numbers = int(input())
total = 0
for even in range(2, numbers + 1, 2):
  total += even

print(f"Sum of all even number is: {total}.")