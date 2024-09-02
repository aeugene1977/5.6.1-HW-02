def show_field(f):
    num ='  0 1 2'
    print(num)
    for i, row in zip(num.split(), f):
        print (f"{i} {' '.join(str(j) for j in row)}")

def users_input(f, user):
    while True:
        place = input(f"Ходит игрок ({user}). Введите координаты: ").split()
        if len(place) != 2:
            print('ОШИБКА: Введите ровно две координаты!')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('ОШИБКА: Введите только целые числа!')
            continue
        x, y = map(int, place)
        if not(x >= 0 and x <= 2 and y >= 0 and y <= 2):
            print('ОШИБКА: Числа должны быть в диапазоне от 0 до 2 включительно!')
            continue
        if f[x][y] != '-':
            print('ПРЕДУПРЕЖДЕНИЕ: Эта клетка уже занята! Выберите другую.')
            continue
        break
    return x, y

def win_position(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
           check_line(f[0][n], f[1][n], f[2][n], user) or \
           check_line(f[0][0], f[1][1], f[2][2], user) or \
           check_line(f[2][0], f[1][1], f[0][2], user):
           return True
    return False

def start(field):
    count = 0
    while True:
        show_field(field)
        if count %2 == 0:
            user = 'X'
        else:
            user = 'O'
        if count < 9:
            x, y = users_input(field, user)
            field[x][y] = user
        elif count == 9:
            print ('Ничья')
            break
        if win_position(field,user):
            show_field(field)
            print(f"ПОЗДРАВЛЯЕМ, выиграл игрок {user}! Игра окончена.")
            break
        count += 1

field = [['-'] * 3 for _ in range(3)]
print("Игра КРЕСТИКИ-НОЛИКИ")
print("ПРАВИЛА: два игрока поочерёдно делают ход: вводят через пробел координаты (два числа от 0 до 2).")
print("Первое число - номер строки, второе - номер столбца игрового поля, куда нужно поставить крестик или нолик.")
print("Первый игрок ставит только крестики, второй - только нолики.")
print("Выигрывает тот, кто первым поставит на поле три крестика или нолика по горизонтали, вертикали или диагонали.")
start(field)