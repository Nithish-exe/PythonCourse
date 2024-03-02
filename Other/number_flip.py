num = int(input("Please enter a number: "))
mod_check = num % 10
flip = 0

while num != 0:
    if num < 0:
        num = num * -1
        negate = True
    elif mod_check != 0:
        dig = num % 10
        flip = flip * 10 + dig
        num = num // 10
    elif mod_check == 0:
        while num % 10 == 0:
            flip = flip * 10 + dig
            num = num // 10
if negate:
    flip = flip * -1

print(flip)