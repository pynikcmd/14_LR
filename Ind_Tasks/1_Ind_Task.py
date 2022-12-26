#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def typer(types="even"):
    def dele(*args):
        values = [int(arg) for arg in args]
        i = 0

        # Удаление четных элементов по значению.
        if types == 'even':
            for j in values[:]:
                if j % 2 == 0:
                    del values[i]
                else:
                    i += 1

        # Удаление нечетных элементов по значению.
        else:
            for j in values[:]:
                if j % 2 != 0:
                    del values[i]
                else:
                    i += 1

        return values

    return dele


if __name__ == '__main__':
    print(*typer("even")(2, 9, 4, 7, 8, 4, 2, 15))
