while True:
    print ("Введите число или exit для выхода из программы")
    n = input()
    if n == "exit":
            break
    elif n.isdigit() is not True:
        raise TypeError("Ошибка типа данных, введено слово. Попробуйте снова")
    else: print("Символов в числе:",len(str(n)))


