# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Dict, Any


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def dictionary_sort(dictionary):
    d={}
    dkeys=dictionary.values()

    setlist = set(dkeys)
    dkeys = list(setlist)
    d_s_l=[]
    for i in dkeys:
        for x, y in dictionary.items():
            if y == i:
                d_s_l.append(x)
        d[i]=d_s_l
        d_s_l=[]
    print(d)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    Dict = {}
    n=int(input("number of dictionary values\n"))
    for i in range(n):
        text = input("enter dictionary value with space\n").split()
        Dict[text[0]] = text[1]

    dictionary_sort(Dict)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
