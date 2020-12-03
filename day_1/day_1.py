file = open('day_1.txt', 'r')

number_array = file.read().split()
file.close()

# part one
print('Part 1: ')
number1 = 0
number2 = 0

for x in number_array:
    for y in number_array:
        if int(x) + int(y) == 2020:
            number1 = int(x)
            number2 = int(y)

print(number1)
print(number2)
print(number1 * number2)

# part 2
print('Part 2: ')

a = 0
b = 0
c = 0

for x in number_array:
    for y in number_array:
        for z in number_array:
            if int(x) + int(y) + int(z) == 2020:
                a = int(x)
                b = int(y)
                c = int(z)

print(a)
print(b)
print(c)
print(a*b*c)
