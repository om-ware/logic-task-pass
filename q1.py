def remove_from(character, letter):
    print('This is the Original letter:-  ',letter)
    new_letter = ""
    for i in range(0, len(letter)):
        if letter[i] != character:
            new_letter = new_letter + letter[i]

    print('This is the letter after deleting :- ')
    return new_letter

res = remove_from('l', "Hello world")
print(res)