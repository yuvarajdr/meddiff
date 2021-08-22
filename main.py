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
        left(i)
        forward(i * 3)
        x = x - 1


def switch(ca):
    if ca == 1:
        n = int(input("number of dictionary values\n"))
        for i in range(n):
            text = input("enter dictionary value with space\n").split()
            Dict[text[0]] = text[1]
        dictionary_sort(Dict)
    elif ca == 2:
        s = input("enter palindrome string which should be tested\n \t")
        ispalindrome(s)
    elif ca == 3:
        angle = int(input("enter angle to start\n"))
        graphicturtle(angle)
    else:
        print("incorrect case please insert numbers within 1 -2\n \t")
        ca = int(input("enter problem number to answer"))
        switch(ca)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    Dict = {}
    cas = int(input("enter problem number to answer\n \t"))
    switch(cas)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
