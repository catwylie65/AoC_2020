file = open('input.txt', 'r')

lines = file.read().split('\n')

file.close()

answer_s = 0
answer_e = 0
add_to = 31161678

for index, num1 in enumerate(lines):
  counter = int(num1)
  for index2, num2 in enumerate(lines[index + 1:]):
    counter += int(num2)
    if counter == add_to:
      answer_s = index
      answer_e = index2 + index + 1
      break
    elif counter > add_to:
      break
  if answer_e != 0 and answer_s != 0:
    break

arr = lines[answer_s:answer_e + 1]

# find lowest
lowest = int(arr[0])
# find highest
highest = int(arr[0])
for value in arr:
  if int(value) < lowest:
   lowest = int(value)
  if int(value) > highest:
    highest = int(value)

print(highest + lowest)