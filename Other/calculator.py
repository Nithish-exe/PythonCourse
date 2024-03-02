equ = input("Equation: ")
calc = ['']

# Part 1: converting the equation into a list
i = 0
for char in equ:
    if ord(char) in range(48, 58):
        calc[i] = calc[i] + char
    elif char == " ":
        pass
    else:
        calc.append(char)
        calc.append('')
        i += 2

# Part 2: converting the numbers into the interger type
i = 0
while i < len(calc):
    calc[i] = int(calc[i])
    i += 2

# Part 3: order of operations
i = 1
is_mul = ''
mul = ''
is_div = ''
div = ''
is_add = ''
add = ''
is_sub = ''
sub = ''
while True:
    if '*' in calc:
        mul = calc.index('*')
        is_mul = True
    else:
        is_mul = False
    if '/' in calc:
        div = calc.index('/')
        is_div = True
    else:
        is_div = False

    if is_mul and is_div:
        if mul < div:
            calc[mul] = calc[mul - 1] * calc[mul + 1]
            del calc[mul + 1], calc[mul - 1]
            div = calc.index('/')
            calc[div] = calc[div - 1] / calc[div + 1]
            del calc[div + 1], calc[div - 1]

        elif div < mul:
            calc[div] = calc[div - 1] / calc[div + 1]
            del calc[div + 1], calc[div - 1]
            div = calc.index('*')
            calc[mul] = calc[mul - 1] * calc[mul + 1]
            del calc[mul + 1], calc[mul - 1]

    elif is_mul and not is_div:
        calc[mul] = calc[mul - 1] * calc[mul + 1]
        del calc[mul + 1], calc[mul - 1]

    elif is_div and not is_mul:
        calc[div] = calc[div - 1] / calc[div + 1]
        del calc[div + 1], calc[div - 1]
    else:
        break

while True:
    if '+' in calc:
        add = calc.index('+')
        is_add = True
    else:
        is_add = False
    if '-' in calc:
        sub = calc.index('-')
        is_sub = True
    else:
        is_sub = False

    if is_add and is_sub:
        if add < sub:
            calc[add] = calc[add - 1] + calc[add + 1]
            del calc[add + 1], calc[add - 1]
            sub = calc.index('-')
            calc[sub] = calc[sub - 1] - calc[sub + 1]
            del calc[sub + 1], calc[sub - 1]

        elif sub < add:
            calc[sub] = calc[sub - 1] - calc[sub + 1]
            del calc[sub + 1], calc[sub - 1]
            add = calc.index('+')
            calc[add] = calc[add - 1] + calc[add + 1]
            del calc[add + 1], calc[add - 1]

    elif is_add and not is_sub:
        calc[add] = calc[add - 1] + calc[add + 1]
        del calc[add + 1], calc[add - 1]

    elif is_sub and not is_add:
        calc[sub] = calc[sub - 1] - calc[sub + 1]
        del calc[sub + 1], calc[sub - 1]
    else:
        break

print(calc[0])