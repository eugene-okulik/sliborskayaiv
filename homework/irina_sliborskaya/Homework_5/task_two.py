text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

# to determine indexes
# print(text1.index(':'))
# print(text3.index(':'))

result1 = int(text1[20:])
result2 = int(text2[20:])
result3 = int(text3[27:])

print(result1 + 10)
print(result2 + 10)
print(result3 + 10)

# or another way
# text_options = [
#     'результат операции: 42',
#     'результат операции: 514',
#     'результат работы программы: 9'
# ]
#
# for options in text_options:
#     result = int(options.split(':')[1].strip()) + 10
#     print(result)
