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


contribute(datetime(2007, 8, 27, 12, 12, 12))
contribute(datetime(2007, 8, 28, 12, 12, 12))
contribute(datetime(2007, 8, 29, 12, 12, 12))
contribute(datetime(2007, 8, 30, 12, 12, 12))
contribute(datetime(2007, 8, 31, 12, 12, 12))
contribute(datetime(2007, 9, 24, 12, 12, 12))
contribute(datetime(2007, 9, 25, 12, 12, 12))
contribute(datetime(2007, 9, 26, 12, 12, 12))
contribute(datetime(2007, 9, 27, 12, 12, 12))
contribute(datetime(2007, 9, 28, 12, 12, 12))
contribute(datetime(2007, 9, 29, 12, 12, 12))
contribute(datetime(2007, 9, 8, 12, 12, 12))
contribute(datetime(2007, 9, 15, 12, 12, 12))
contribute(datetime(2007, 9, 22, 12, 12, 12))
contribute(datetime(2007, 9, 2, 12, 12, 12))
contribute(datetime(2007, 9, 9, 12, 12, 12))
contribute(datetime(2007, 9, 16, 12, 12, 12))
