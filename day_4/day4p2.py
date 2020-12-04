import re
file = open('day_4.txt', 'r')

p = file.read().split('\n\n')

file.close()


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
  # If cm, the number must be at least 150 and at most 193.
  # If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
def isValid(field, value):
  if field == 'cid':
    return False 
  elif field == 'byr' and int(value) <= 2002 and int(value) >= 1920:
    return True
  elif field == 'iyr' and int(value) <= 2020 and int(value) >= 2010:
    return True
  elif field == 'eyr' and int(value) <= 2030 and int(value) >= 2020:
    return True
  elif field == 'hgt':
    cm = value.split('cm')
    inches = value.split('in')
    if value.find('cm') != -1 and int(cm[0]) >= 150 and int(cm[0]) <=193: 
      return True
    elif value.find('in') != -1 and int(inches[0]) >= 59 and int(inches[0]) <= 76:
      return True
  elif field == 'hcl':
    if len(value) == 7 and re.match("^#[a-f0-9]+$", value):
      return True
  elif field == 'ecl':
    if value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth':
      return True
  elif field == 'pid':
    if value.isdigit() and len(value) == 9:
      return True
  return False

passports = []
valid_passports = 0

# get that data right
for x in p:
  line = x.replace('\n', ' ')
  fields = line.split(' ')
  parsed = []
  for field in fields:
    parsed.append(field.split(':'))

  passports.append(parsed)

# check that data
for passport in passports:
  valid_fields = 0
  for field in passport:
    if(isValid(field[0], field[1])):
      valid_fields += 1
  if valid_fields == 7:
    valid_passports += 1

print('valid passports: ', valid_passports)
