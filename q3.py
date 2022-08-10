def char_calc(letter,character):
    count = 0
    for i in range(0, len(letter)):
        if letter[i] == character:
            count += 1
    return print('your letter is "',letter,'" and the character "',character,'" repeated ',count,' times')

res = char_calc('hello there', 'l')
print(res)
