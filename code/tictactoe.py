#!/usr/bin/env python3

from random import randint, random


board = [["-" for c in range(3)] for r in range(3)]


def columns() -> list[list]:
    return [[board[r][c] for r in range(3)] for c in range(3)]


def diags() -> list[list]:
    return [
        [board[_][_] for _ in range(3)],  # dexter
        [board[3 - _ - 1][_] for _ in range(3)],  # sinister
    ]


def do_move(turn, player, action, row, column):
    board[row][column] = player
    print(
        f"DEBUG: "
        f"turn={turn}, "
        f"player={current_player}, "
        f"action={action}, "
        f"row={row}, "
        f"column={column}"
    )


def do_show() -> None:
    for r in range(3):
        for c in range(3):
            print(board[r][c], end=" ")
        print()


def rows() -> list[list]:
    return board


try:
    for turn in range(1, 3 * 2):
        print(f"Turn {turn}...")

        for current_player, other_player in [("X", "O"), ("O", "X")]:

            if turn == (3 * 2 - 1) and current_player == "O":
                continue

            try:
                r, c = None, None

                if turn == 1:
                    if current_player == "X" and random() > 0.64:
                        r, c = 1, 1

                    if current_player == "O" and random() > 0.64:
                        r, c = (1, 1) if board[1][1] == "-" else (0, 0)

                    if all(
                        [
                            r is not None,
                            c is not None,
                        ]
                    ):
                        raise StopIteration("opening")

                for d, diag in enumerate(diags()):
                    if diag.count("-") == 0:
                        continue

                    c = diag.index("-")

                    if d == 0:  # dexter
                        r = diag.index("-")
                    else:  # sinister
                        r = 3 - 1 - diag.index("-")

                    if diag.count(current_player) == 2:
                        raise StopIteration("diag finish")

                    if diag.count(other_player) == 2:
                        raise StopIteration("diag defense")

                for r, row in enumerate(rows()):
                    if row.count("-") == 0:
                        continue

                    c = row.index("-")

                    if row.count(current_player) == 2:
                        raise StopIteration("row finish")

                    if row.count(other_player) == 2:
                        raise StopIteration("row defense")

                for c, column in enumerate(columns()):
                    if column.count("-") == 0:
                        continue

                    r = column.index("-")

                    if column.count(current_player) == 2:
                        raise StopIteration("column finish")

                    if column.count(other_player) == 2:
                        raise StopIteration("column defense")

                for r, row in enumerate(rows()):
                    if row.count("-") == 0:
                        continue

                    if row.count(other_player) == 1:
                        continue

                    if row.count(current_player) == 1:
                        c = row.index("-")
                        raise StopIteration("row attack")

                for c, column in enumerate(columns()):

                    if column.count("-") == 0:
                        continue

                    if column.count(other_player) == 1:
                        continue

                    if column.count(current_player) == 1:
                        r = column.index("-")
                        raise StopIteration("column attack")

                while True:
                    r = randint(0, 2)
                    c = randint(0, 2)
                    if board[r][c] == "-":
                        raise StopIteration("random")

            except StopIteration as action:
                do_move(
                    turn=turn, player=current_player, action=action, row=r, column=c
                )
                do_show()

            if any(
                [
                    [True for row in rows() if row.count(current_player) == 3],
                    [True for column in columns() if column.count(current_player) == 3],
                    [True for diag in diags() if diag.count(current_player) == 3],
                ]
            ):
                raise StopIteration(f"{current_player}")

    print("Draw!..")

except StopIteration as player:
    print(f"Player {player} wins!..")
