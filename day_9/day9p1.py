file = open('example.txt', 'r')

lines = file.read().split('\n')

file.close()

answer = 0
preamble_len = 5

for index, line in enumerate(lines):
  counter = 0
  if index >= preamble_len:
    start = index - preamble_len
    to_check = lines[start:index]

    for index1, num1 in enumerate(to_check):
      for  num2 in to_check[index1:]:
        if int(num1) + int(num2) == int(line):
          counter += 1
    if counter == 0:
      answer = index
      break

print(lines[answer])