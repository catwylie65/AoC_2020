file = open('day_2.txt', 'r')

password_array = file.read().split('\n')
file.close()

total_valid_passwords = 0

for password in password_array:
  split_string = password.split(' ')
  numbers = split_string[0].split('-')
  index_one = int(numbers[0]) - 1
  index_two = int(numbers[1]) - 1
  letter_rule = split_string[1].split(':')[0]
  password_string = split_string[2]
  letter_rule_at_index_count = 0
  if password_string[index_one] == letter_rule:
    letter_rule_at_index_count += 1
  if password_string[index_two] == letter_rule:
    letter_rule_at_index_count += 1
  if letter_rule_at_index_count == 1:
    total_valid_passwords += 1


print('Total valid passwords: ', total_valid_passwords)