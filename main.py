import gspread
import logging
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# For running through terminal
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
# For running through py2app
logging.basicConfig(filename="../../../../log.txt", level=logging.DEBUG)

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
print_hi('PyCharm')
logging.debug('Hi, PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# gc = gspread.oauth(
#     credentials_filename='credentials.json'
# )
#
# sh = gc.open("TEST")
#
# print(sh.sheet1.cell(1, 1).value)
