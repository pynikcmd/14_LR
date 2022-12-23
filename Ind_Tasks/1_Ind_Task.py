#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def typer(types="even"):
    def dele(*args):
        values = [int(arg) for arg in args]
        # удаление четных
        if types == 'even':
            values = [itm for itm in values if itm % 2 != 0]
        # удаление нечетных
        else:
            values = [itm for itm in values if itm % 2 == 0]
        return values

    return dele


if __name__ == '__main__':
    print(*typer("noteven")(2, 9, 7, 8, 4, 2, 15))
