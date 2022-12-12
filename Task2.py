# Создайте программу для игры в ""Крестики-нолики"".

# Создаём функцию для заполнения нашего поля игры
board = list(range(1,10))
def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

# Пишем функцию выбора Х и О, ввод будет осуществляться взависимости от выбранного номера клетки, с учетом проверки
# её занятости и корректного значения от 1 до 9
def input_token(player_token):
    valid = False
    while not valid:
        player_answer = input(f"Куда поставим {player_token}?: ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта ячейка уже занята")
        else:
            print("Некорректный ввод! Введите число от 1 до 9!")

# Пишем функцию для определения победы. Для этого перебираем все возможные варианты победы, если победный вариант во
# время игры достигается, то возвращаем выигрышный символ
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

# Функция самой игры. Это итоговая функция в которой собираем все функции для этого
def game(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            input_token("X")
        else:
            input_token("O")
        counter += 1
        if counter > 4:
            x = check_win(board)
            if x:
                print(x, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

game(board)