text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')

words = text.split()
fin_text = []
for word in words:
    if '.' in word:
        new_word = word.replace('.', 'ing.')
        fin_text.append(new_word)
    elif ',' in word:
        new_word = word.replace(',', 'ing,')
        fin_text.append(new_word)
    else:
        fin_text.append(f'{word}ing')

print(' '.join(fin_text))
