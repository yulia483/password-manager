import random
import string
passwords=[]
file_name= "passwords.txt"
def enc(t, k):
    # Шифрует пароль сдвигом символов по ключу
    r = ""
    for ch in t:
        r += chr(ord(ch) + k)
    return r

def dec(t, k):
    # Расшифровывает пароль обратно
    r = ""
    for ch in t:
        r += chr(ord(ch) - k)
    return r

def gen():
    #Генерирует случайный пароль заданной длины
    x = input("Введите длину пароля (от 8 до 32): ").strip()
    if not x.isdigit():
        print("Ошибка: нужно ввести целое число!")
        return ""

    n = int(x)
    if n < 8 or n > 32:
        print("Пароль должен быть длиной от 8 до 32 символов")
        return ""

    s = string.ascii_letters + string.digits + "!@#$%&*"
    p = ""
    for i in range(n):
        p += random.choice(s)

    print("Сгенерированный пароль:", p)
    return p
    
def f():
    print("====Защищённый менеджер паролей====")
    key_str = input("Введите числовой мастер-ключ (например, 1234): ").strip()
    if not key_str.isdigit():
        print("Ошибка: мастер-ключ должен состоять из цифр!")
        return

    secret_key = int(key_str) % 500 + 1

    while True:
        print("\n====Менеджер паролей====")
        print("1. Сгенерировать пароль")
        print("2. Добавить пароль в хранилище")
        print("3. Показать все пароли")
        print("4. Найти пароль по сайту")
        print("5. Удалить пароль")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            gen()
        elif choice == "2":
            print("Функция добавления в разработке")
        elif choice == "3":
            print("Функция просмотра в разработке")
        elif choice == "4":
            print("Функция поиска в разработке")
        elif choice == "5":
            print("Функция удаления в разработке")
        elif choice == "0":
            print(" Программа завершена")
            break
        else:
            print("Такого пункта нет")
f()