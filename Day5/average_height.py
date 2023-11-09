student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

total_students = 0
for students in student_heights:
  total_students += 1
print(f"number of students = {total_students}")

average = round(total_height/total_students)
print(f"average height = {average}")