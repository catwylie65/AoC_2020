import pandas as pd

df = pd.read_table('day_2.txt', delimiter=' ')

total_valid_passwords = 0

for index, row in df.iterrows():
  letter_rule_at_index_count = 0

  if row.loc['password'][int(row.loc['range'].split('-')[0]) - 1] == row.loc['letter'].split(':')[0]:
    letter_rule_at_index_count += 1
  if row.loc['password'][int(row.loc['range'].split('-')[1]) - 1] == row.loc['letter'].split(':')[0]:
    letter_rule_at_index_count += 1
  if letter_rule_at_index_count == 1:
    total_valid_passwords += 1
  letter_count = 0

print('valid password count: ', total_valid_passwords)