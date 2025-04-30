PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list = PRICE_LIST.split()

key = list[::2]
price = [int(p[:-1]) for p in list[1::2]]

new_dict = dict(zip(key, price))
print(new_dict)
