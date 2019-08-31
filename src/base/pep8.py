sample_list = [100000000, 200000000, 300000000, 400000000, 500000000,
               600000000, 700000000]

foo = long_function_name(
    var_one, var_two, var_three, var_four)

def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

if (var_one == 100 
        and var_two == 200
        and var_three == 300):
    do_something()

with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)


def sample_func_1():
    pass


def sample_func_2():
    pass


class SampleClass():
    pass


class SampleClass():

    def __init__(self):
        pass

    def sample_func_1(self):
        pass

# import os, sys といったように、1行にまとめるべきではありません。
import os
import sys

from datetime import datetime, date

import os
import shutil
import sys

import numpy as np
import pandas as pd

from apps.your_app import your_module

# 以下好ましくない例。

# hamの前や1の前後、eggsの前、2の後など、不要なスペースは
# 入れるべきではありません。
spam( ham[ 1 ], { eggs: 2 } )

# tuple定義のためのコンマの後にも、不要なスペースは入れるべきでは
# ありません。
bar = (0, )

# 関数と括弧でスペースを入れるべきではありません。
sample_func (1)

# 辞書やリストなども、変数名と括弧の間にスペースを
# 入れるべきではありません。
dct ['key'] = lst [index]

ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]

ham[lower:upper], ham[lower:upper:], ham[lower::step]

ham[lower+offset : upper+offset]
ham[lower + offset : upper + offset]

# この例では、コロンの左の括弧との間にはスペースを入れていません。
ham[: upper_fn(x) : step_fn(x)]
ham[:: step_fn(x)]

x             = 1
y             = 2
long_variable = 3

# imgの後のデフォルト引数のイコールの前後には
# スペースを入れません。
def complex(real, imag=0.0):
    # キーワード引数を指定する際にも、イコールの
    # 前後にはスペースを入れません。
    return magic(r=real, i=imag)

if foo == 'blah': do_blah_thing()

FILES = [
    'setup.cfg',
    'tox.ini',
    ]

try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
