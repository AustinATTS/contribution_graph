#!/usr/bin/env python
import argparse
import os
from datetime import datetime
from datetime import timedelta
from random import randint
from subprocess import Popen
import sys


def contribute(date):
    with open(os.path.join(os.getcwd(), 'birth.txt'), 'a') as file:
        file.write(message(date) + '\n\n')
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', '"%s"' % message(date),
         '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])


def run(commands):
    Popen(commands).wait()


def message(date):
    return date.strftime('Contribution: %Y-%m-%d %H:%M')


contribute(datetime(2007, 1, 28, 12, 12, 12))
contribute(datetime(2007, 1, 22, 12, 12, 12))
contribute(datetime(2007, 1, 23, 12, 12, 12))
contribute(datetime(2007, 1, 24, 12, 12, 12))
contribute(datetime(2007, 1, 25, 12, 12, 12))
contribute(datetime(2007, 1, 26, 12, 12, 12))
contribute(datetime(2007, 1, 27, 12, 12, 12))
contribute(datetime(2007, 1, 20, 12, 12, 12))
contribute(datetime(2007, 2, 3, 12, 12, 12))
contribute(datetime(2007, 2, 25, 12, 12, 12))
contribute(datetime(2007, 2, 26, 12, 12, 12))
contribute(datetime(2007, 2, 27, 12, 12, 12))
contribute(datetime(2007, 2, 28, 12, 12, 12))
contribute(datetime(2007, 3, 1, 12, 12, 12))
contribute(datetime(2007, 3, 2, 12, 12, 12))
contribute(datetime(2007, 3, 3, 12, 12, 12))
contribute(datetime(2007, 3, 9, 12, 12, 12))
contribute(datetime(2007, 3, 15, 12, 12, 12))
contribute(datetime(2007, 3, 23, 12, 12, 12))
contribute(datetime(2007, 3, 25, 12, 12, 12))
contribute(datetime(2007, 3, 26, 12, 12, 12))
contribute(datetime(2007, 3, 27, 12, 12, 12))
contribute(datetime(2007, 3, 28, 12, 12, 12))
contribute(datetime(2007, 3, 29, 12, 12, 12))
contribute(datetime(2007, 3, 30, 12, 12, 12))
contribute(datetime(2007, 3, 31, 12, 12, 12))
contribute(datetime(2007, 4, 9, 12, 12, 12))
contribute(datetime(2007, 4, 10, 12, 12, 12))
contribute(datetime(2007, 4, 11, 12, 12, 12))
contribute(datetime(2007, 4, 12, 12, 12, 12))
contribute(datetime(2007, 4, 13, 12, 12, 12))
contribute(datetime(2007, 4, 14, 12, 12, 12))
contribute(datetime(2007, 4, 15, 12, 12, 12))
contribute(datetime(2007, 4, 22, 12, 12, 12))
contribute(datetime(2007, 4, 29, 12, 12, 12))
contribute(datetime(2007, 4, 17, 12, 12, 12))
contribute(datetime(2007, 4, 24, 12, 12, 12))
contribute(datetime(2007, 5, 1, 12, 12, 12))
contribute(datetime(2007, 5, 7, 12, 12, 12))
contribute(datetime(2007, 5, 8, 12, 12, 12))
contribute(datetime(2007, 5, 9, 12, 12, 12))
contribute(datetime(2007, 5, 10, 12, 12, 12))
contribute(datetime(2007, 5, 11, 12, 12, 12))
contribute(datetime(2007, 5, 12, 12, 12, 12))
