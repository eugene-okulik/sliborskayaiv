text1 = 'результат операции: 42'
text2 = 'результат операции: 54'
text3 = 'результат работы программы: 209'
text4 = 'результат: 2'

def add_ten(text):
    colon_index = text.index(':')
    result = int(text[colon_index + 1:].strip()) + 10
    print(result)

add_ten(text1)
add_ten(text2)
add_ten(text3)
add_ten(text4)
