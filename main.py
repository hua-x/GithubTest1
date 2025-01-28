# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_hi_1():
    print(f'Hi, ', sys.argv[1])

def repeat(s, exclaim):
    str = s * 3
    if exclaim:
        str += '!!!'
    return str

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm revised')
    repeat('abr', True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# REMove THIS LINE
# after first commit, try push

