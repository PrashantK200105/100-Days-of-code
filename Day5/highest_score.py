total_score = input().split()
for n in range(0, len(total_score)):
  total_score[n] = int(total_score[n])

highest_score = 0
for score in total_score:
  if score > highest_score:
    highest_score = score

print(f"The highest score of the class is: {highest_score}.")
  