import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def password_main():
    input('Какое количество паролей сгенерировать? ').isdigit()
    input('Какова длина будущего пароля? ').isdigit()
    input('Включать ли цифры 0123456789? (Да/Нет) ').capitalize()
    input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (Да/Нет) ').capitalize()
    input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (Да/Нет) ').capitalize()
    input('Включать ли символы !#$%&*+-=?@^_? (Да/Нет) ').capitalize()
    input('Исключать ли неоднозначные символы il1Lo0O? (Да/Нет) ').capitalize()

password_main()