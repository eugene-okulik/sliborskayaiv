text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

colon_index1 = text1.index(':')
colon_index2 = text2.index(':')
colon_index3 = text3.index(':')

result1 = int(text1[colon_index1 + 1:].strip()) + 10
result2 = int(text2[colon_index2 + 1:].strip()) + 10
result3 = int(text3[colon_index3 + 1:].strip()) + 10

print(result1)
print(result2)
print(result3)
