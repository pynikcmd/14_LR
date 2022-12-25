#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def typer(types="even"):
    def dele(*args):
        values = [int(arg) for arg in args]

        # Удаление четных элементов по расположению.
        if types == 'even':
            del values[1::2]

        # Удаление нечетных элементов по расположению.
        else:
            del values[0::2]

        return values

    return dele


if __name__ == '__main__':
    print(*typer("keven")(1, 2, 3, 4, 5, 6, 7, 8))
