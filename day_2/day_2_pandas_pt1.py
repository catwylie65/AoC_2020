import pandas as pd

df = pd.read_table('day_2.txt', delimiter=' ')

total_valid_passwords = 0

for index, row in df.iterrows():
  letter_count = 0

  for letter in row.loc['password']:
    if letter == row.loc['letter'].split(':')[0]:
      letter_count += 1
  if letter_count >= int(row.loc['range'].split('-')[0]) and letter_count <= int(row.loc['range'].split('-')[1]):
    total_valid_passwords += 1

print('valid password count: ', total_valid_passwords)