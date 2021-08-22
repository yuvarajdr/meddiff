# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Dict, Any
from turtle import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def dictionary_sort(dictionary):
    d = {}
    dkeys = dictionary.values()

    setlist = set(dkeys)
    dkeys = list(setlist)
    d_s_l = []
    for i in dkeys:
        for x, y in dictionary.items():
            if y == i:
                d_s_l.append(x)
        d[i] = d_s_l
        d_s_l = []
    print(d)


def ispalindrome(s):
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")


def graphicturtle(i):
    speed(8)
    color('yellow')
    bgcolor('black')
    x = i
    while x > 0:
        left(x)
        forward(x * 3)
        x = x - 1


class Path:
    def __init__(self, s, cd):
        self.s = s
        self.cd = cd

    def pathcd(self):
        sl = self.s.split('/')
        cdl = self.cd.split('/')
        for i in sl:
            if not i.isalpha():
                input("insert correct path\n")
                switch('4')
        for i in cdl:
            if i.isalpha() or i == "..":
                while i:
                    if i == "..":
                        sl.pop()
                        break
                    elif i.isalpha():
                        sl.append(i)
                        break
            else:
                input("insert correct path\n")
                switch('4')
        separators = '/'
        s = separators.join(sl)
        print(s)


def switch(ca):
    while ca:
        if ca == '1':
            n = int(input("number of dictionary values\n"))
            for i in range(n):
                text = input("enter dictionary value with space\n").split()
                Dict[text[0]] = text[1]
            dictionary_sort(Dict)
            ca = input("enter problem number to answer\n")
            switch(ca)
        elif ca == '2':
            s = input("enter palindrome string which should be tested\n \t")
            ispalindrome(s)
            ca = input("enter problem number to answer\n")
            switch(ca)
        elif ca == '4':
            s = input("enter file path\n \t")
            cd = input("change directory\n \t")
            Paths = Path(s, cd)
            Paths.pathcd()
            ca = input("enter problem number to answer\n")
            switch(ca)
        elif ca == '10':
            angle = int(input("enter angle to start\n"))
            graphicturtle(angle)
            ca = input("enter problem number to answer\n")
            switch(ca)
        elif ca == '0':
            break
        else:
            print("incorrect case please insert numbers within 1,2 4 and 0 for exit\n \t")
            ca = input("enter problem number to answer\n")
            switch(ca)


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('PyCharm')
    Dict = {}
    cas = input("enter problem number 1,2 4 and 0 for exit\n \t")
    switch(cas)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
