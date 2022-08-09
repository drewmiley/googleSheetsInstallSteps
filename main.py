import gspread
import logging
import os
from dotenv import load_dotenv

load_dotenv()

Template_id = os.getenv('Template_id')
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# For running through terminal
# logging.basicConfig(filename="log.txt", level=logging.DEBUG)
# For running through py2app
logging.basicConfig(filename="../../../../log.txt", level=logging.DEBUG)

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
print_hi('PyCharm')
logging.debug('Hi, PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

gc = gspread.oauth(
    credentials_filename='credentials.json',
    authorized_user_filename='authorized_user.json'
)

# sh = gc.open("TEST")
sh = gc.open_by_key(Template_id)

print(sh.sheet1.cell(2, 2).value)
logging.debug(sh.sheet1.cell(2, 2).value)
