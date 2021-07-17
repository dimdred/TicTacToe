from texttable import Texttable

initial_arr = list(range(1, 10))
print('Welcome to Tic Tac Toe game!')

pl1_arr = []
pl2_arr = []
winning_combinations = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
is_game = True


def print_table(p_arr):
    t = Texttable()
    arr = [p_arr[:3], p_arr[3:6], p_arr[-3:]]
    t.add_rows(arr, header=False)
    print(t.draw())


def check_winner(pl_arr):
    return any(winning_combination.issubset(set(pl_arr)) for winning_combination in winning_combinations)


print_table(initial_arr)

while is_game:
    num1 = int(input('Player1 (X), enter the number? '))
    pl1_arr.append(num1)
    initial_arr = ['X' if num1 == x else x for x in initial_arr]
    print_table(initial_arr)
    print(pl1_arr)
    if check_winner(pl1_arr):
        print('Player1 won! Game over.')
        break

    num2 = int(input('Player2 (O), enter the number? '))
    pl2_arr.append(num2)
    initial_arr = ['O' if num2 == x else x for x in initial_arr]
    print_table(initial_arr)
    print(pl2_arr)
    if check_winner(pl2_arr):
        print('Player2 won! Game over.')
        break
