from collections import defaultdict 

file = open('day7.txt', 'r')

rules = file.read().split('\n')

file.close()

rules_dict = {}

gold_bag_dict = defaultdict(list)

paths = 0

# build gold dictionary
def getGoldDict(target, multiplier):
  total_bags = 0
  # print(target, rules_dict[target])
  for rule in rules_dict[target]:
    # print(rule)
    num_bags = int(rule[0]) * multiplier
    # print('num_bags', num_bags)
    total_bags += num_bags
  gold_bag_dict[target].append(total_bags)
  print(target, gold_bag_dict[target])
  for rule in rules_dict[target]:
    getGoldDict(rule[1], int(rule[0]) * multiplier)

# set up the rules dictionary
for rule in rules:
  var = []
  rule = rule.split(',')
  key = rule[0].split(' contain ')[0].replace('bags', 'bag')
  first_entry = rule[0].split(' contain ')[1].replace('.', '').replace('bags', 'bag').lstrip()
  num = first_entry[0]
  if num == 'n':
    num = '0'
    rules_dict['no other bag'] = []
  var.append([num, ''.join([i for i in first_entry if not i.isdigit()]).lstrip()])
  for bag in rule:
    if bag.find('contain') == -1:
      st = bag.replace('.', '').replace('bags', 'bag').lstrip()
      num = st[0]
      var.append([num, ''.join([i for i in st if not i.isdigit()]).lstrip()])
  rules_dict[key] = var

# call recursive function
getGoldDict('shiny gold bag', 1)

for key in gold_bag_dict.keys():
  for num in gold_bag_dict[key]:
    print(key, 'THE NUM =', num)
    # print(num)
    paths += num
  # print(key, gold_bag_dict[key])

print(paths)
#  is too low 1120
# print('Bag recursion: ', len(gold_bag_dict.keys()) - 1)