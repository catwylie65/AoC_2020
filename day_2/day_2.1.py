file = open('day_2.txt', 'r')

password_array = file.read().split('\n')
file.close()

total_valid_passwords = 0

for password in password_array:
  split_string = password.split(' ')
  numbers = split_string[0].split('-')
  low_range = int(numbers[0])
  high_range = int(numbers[1])
  letter_rule = split_string[1].split(':')[0]
  password_string = split_string[2]
  letter_count = 0
  for letter in password_string:
    if letter == letter_rule:
      letter_count += 1
  if letter_count >= low_range and letter_count <= high_range:
    total_valid_passwords += 1

print('valid password count: ', total_valid_passwords)