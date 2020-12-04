file = open('day_4.txt', 'r')

passports = file.read().split('\n\n')

file.close()
valid_passports = 0
fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
for passport in passports:
  valid_fields = 0
  for field in fields:
    if passport.find(field) != -1:
      valid_fields += 1
  if valid_fields == 7:
    valid_passports += 1

print(valid_passports)
  