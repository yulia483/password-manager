passwords=[]
file_name= "passwords.txt"
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
            print("Функция генерации в разработке")
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