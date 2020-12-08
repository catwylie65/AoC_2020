from collections import defaultdict 

file = open('day7.txt', 'r')

rules = file.read().split('\n')

file.close()

rules_dict = {}

gold_bag_dict = defaultdict(list)

paths = 0

def getGoldDict(target):
  for key in rules_dict.keys():
    for rule in rules_dict[key]:
      if rule == target:
        if key not in gold_bag_dict[target]:
          gold_bag_dict[target].append(key)
  for rule in gold_bag_dict[target]:
    getGoldDict(rule)

for rule in rules:
  var = []
  rule = rule.split(',')
  key = rule[0].split(' contain ')[0].replace('bags', 'bag')
  first_entry = rule[0].split(' contain ')[1].replace('.', '').replace('bags', 'bag')
  var.append(''.join([i for i in first_entry if not i.isdigit()]).lstrip())
  for bag in rule:
    if bag.find('contain') == -1:
      st = bag.replace('.', '').replace('bags', 'bag')
      var.append(''.join([i for i in st if not i.isdigit()]).lstrip())
  rules_dict[key] = var

getGoldDict('shiny gold bag')

print('Bag recursion: ', len(gold_bag_dict.keys()) - 1)