import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

num = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
digit = input('Включить в пароль цифры? (да/нет) ').strip()
lowercase = input('Включить прописные буквы в пароль? (да/нет) ').strip()
uppercase = input('Включить строчные буквы в пароль? (да/нет) ').strip()
punctuations = input('Включить символы, такие как !#$%&*+-=?@^_? в пароль? (да/нет) ').strip()
bad_symbols = input('Исключить символы il1Lo0O из пароля? (да/нет) ').strip()

if digit.lower() == 'да':
    chars += digits
if lowercase.lower() == 'да':
    chars += lowercase_letters
if uppercase.lower() == 'да':
    chars += uppercase_letters
if punctuations.lower() == 'да':
    chars += punctuation
if bad_symbols.lower() == 'да':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)

for _ in range(num):
    generate_password(length, chars)