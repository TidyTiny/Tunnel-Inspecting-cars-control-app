import os
def open_mysql():
    command = '''start cmd /k "d: & cd d:/HOME/QT_text/ & python d:/HOME/QT_text/MySQL.py "{$name$:$qcy$}" && exit"'''
    os.system(command)
# open_mysql()
