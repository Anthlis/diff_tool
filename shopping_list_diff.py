# shopping_list_diff.py

import difflib
import sys

file_1 = open("my_shopping_list.txt").readlines()
file_2 = open("friends_shopping_list.txt").readlines()

delta = difflib.unified_diff(file_1, file_2)
sys.stdout.writelines(delta)